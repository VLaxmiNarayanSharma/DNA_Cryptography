from .translation import symbols_to_dna
from .intron_handler import restore_introns
from .utils import bitstring_to_text
from .dna_mapping import dna_to_bitstring
from typing import Dict


def decrypt(cipher_symbols: str, key: Dict) -> str:
    """
    Reverse of encrypt():
        1. symbols → DNA exons
        2. restore introns
        3. DNA → bits
        4. bits → text
    """

    # 1. SYMBOLS → EXON DNA
    exons = symbols_to_dna(cipher_symbols)

    # 2. RESTORE INTRONS
    full_dna = restore_introns(exons, key["introns"], key["start_sig"], key["end_sig"])

    # 3. DNA → BITSTRING
    bits = dna_to_bitstring(full_dna)

    # 4. BITSTRING → TEXT  (truncate to original length)
    bits = bits[: key["dna_length"] * 2]   # 1 base = 2 bits
    return bitstring_to_text(bits)
