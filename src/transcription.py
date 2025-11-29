"""DNA <-> mRNA transcription utilities."""

DNA_TO_MRNA = {
'A': 'U',
'T': 'A',
'G': 'C',
'C': 'G'
}


MRNA_TO_DNA = {v: k for k, v in DNA_TO_MRNA.items()}




def dna_to_mrna(dna: str) -> str:
    return ''.join(DNA_TO_MRNA[b] for b in dna)

def mrna_to_dna(mrna: str) -> str:
    return ''.join(MRNA_TO_DNA[b] for b in mrna)