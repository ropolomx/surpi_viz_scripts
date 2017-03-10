#!/usr/bin/env python3

import pandas as pd
import os
import argparse

def arguments():

    parser = argparse.ArgumentParser()
    parser.add_argument('--tax-level', default='species', help='Taxonomical level of SURPI results')
    parser.add_argument('surpi', help='Count table file that is the output of SURPI analysis. Tab-delimited file')

    return parser.parse_args()

def counttables(counttable):

    return os.path.splitext(os.path.basename(counttable))[0]


def melt_counttable(surpi_output):

    """Read table with SURPI output and return table in tidy format
    """

    counttable = pd.read_table(surpi_output)

    counttable = counttable.rename(columns={'Family(@=contigbarcode)': 'Family'})

    counttable = pd.melt(counttable, id_vars = ['Species', 'Genus', 'Family'], var_name='Sample', value_name='Counts')

    return counttable

def group_by_Sample(melted):

    surpi_krona_group = melted.groupby('Sample')

    return surpi_krona_group

def save_to_file(melted):

    """ Save table to tab-delimite file. Header variable a list with the desired order of columns to export Krona visualizations
    """
    header = ['Counts','Family','Genus','Species']

    for name, group in group_by_Sample(melted):
        group.to_csv(str(name+".txt"), sep='\t', columns=header, header=False, index=False)

def main():

    args = arguments()

    melting = melt_counttable(args.surpi)

    grouping = group_by_Sample(melting)

    save_to_file(melting)

if __name__ == '__main__':
    main()
