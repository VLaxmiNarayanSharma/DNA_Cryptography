"""Utility helpers: bitstring conversions, file helpers, and small helpers."""
from typing import Tuple




def bytes_to_bitstring(data: bytes) -> str:
    return ''.join(f"{b:08b}" for b in data)




def bitstring_to_bytes(bits: str) -> bytes:
    if len(bits) % 8 != 0:
    # trim trailing padding zeros if any
        bits = bits[:len(bits) - (len(bits) % 8)]
    out = bytearray()
    for i in range(0, len(bits), 8):
        out.append(int(bits[i:i+8], 2))
    return bytes(out)




def text_to_bitstring(text: str) -> str:
    return bytes_to_bitstring(text.encode('utf-8'))




def bitstring_to_text(bits: str) -> str:
    b = bitstring_to_bytes(bits)
    return b.decode('utf-8', errors='replace')