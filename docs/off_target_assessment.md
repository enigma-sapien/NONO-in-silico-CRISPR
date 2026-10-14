# Predicted off-target assessment

## Purpose

Document predicted off-target information for candidate sgRNAs and
identify candidates requiring further review.

## Current evidence

The initial review used CRISPOR screenshots.

These screenshots show only selected off-target annotations. They do not
provide a complete assessment of every predicted site.

The absence of an exonic annotation in a screenshot must not be interpreted
as the absence of exonic off-targets in the complete result.

## Features to review

For each candidate, record:

- Number of mismatches
- Predicted off-target sequence and PAM
- Chromosome and genomic coordinates
- Gene or intergenic annotation
- Exonic, intronic, or other genomic context
- Site-level predicted cutting score, when available
- Whether the site deserves experimental follow-up

## Interpretation principles

Total predicted off-target count is not sufficient for guide selection.

A candidate with many weakly similar predicted sites may differ in risk
from a candidate with fewer but closely matched sites.

Mismatch number, sequence context, site-level scores, and genomic
annotation should be considered together.

Tool warnings should also be interpreted in relation to the intended
guide-delivery or expression strategy.

## Correction to the preliminary review

NONO_g04 corresponds to CRISPOR candidate 180/rev.

Its screenshot includes a predicted off-target annotated as:

3:exon:GPATCH8

It must therefore not be described as having no visible exonic
off-target annotation.

## Current conclusion

The five guides are preliminary candidates.

No candidate has been demonstrated to be free of off-target activity.

A final preferred guide should not be designated until:

- The on-target coding region is confirmed
- Score-column identities are verified
- Complete predicted off-target lists are reviewed

## Experimental status

No off-target editing was measured experimentally.