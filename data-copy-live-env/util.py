import pandas as pd


def get_tables(path):
    tables_to_be_loaded = pd.read_csv(path, sep=':')
    return tables_to_be_loaded.query("to_be_loaded='yes'")