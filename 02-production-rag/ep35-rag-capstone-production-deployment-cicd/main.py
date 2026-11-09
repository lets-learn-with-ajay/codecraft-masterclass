# Phase 1: FastAPI Kubernetes Readiness Probe & Queue Saturation Guard
from dataclasses import dataclass

@dataclass
class WorkerTelemetry:
    inflight_requests: int
    gpu_vram_utilization: float
    p99_ttft_ms: float

def evaluate_k8s_readiness(metrics: WorkerTelemetry) -> tuple[int, dict]:
    healthy = metrics.gpu_vram_utilization < 0.92 and metrics.inflight_requests < 64
    status_code = 200 if healthy else 503
    return status_code, {'ready': healthy, 'p99_ttft_ms': metrics.p99_ttft_ms}
