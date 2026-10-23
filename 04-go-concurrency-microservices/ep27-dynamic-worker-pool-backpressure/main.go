package main

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

func main() {
    // CodeCraft Masterclass entry point
}

