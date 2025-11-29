"""
Handles intron removal (splicing) and restoration for reversible DNA encryption.
"""

from typing import List, Tuple


def remove_introns(dna: str, start_sig: str, end_sig: str) -> Tuple[str, List[Tuple[int, int, str]]]:
    """
    Removes introns from DNA based on start_sig and end_sig.

    Returns:
        exons_only (str)
        intron_list: list of (start_index, end_index, intron_string)
    """

    exons = []
    introns = []
    i = 0
    n = len(dna)

    while i < n:
        if dna.startswith(start_sig, i):
            j = dna.find(end_sig, i + len(start_sig))
            if j == -1:
                exons.append(dna[i:])
                break

            intron_text = dna[i: j + len(end_sig)]
            introns.append((i, j + len(end_sig), intron_text))
            i = j + len(end_sig)

        else:
            exons.append(dna[i])
            i += 1

    return ''.join(exons), introns



def restore_introns(exons: str, introns: List[Tuple[int, int, str]], start_sig: str, end_sig: str) -> str:
    """
    Rebuilds the full DNA by re-inserting intron sequences at correct positions.

    introns: list of (start, end, intron_string)
    """

    dna = []
    exon_pos = 0
    intron_index = 0

    # Sort introns by their original location
    introns_sorted = sorted(introns, key=lambda x: x[0])

    current_pos = 0

    for start, end, intron_text in introns_sorted:

        # Add exon characters until intron's start
        while current_pos < start and exon_pos < len(exons):
            dna.append(exons[exon_pos])
            exon_pos += 1
            current_pos += 1

        # Insert intron
        dna.append(intron_text)
        current_pos += (end - start)

    # Add leftover exon characters
    dna.append(exons[exon_pos:])

    return ''.join(dna)
