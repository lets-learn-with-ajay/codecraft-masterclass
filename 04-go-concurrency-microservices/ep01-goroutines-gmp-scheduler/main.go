// Phase 1: Concurrency Invariants & Worker Synchronization
package main

import (
    "context"
    "sync"
    "time"
)

type WorkerPool struct {
    tasks   chan Task
    wg      sync.WaitGroup
    workers int
}

func NewWorkerPool(workers int, queueCap int) *WorkerPool {
    return &WorkerPool{tasks: make(chan Task, queueCap), workers: workers}
}

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

// Phase 1: Concurrency Invariants & Worker Synchronization
package main

import (
    "context"
    "sync"
    "time"
)

type WorkerPool struct {
    tasks   chan Task
    wg      sync.WaitGroup
    workers int
}

func NewWorkerPool(workers int, queueCap int) *WorkerPool {
    return &WorkerPool{tasks: make(chan Task, queueCap), workers: workers}
}

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

// Phase 1: Concurrency Invariants & Worker Synchronization
package main

import (
    "context"
    "sync"
    "time"
)

type WorkerPool struct {
    tasks   chan Task
    wg      sync.WaitGroup
    workers int
}

func NewWorkerPool(workers int, queueCap int) *WorkerPool {
    return &WorkerPool{tasks: make(chan Task, queueCap), workers: workers}
}

func main() {
    // CodeCraft Masterclass entry point
}

