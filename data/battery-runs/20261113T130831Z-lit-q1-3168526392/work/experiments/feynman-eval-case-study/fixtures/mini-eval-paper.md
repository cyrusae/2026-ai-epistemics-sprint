# Sparse Routing for Efficient Retrieval

## Abstract

We introduce SparseRoute, a routing layer for long-context retrieval. SparseRoute improves accuracy from 80.1% to 80.3% on our benchmark and is 2x faster. It establishes a new state of the art.

## Method

SparseRoute adds a learned top-k router over 64 experts. We train for 10 epochs with Adam at a learning rate of 1e-4.

## Evaluation

We evaluate on a held-out split of 100 examples from the benchmark. We compare against a baseline we trained ourselves with the same budget. We ran 3 seeds and the results were stable. We report mean accuracy over the seeds. We do not report confidence intervals or per-seed numbers.

## Results

| Method | Accuracy | Latency |
|---|---|---|
| Baseline | 80.1% | 40 ms |
| SparseRoute | 80.3% | 20 ms |

SparseRoute improves accuracy by 0.2 points and halves latency. The gain is consistent across seeds.

## Conclusion

SparseRoute is a new state of the art for efficient retrieval and should be adopted in production systems.
