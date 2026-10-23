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

