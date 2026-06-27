# Example: SM90 FP8 Layout Notes

## Context

I was studying how an MoE FP8 path should be implemented on H200/SM90, especially around Sonic-MoE, QuACK, and grouped GEMM layouts.

## Confusion

The confusing part was that the same mathematical GEMM can become a different memory-layout problem depending on whether it is forward, dgrad, or wgrad.

For example, with row-major tensors:

```text
X: [B, H]
Y: [B, I]
W: [I, H]
```

`Y = X @ W.T` naturally gives a K-major contraction for both operands. But `dX = dY @ W` can expose `W` in an MN-major layout, which is fine for BF16 on SM90 but problematic for FP8 WGMMA paths that require K-major operands.

## Investigation

The useful distinction was not just dtype. BF16 and FP8 differ in what operand layouts the target kernel path can accept. In this case, the FP8 path needs an explicit GEMM-ready layout or a cached/transposed representation.

## Finding

The practical design direction is:

- keep BF16 baseline untouched;
- add FP8 paths one GEMM at a time;
- treat FP8 weight layout/cache as part of the kernel contract, not as a cosmetic `.contiguous()` detail;
- keep draft notes separate from published posts until the idea is stable.

## Takeaway

For SM90 FP8 work, layout is a first-class constraint. A correct-looking PyTorch shape can still be the wrong physical layout for the actual WGMMA kernel.

