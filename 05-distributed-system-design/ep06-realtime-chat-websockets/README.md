# Episode 06: Real-Time Chat & Notification Scaling: WebSockets + Redis Pub/Sub

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtu.be/PLACEHOLDER)
[![Track: Distributed System Design](https://img.shields.io/badge/Track-05_Distributed_Systems-fb923c?style=for-the-badge)](../README.md)

## 📌 Summary
Scaling persistent bidirectional connections across thousands of servers with connection managers and pub/sub backplanes.

## 🎯 Key Takeaways
- Stateful WebSocket connections require a centralized messaging backplane to route messages across horizontal server nodes.
- Redis Pub/Sub or Kafka channels route outbound events to the exact gateway cluster node holding the user's active socket.
- Heartbeats, exponential reconnection backoffs, and jitter prevent thundering herd reconnection avalanches during network hiccups.

## 🔍 Topics Covered
- `scalable websocket architecture redis pubsub`
- `realtime notification system design`

## 🚀 How to Run

```bash
python simulation.py
```
