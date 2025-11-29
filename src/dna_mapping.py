"""Mapping between bits and DNA bases (A, C, G, T)."""
from typing import Dict


BASE_TO_BITS: Dict[str, str] = {
'A': '00',
'C': '01',
'G': '10',
'T': '11',
}


BITS_TO_BASE = {v: k for k, v in BASE_TO_BITS.items()}




def bitstring_to_dna(bits: str) -> str:
# pad to multiple of 2
    if len(bits) % 2 != 0:
        bits += '0'
    dna = []
    for i in range(0, len(bits), 2):
        dna.append(BITS_TO_BASE[bits[i:i+2]])
    return ''.join(dna)




def dna_to_bitstring(dna: str) -> str:
    return ''.join(BASE_TO_BITS[b] for b in dna)