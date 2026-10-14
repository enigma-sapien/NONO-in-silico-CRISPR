# Raw inputs and source records

This folder stores the sequence and source data used in the analysis.

## Files

- NONO_target_region_hg38.fasta:
  Genomic sequence retrieved from UCSC.

- candidate_guides.csv:
  Working candidate table used by the Python ranking script.
  This is a manually transcribed analysis input, not an untouched
  CRISPOR export.

## Source records to retain

Save the following when available:

- Original UCSC FASTA header
- Genome assembly and interval
- Retrieval date
- Original CRISPOR export with column headers
- Complete predicted off-target outputs
- CRISPOR result URL or job identifier

Do not overwrite original tool exports. Keep them separate from manually
cleaned or reformatted tables.

Do not include confidential or patient-identifiable information.