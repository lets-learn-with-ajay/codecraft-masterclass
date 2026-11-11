package main

// Phase 1: gRPC Unary Interceptor with Context Deadline & Rate Guard
package gateway

import (
    "context"
    "errors"
    "sync/atomic"
    "time"
)

type GatewayRateGuard struct {
    inflight   atomic.Int64
    maxAllowed int64
}

func (g *GatewayRateGuard) Acquire(ctx context.Context) error {
    if g.inflight.Add(1) > g.maxAllowed {
        g.inflight.Add(-1)
        return errors.New("rate limit exceeded: shedding load")
    }
    if _, ok := ctx.Deadline(); !ok {
        var cancel context.CancelFunc
        _, cancel = context.WithTimeout(ctx, 25*time.Millisecond)
        defer cancel()
    }
    return nil
}

// Phase 2: Batch Write Coalescer for High-Throughput gRPC Streams
package gateway

type WriteMutation struct {
    Key   string
    Value []byte
}

func CoalesceWriteBatch(mutations []WriteMutation) map[string][]byte {
    merged := make(map[string][]byte, len(mutations))
    for _, m := range mutations {
        merged[m.Key] = m.Value
    }
    return merged
}

// Phase 3: Lock-Free Microsecond Latency Percentile Tracker
package gateway

import "sort"

func ComputeP99Micros(samplesUs []int64) int64 {
    if len(samplesUs) == 0 {
        return 0
    }
    cp := append([]int64(nil), samplesUs...)
    sort.Slice(cp, func(i, j int) bool { return cp[i] < cp[j] })
    idx := int(float64(len(cp)-1) * 0.99)
    return cp[idx]
}

func main() {
    // CodeCraft Masterclass entry point
}

