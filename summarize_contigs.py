#!/usr/bin/env python

import sys
from Bio import SeqIO
from Bio import SeqUtils

def count_telo(seq):
    return( seq.count('CCTAAC') )



if __name__ == "__main__":
    try:
        infile = sys.argv[1]
    except:
        print("Usage: summarize_contigs.py [assembly.fna] > assembly_summary.tsv")
        sys.exit(1)
    line_template = '{}\t{}\t{}\t{}\t{}\n'
    lens = []
    for rec in SeqIO.parse(infile, "fasta"):
        L = len(rec)
        lens.append(L)
        info = (rec.id,                                       # contig name
                L       ,                                     # contig len
                SeqUtils.GC(rec.seq),                         # mean GC
                count_telo(rec.seq[:40]),                     # n. telomeres left
                count_telo(rec.seq[-40:].reverse_complement()) # n. telomeres right
        )
        sys.stdout.write(line_template.format(*info))
    total = large = n = 0
    for L in lens:
        if L > 1e6:
            large += L
        total += L
        n += 1
    out_template = "Wrote data for {} contigs, {}Mb of {}Mb in contigs > 1Mb\n"
    sys.stderr.write(out_template.format(n,round(large/1e6,2),round(total/1e6,2)))
    sys.exit(0)
            
    
        



