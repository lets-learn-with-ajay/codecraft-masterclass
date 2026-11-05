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

func main() {
    // CodeCraft Masterclass entry point
}

