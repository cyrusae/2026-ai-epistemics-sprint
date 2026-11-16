#!/usr/bin/env bash
# check-public.sh [ref]  — scan everything that `git push <ref>` would publish:
# file contents and paths in EVERY commit reachable from ref (not just the tip),
# plus commit messages. Exits 1 if anything matches.
#
# What it looks for:
#   - each line of .public-denylist (case-insensitive fixed strings; gitignored,
#     because a committed list of identifiers would itself identify the paper)
#   - the literal values of every key in .env, and generic API-key shapes
#   - .env or run directories tracked by git
# It also prints the author/committer identities that would be published.
set -uo pipefail
cd "$(git rev-parse --show-toplevel)"
REF="${1:-HEAD}"
git rev-parse --verify -q "$REF^{commit}" >/dev/null || { echo "no such ref: $REF" >&2; exit 2; }
COMMITS=$(git rev-list "$REF")
echo "Scanning $REF: $(echo "$COMMITS" | wc -l | tr -d ' ') commit(s), all history reachable from it"
fail=0
hit() { fail=1; printf '\n\033[31mFAIL\033[0m %s\n' "$1"; }

pats=()
if [ -f .public-denylist ]; then
  while IFS= read -r l; do l="${l%%#*}"; l="$(echo "$l" | sed 's/[[:space:]]*$//')"; [ -n "$l" ] && pats+=("$l"); done < .public-denylist
else
  echo "warning: no .public-denylist, only checking for secrets" >&2
fi

for p in "${pats[@]+"${pats[@]}"}"; do
  out=$(git grep -I -l -i -F -e "$p" $COMMITS -- 2>/dev/null | sed 's/^[0-9a-f]*://' | sort -u)
  [ -n "$out" ] && { hit "\"$p\" in file contents:"; echo "$out" | sed 's/^/  /'; }
  out=$(for c in $COMMITS; do git ls-tree -r --name-only "$c"; done | sort -u | grep -i -F -e "$p")
  [ -n "$out" ] && { hit "\"$p\" in file paths:"; echo "$out" | sed 's/^/  /'; }
  out=$(git log --format='%h %s%n%b' "$REF" | grep -i -F -e "$p")
  [ -n "$out" ] && { hit "\"$p\" in commit messages:"; echo "$out" | sed 's/^/  /'; }
done

# secrets: literal .env values (never printed) + generic key shapes
if [ -f .env ]; then
  while IFS= read -r l; do
    v="${l#*=}"; v="$(echo "$v" | tr -d '"'"'"' \r')"
    [ ${#v} -ge 12 ] || continue
    out=$(git grep -I -l -F -e "$v" $COMMITS -- 2>/dev/null | sed 's/^[0-9a-f]*://' | sort -u)
    [ -n "$out" ] && { hit "a value from .env (redacted) in:"; echo "$out" | sed 's/^/  /'; }
  done < <(grep -v '^[[:space:]]*#' .env | grep -v '^[[:space:]]*$')
fi
out=$(git grep -I -l -E -e 'sk-or-v1-[0-9a-f]{20,}' -e 'sk-ant-[A-Za-z0-9_-]{20,}' -e 'sk-[A-Za-z0-9]{32,}' $COMMITS -- 2>/dev/null | sed 's/^[0-9a-f]*://' | sort -u)
[ -n "$out" ] && { hit "API-key-shaped strings in:"; echo "$out" | sed 's/^/  /'; }
out=$(for c in $COMMITS; do git ls-tree -r --name-only "$c"; done | sort -u | grep -E '(^|/)\.env$|(^|/)runs/|(^|/)auth\.json$')
[ -n "$out" ] && { hit "files that should never be tracked:"; echo "$out" | sed 's/^/  /'; }

echo; echo "Identities that would be published (author/committer):"
git log --format='  %an <%ae>%n  %cn <%ce>' "$REF" | sort -u

if [ $fail = 0 ]; then printf '\n\033[32mOK\033[0m nothing on the denylist or secret checks in %s\n' "$REF"; else printf '\n\033[31mNot safe to publish %s.\033[0m\n' "$REF"; fi
exit $fail
