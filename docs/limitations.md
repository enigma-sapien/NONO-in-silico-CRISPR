# Limitations

## Computational-only scope

This project contains computational guide-design outputs, analysis code,
documentation, and an experimental validation plan.

It does not include:

- Cell culture or transfection
- Genome editing
- PCR or sequencing experiments
- Editing-efficiency measurements
- Protein or RNA measurements
- Phenotypic validation

## Target annotation

The selected genomic interval has not yet been formally verified as a
relevant coding exon of the intended NONO transcript.

A match to the reference genome does not establish that a guide targets
coding sequence or will produce a loss-of-function allele.

## Score verification

The initial working table was assembled from screenshots without
visible column headers.

Score identities and scales must be checked against the original
CRISPOR export before interpretation.

## Off-target review

Screenshot excerpts are incomplete.

The absence of a visible exonic annotation does not establish the
absence of exonic predicted off-targets.

## Ranking limitations

The composite score is a custom, unvalidated comparison formula.

Its weights are arbitrary and it must not be interpreted as:

- Editing efficiency
- Probability of knockout
- Experimental specificity
- Safety
- Evidence of biological effect

It also does not explicitly incorporate all tool warnings or site-level
off-target information.

## Sequence-data quality

Spacer sequences, GC percentages, PAMs, and genomic positions require
independent verification against the original tool output.

## Current project status

The repository demonstrates a working computational analysis framework.

The guide shortlist and ranking remain preliminary pending annotation
and data-quality checks.