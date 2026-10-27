package main

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

func main() {
    // CodeCraft Masterclass entry point
}

