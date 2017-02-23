#!/usr/bin/env python3

import pandas as pd

def arguments():

    parser = argparse.ArgumentParser()

    parser.add_argument('surpi-output',

    return parser.parse_args()

def melt_counttable(surpi_output):

    counttable = pd.read_table(surpi_output)

    counttable = pd.melt(counttable, id_vars = ['Species', 'Genus', 'Species'], var_name='Barcode', value_name='Counts')

