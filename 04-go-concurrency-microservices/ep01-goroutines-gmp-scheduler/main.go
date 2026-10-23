package main

// Phase 2: Non-Blocking Dispatch & GMP Scheduling
func (p *WorkerPool) Start(ctx context.Context) {
    for i := 0; i < p.workers; i++ {
        p.wg.Add(1)
        go func(workerID int) {
            defer p.wg.Done()
            for {
                select {
                case <-ctx.Done():
                    return
                case task, ok := <-p.tasks:
                    if !ok { return }
                    task.Execute(workerID)
                }
            }
        }(i)
    }
}

func main() {
    // CodeCraft Masterclass entry point
}

