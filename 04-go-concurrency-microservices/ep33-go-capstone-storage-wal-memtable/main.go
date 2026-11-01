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

func main() {
    // CodeCraft Masterclass entry point
}

