import pandas as pd
import pickle

DATA_DIR = '../input'


def extract_descriptions(data_dir=DATA_DIR):
    """Extracts and saves a list of wine descriptions from the raw data"""
    df = pd.read_csv(f'{data_dir}/raw/winemag-data_first150k.csv')

    descriptions = df.description.tolist()

    with open(f'{data_dir}/processed/descriptions', 'wb') as fp:
        pickle.dump(descriptions, fp)


def load_descriptions(data_dir=DATA_DIR):
    """Loads saved wine descriptions to memory"""
    with open(f'{data_dir}/processed/descriptions', 'rb') as fp:
        descriptions = pickle.load(fp)
    return descriptions
