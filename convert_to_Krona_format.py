#!/usr/bin/env python3

import pandas as pd

def arguments():

    parser = argparse.ArgumentParser()

    parser.add_argument('surpi-output', help='Count table file that is the output of SURPI analysis. Tab-delimited file')

    return parser.parse_args()

def melt_counttable(surpi_output):

    counttable = pd.read_table(surpi_output)
    counttable = pd.melt(counttable, id_vars = ['Species', 'Genus', 'Family'], var_name='Sample', value_name='Counts')

#cols = cols[-1] + cols [:-3]
#surpi_sorted = surpi_sorted[cols]

surpi_krona_group = counttable.groupby('Sample')

# Variable with the desired order of columns to export for
# Krona visualizations
header = ['Counts','Family','Genus','Species']

for name, group in surpi_krona_group:
        group.to_csv(str(name + ".txt"), columns=header, header=False, index=False)

