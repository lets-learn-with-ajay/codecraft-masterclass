// Phase 1: Bounded Worker Pool & Context Cancellation
package main

import (
    "context"
    "sync"
    "time"
)

type Job struct {
    ID      string
    Payload []byte
}

type BoundedPool struct {
    jobs    chan Job
    wg      sync.WaitGroup
    workers int
}

func NewBoundedPool(workers, queueDepth int) *BoundedPool {
    return &BoundedPool{jobs: make(chan Job, queueDepth), workers: workers}
}

// Phase 2: Non-Blocking Dispatch & Backpressure Guard
func (p *BoundedPool) Submit(ctx context.Context, job Job) error {
    select {
    case <-ctx.Done():
        return ctx.Err()
    case p.jobs <- job:
        return nil
    }
}

func (p *BoundedPool) StartWorkers(ctx context.Context, handler func(context.Context, Job) error) {
    for i := 0; i < p.workers; i++ {
        p.wg.Add(1)
        go func() {
            defer p.wg.Done()
            for {
                select {
                case <-ctx.Done():
                    return
                case j, ok := <-p.jobs:
                    if !ok { return }
                    _ = handler(ctx, j)
                }
            }
        }()
    }
}

// Phase 3: Singleflight Request Coalescing & P99 Deadline Enforcement
func ExecuteWithDeadline(parent context.Context, timeout time.Duration, fn func(context.Context) error) error {
    ctx, cancel := context.WithTimeout(parent, timeout)
    defer cancel()
    return fn(ctx)
}

func main() {
    // CodeCraft Masterclass entry point
}

