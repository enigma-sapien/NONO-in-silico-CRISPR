# CRISPR guide-design workflow

## Objective

Generate and review candidate SpCas9 sgRNAs for a genomic region
selected during a NONO-focused computational project.

## Reference assembly

- Species: Homo sapiens
- Genome assembly selected: GRCh38 / hg38
- Sequence source: UCSC Genome Browser

## Sequence retrieval

The UCSC Get DNA page displayed the following core interval:

chrX:71,283,639-71,283,727

The retrieval settings included:

- 200 bases upstream
- 200 bases downstream
- Upper-case sequence
- Repeat masking disabled
- Reverse complement disabled

The resulting genomic DNA sequence was saved as:

data/raw/NONO_target_region_hg38.fasta

The exact sequence length, assembly, and returned coordinates should be
confirmed from the original UCSC FASTA header.

## Initial input issue

An initial query used a NONO mRNA sequence.

CRISPOR reported that the full query was not found as a continuous
sequence in the selected genome.

The workflow was revised to use a genomic DNA region retrieved from UCSC.

## CRISPOR settings

- Genome: Homo sapiens hg38
- Nuclease: SpCas9
- PAM: NGG
- Input: UCSC-derived genomic DNA sequence

## Candidate review

Candidate rows were inspected for:

- Guide sequence and PAM
- Strand
- Tool warnings
- Predicted activity scores
- Predicted specificity scores
- Predicted off-target sites and genomic annotations

Five candidates were transferred into a working CSV for analysis.

## Python analysis

Input:

data/raw/candidate_guides.csv

Script:

scripts/rank_guides.py

Output:

results/guide_ranking.csv

A separate plotting script generates:

figures/guide_ranking.png

## Checks still required

Before final biological interpretation:

1. Confirm the genomic interval belongs to the intended NONO locus.
2. Confirm the selected transcript and coding-exon identity.
3. Confirm which candidate spacers and cleavage sites fall within coding sequence.
4. Export the original CRISPOR table with its column headers.
5. Verify the identities and scales of all numerical score columns.
6. Recalculate GC percentages directly from the spacer sequences.
7. Review complete off-target lists rather than screenshot excerpts.
8. Record the retrieval/design date and source links.