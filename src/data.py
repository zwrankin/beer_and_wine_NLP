import pandas as pd
import pickle

DATA_DIR = '../input'


def extract_descriptions():
    """Extracts and saves a list of wine descriptions from the raw data"""
    df = pd.read_csv(f'{DATA_DIR}/raw/winemag-data_first150k.csv')

    descriptions = df.description.tolist()

    with open(f'{DATA_DIR}/processed/descriptions', 'wb') as fp:
        pickle.dump(descriptions, fp)


def load_descriptions():
    """Loads saved wine descriptions to memory"""
    with open(f'{DATA_DIR}/processed/descriptions', 'rb') as fp:
        descriptions = pickle.load(fp)
    return descriptions
