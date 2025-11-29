from .utils import text_to_bitstring
from .dna_mapping import bitstring_to_dna
from .intron_handler import remove_introns
from .translation import dna_to_symbols  # updated reversible mapping
from typing import Tuple, Dict


def encrypt(text: str, start_sig: str = 'ATG', end_sig: str = 'TAG') -> Tuple[str, Dict]:
    """
    Encrypt plaintext by:
        1. text -> bits
        2. bits -> DNA
        3. remove introns
        4. pad exons to multiple of 3 and translate exons DNA into reversible codon symbols
    """

    # 1. TEXT → BITS
    bits = text_to_bitstring(text)

    # 2. BITS → DNA
    dna = bitstring_to_dna(bits)

    # 3. DNA → EXONS (remove introns)
    exons, intron_list = remove_introns(dna, start_sig, end_sig)

    # --- NEW: pad exons to multiple of 3 to avoid losing trailing bases in codon mapping
    pad = (-len(exons)) % 3  # 0, 1, or 2
    exons_padded = exons + ('A' * pad) if pad else exons

    # 4. EXONS (padded) DNA → REVERSIBLE CODON SYMBOL STRING
    cipher_symbols = dna_to_symbols(exons_padded)

    key = {
        "start_sig": start_sig,
        "end_sig": end_sig,
        "introns": intron_list,
        "dna_length": len(dna),     # needed to reconstruct padded bits later
        "pad": pad,                 # how many padding bases were added to exons
    }

    return cipher_symbols, key
