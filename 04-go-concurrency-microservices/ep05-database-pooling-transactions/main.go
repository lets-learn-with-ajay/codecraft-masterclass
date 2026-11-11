// Phase 1: Fan-Out / Fan-In Channel Pipelines
package main

func FanOut(ctx context.Context, in <-chan Job, numWorkers int) []<-chan Result {
    outputs := make([]<-chan Result, numWorkers)
    for i := 0; i < numWorkers; i++ {
        outputs[i] = worker(ctx, in)
    }
    return outputs
}

// Phase 2: Multiplexing Streams with Fan-In
func FanIn(ctx context.Context, channels ...<-chan Result) <-chan Result {
    var wg sync.WaitGroup
    multiplexed := make(chan Result)
    for _, ch := range channels {
        wg.Add(1)
        go func(c <-chan Result) {
            defer wg.Done()
            for val := range c { multiplexed <- val }
        }(ch)
    }
    go func() { wg.Wait(); close(multiplexed) }()
    return multiplexed
}

// Phase 2: Multiplexing Streams with Fan-In
func FanIn(ctx context.Context, channels ...<-chan Result) <-chan Result {
    var wg sync.WaitGroup
    multiplexed := make(chan Result)
    for _, ch := range channels {
        wg.Add(1)
        go func(c <-chan Result) {
            defer wg.Done()
            for val := range c { multiplexed <- val }
        }(ch)
    }
    go func() { wg.Wait(); close(multiplexed) }()
    return multiplexed
}

// Phase 1: Fan-Out / Fan-In Channel Pipelines
package main

func FanOut(ctx context.Context, in <-chan Job, numWorkers int) []<-chan Result {
    outputs := make([]<-chan Result, numWorkers)
    for i := 0; i < numWorkers; i++ {
        outputs[i] = worker(ctx, in)
    }
    return outputs
}

// Phase 2: Multiplexing Streams with Fan-In
func FanIn(ctx context.Context, channels ...<-chan Result) <-chan Result {
    var wg sync.WaitGroup
    multiplexed := make(chan Result)
    for _, ch := range channels {
        wg.Add(1)
        go func(c <-chan Result) {
            defer wg.Done()
            for val := range c { multiplexed <- val }
        }(ch)
    }
    go func() { wg.Wait(); close(multiplexed) }()
    return multiplexed
}

// Phase 2: Multiplexing Streams with Fan-In
func FanIn(ctx context.Context, channels ...<-chan Result) <-chan Result {
    var wg sync.WaitGroup
    multiplexed := make(chan Result)
    for _, ch := range channels {
        wg.Add(1)
        go func(c <-chan Result) {
            defer wg.Done()
            for val := range c { multiplexed <- val }
        }(ch)
    }
    go func() { wg.Wait(); close(multiplexed) }()
    return multiplexed
}

// Phase 1: Fan-Out / Fan-In Channel Pipelines
package main

func FanOut(ctx context.Context, in <-chan Job, numWorkers int) []<-chan Result {
    outputs := make([]<-chan Result, numWorkers)
    for i := 0; i < numWorkers; i++ {
        outputs[i] = worker(ctx, in)
    }
    return outputs
}

func main() {
    // CodeCraft Masterclass entry point
}

