# summarize_contigs

These Python programs characterize sequences in a fasta file, including telomere information.  


ACKNOWLEDGEMENT

This code was written by [David Winter](https://github.com/dwinter). It is posted here to allow for automated git cloning.


INSTALLATION

*summarize_contigs* requires the *biopython* package. This can be installed with

```
pip install biopython
```

CODE VARIANTS

*summarize_contigs* looks for the typical fungal telomere sequence *TAACCC*.  *summarize_contigs_phytophthora* looks for the typical *Phytophthora* telomere sequence *TAAACCC*.


USAGE

Program usage is as follows:

```
summarize_contigs.py FASTA_input_file > summary_file.tsv
summarize_contigs_phytophthora.py FASTA_input_file > summary_file.tsv
```


EXAMPLE

```
summarize_contigs.py fungal_assembly.fna > assembly_summary.tsv
summarize_contigs_phytophthora.py phytophthora_assembly.fna > assembly_summary.tsv
```
