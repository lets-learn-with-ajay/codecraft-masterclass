package main

// Phase 1: CRC32-Framed Binary Write-Ahead Log (WAL) Engine
package storage

import (
    "encoding/binary"
    "hash/crc32"
    "os"
    "sync"
)

type WriteAheadLog struct {
    mu   sync.Mutex
    file *os.File
    lsn  uint64
}

func (w *WriteAheadLog) AppendRecord(key, val []byte) (uint64, error) {
    w.mu.Lock()
    defer w.mu.Unlock()
    w.lsn++
    buf := make([]byte, 20+len(key)+len(val))
    binary.LittleEndian.PutUint64(buf[4:12], w.lsn)
    binary.LittleEndian.PutUint32(buf[12:16], uint32(len(key)))
    binary.LittleEndian.PutUint32(buf[16:20], uint32(len(val)))
    copy(buf[20:], key)
    copy(buf[20+len(key):], val)
    binary.LittleEndian.PutUint32(buf[0:4], crc32.ChecksumIEEE(buf[4:]))
    if _, err := w.file.Write(buf); err != nil {
        return 0, err
    }
    return w.lsn, w.file.Sync()
}

// Phase 2: Concurrent In-Memory MemTable with Flush Watermark
package storage

import "sync"

type MemTableEntry struct {
    Value     []byte
    LSN       uint64
    Tombstone bool
}

type ShardedMemTable struct {
    mu        sync.RWMutex
    entries   map[string]MemTableEntry
    sizeBytes int64
    maxBytes  int64
}

func (m *ShardedMemTable) Put(key string, val []byte, lsn uint64) bool {
    m.mu.Lock()
    defer m.mu.Unlock()
    m.entries[key] = MemTableEntry{Value: val, LSN: lsn}
    m.sizeBytes += int64(len(key) + len(val))
    return m.sizeBytes >= m.maxBytes
}

// Phase 3: Deterministic Crash Recovery & WAL Checksum Verification
package storage

import (
    "encoding/binary"
    "errors"
    "hash/crc32"
)

func VerifyWALFrame(frame []byte) (uint64, error) {
    if len(frame) < 20 {
        return 0, errors.New("corrupted WAL frame: truncated header")
    }
    expectedCRC := binary.LittleEndian.Uint32(frame[0:4])
    actualCRC := crc32.ChecksumIEEE(frame[4:])
    if expectedCRC != actualCRC {
        return 0, errors.New("corrupted WAL frame: CRC32 mismatch")
    }
    return binary.LittleEndian.Uint64(frame[4:12]), nil
}

func main() {
    // CodeCraft Masterclass entry point
}

