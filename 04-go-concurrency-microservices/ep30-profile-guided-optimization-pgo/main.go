// Phase 1: gRPC Service Server & Interceptors
package main

import (
    "google.golang.org/grpc"
    "google.golang.org/grpc/codes"
    "google.golang.org/grpc/status"
)

type OrderServer struct { pb.UnimplementedOrderServiceServer }

func (s *OrderServer) CreateOrder(ctx context.Context, req *pb.OrderRequest) (*pb.OrderResponse, error) {
    if req.GetAmount() <= 0 { return nil, status.Error(codes.InvalidArgument, "amount must be positive") }
    return &pb.OrderResponse{OrderId: "ord_9842", Status: "CONFIRMED"}, nil
}

// Phase 2: Context Deadlines & Singleflight Caching
import "golang.org/x/sync/singleflight"

var sfGroup singleflight.Group

func FetchUserDataWithDeduplication(ctx context.Context, userID string) (*UserData, error) {
    result, err, _ := sfGroup.Do(userID, func() (interface{}, error) {
        childCtx, cancel := context.WithTimeout(ctx, 350*time.Millisecond)
        defer cancel()
        return queryDatabase(childCtx, userID)
    })
    return result.(*UserData), err
}

// Phase 2: Context Deadlines & Singleflight Caching
import "golang.org/x/sync/singleflight"

var sfGroup singleflight.Group

func FetchUserDataWithDeduplication(ctx context.Context, userID string) (*UserData, error) {
    result, err, _ := sfGroup.Do(userID, func() (interface{}, error) {
        childCtx, cancel := context.WithTimeout(ctx, 350*time.Millisecond)
        defer cancel()
        return queryDatabase(childCtx, userID)
    })
    return result.(*UserData), err
}

// Phase 1: gRPC Service Server & Interceptors
package main

import (
    "google.golang.org/grpc"
    "google.golang.org/grpc/codes"
    "google.golang.org/grpc/status"
)

type OrderServer struct { pb.UnimplementedOrderServiceServer }

func (s *OrderServer) CreateOrder(ctx context.Context, req *pb.OrderRequest) (*pb.OrderResponse, error) {
    if req.GetAmount() <= 0 { return nil, status.Error(codes.InvalidArgument, "amount must be positive") }
    return &pb.OrderResponse{OrderId: "ord_9842", Status: "CONFIRMED"}, nil
}

// Phase 2: Context Deadlines & Singleflight Caching
import "golang.org/x/sync/singleflight"

var sfGroup singleflight.Group

func FetchUserDataWithDeduplication(ctx context.Context, userID string) (*UserData, error) {
    result, err, _ := sfGroup.Do(userID, func() (interface{}, error) {
        childCtx, cancel := context.WithTimeout(ctx, 350*time.Millisecond)
        defer cancel()
        return queryDatabase(childCtx, userID)
    })
    return result.(*UserData), err
}

// Phase 2: Context Deadlines & Singleflight Caching
import "golang.org/x/sync/singleflight"

var sfGroup singleflight.Group

func FetchUserDataWithDeduplication(ctx context.Context, userID string) (*UserData, error) {
    result, err, _ := sfGroup.Do(userID, func() (interface{}, error) {
        childCtx, cancel := context.WithTimeout(ctx, 350*time.Millisecond)
        defer cancel()
        return queryDatabase(childCtx, userID)
    })
    return result.(*UserData), err
}

// Phase 1: gRPC Service Server & Interceptors
package main

import (
    "google.golang.org/grpc"
    "google.golang.org/grpc/codes"
    "google.golang.org/grpc/status"
)

type OrderServer struct { pb.UnimplementedOrderServiceServer }

func (s *OrderServer) CreateOrder(ctx context.Context, req *pb.OrderRequest) (*pb.OrderResponse, error) {
    if req.GetAmount() <= 0 { return nil, status.Error(codes.InvalidArgument, "amount must be positive") }
    return &pb.OrderResponse{OrderId: "ord_9842", Status: "CONFIRMED"}, nil
}

func main() {
    // CodeCraft Masterclass entry point
}

