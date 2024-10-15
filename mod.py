import sys

import pandas as pd

cols = [
    "#chrom",
    "chromStart",
    "chromEnd",
    "name",
    "score",
    "strand",
    "thickStart",
    "thickEnd",
    "dgvID",
    "variant_type",
    "variant_sub_type",
    "num_variants",
    "num_studies",
    "num_samples",
    "Frequency",
    "num_unique_samples_tested",
    "blockCount",
]
ipath = sys.argv[1]
if not ipath:
    sys.exit("No input file provided")
opath = ipath.replace("_org", "")
dgv = pd.read_table(ipath, usecols=cols)  # type:ignore
dgv.to_csv(opath, sep="\t", index=False)
