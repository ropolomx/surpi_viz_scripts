#!/usr/bin/env python3

import pandas as pd

def arguments():

    parser = argparse.ArgumentParser()

    parser.add_argument('surpi-output', help='Count table file that is the output of SURPI analysis. Tab-delimited file')

    return parser.parse_args()

def melt_counttable(surpi_output):

    """Read table with SURPI output and return table in tidy format
    """

    counttable = pd.read_table(surpi_output)
    counttable = pd.melt(counttable, id_vars = ['Species', 'Genus', 'Family'], var_name='Sample', value_name='Counts')

    return counttable

#cols = cols[-1] + cols [:-3]
#surpi_sorted = surpi_sorted[cols]

def group_by_Sample():
    surpi_krona_group = counttable.groupby('Sample')

def save_to_file():
    
    # Variable with the desired order of columns to export for
    # Krona visualizations
header = ['Counts','Family','Genus','Species']

for name, group in surpi_krona_group:
        group.to_csv(str(name + ".txt"), sep='\t', columns=header, header=False, index=False)

