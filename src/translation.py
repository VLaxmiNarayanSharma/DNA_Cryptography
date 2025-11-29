"""
Reversible codon <-> symbol translation layer for the pseudo DNA cryptosystem.

This completely replaces biological translation because biological mapping
is NOT reversible (64 codons → 20 amino acids).  
We provide a PERFECT 1-to-1 reversible mapping between:

    DNA codon (AAA, AAC, …, TTT)  <==>  Printable symbol

This guarantees encryption/decryption symmetry.
"""

from typing import Dict
import string

# ───────────────────────────────────────────────
# 1. Generate all 64 DNA codons
# ───────────────────────────────────────────────
BASES = "ACGT"

CODONS = [
    a + b + c
    for a in BASES
    for b in BASES
    for c in BASES
]

# ───────────────────────────────────────────────
# 2. Choose 64 reversible symbols:
#    Letters + digits + punctuation (exactly 64 chars)
# ───────────────────────────────────────────────
SYMBOLS = (
    string.ascii_uppercase +      # 26
    string.ascii_lowercase +      # 26 → 52
    "0123456789" +                # 10 → 62
    "+="                          # 2 → 64 symbols total
)

assert len(SYMBOLS) == 64, "Reversible symbol set must be exactly 64 chars."

# ───────────────────────────────────────────────
# 3. Build reversible lookup tables
# ───────────────────────────────────────────────
CODON_TO_SYMBOL: Dict[str, str] = dict(zip(CODONS, SYMBOLS))
SYMBOL_TO_CODON: Dict[str, str] = {v: k for k, v in CODON_TO_SYMBOL.items()}


# ───────────────────────────────────────────────
# 4. DNA → symbols  (encryption stage)
# ───────────────────────────────────────────────
def dna_to_symbols(dna_seq: str) -> str:
    """Convert DNA sequence into reversible symbol string (1 symbol per codon)."""
    out = []
    for i in range(0, len(dna_seq), 3):
        codon = dna_seq[i:i+3]
        if len(codon) < 3:
            break
        out.append(CODON_TO_SYMBOL[codon])
    return ''.join(out)


# ───────────────────────────────────────────────
# 5. Symbols → DNA (decryption stage)
# ───────────────────────────────────────────────
def symbols_to_dna(symbol_seq: str) -> str:
    """Convert reversible symbol string back into DNA codons."""
    return ''.join(SYMBOL_TO_CODON[s] for s in symbol_seq)
