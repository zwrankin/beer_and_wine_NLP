import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from joblib import dump, load
from .nlp import preprocess_reviews

DATA_DIR = '../input'
MODEL_DIR = '../models'


def process_data(data_dir=DATA_DIR, target='points'):
    """Takes raw data and transforrms into train, validation, and testing arrays"""
    # Load data
    df = pd.read_csv(f'{data_dir}/raw/winemag-data_first150k.csv')

    # Clean descriptions using NLP
    descriptions = preprocess_reviews(df.description)

    # Split into train,  test (no validation yet)
    desc_train, desc_val, desc_test, y_train, y_val, y_test = split_train_val_test(descriptions, df[target])

    # Feature engineering
    cv = CountVectorizer(binary=True, stop_words='english')
    cv.fit(desc_train)
    dump(cv, f'{MODEL_DIR}/cv.joblib')

    X_train = cv.transform(desc_train)
    X_val = cv.transform(desc_val)
    X_test = cv.transform(desc_test)

    # Save to processed data directory
    with open(f'../input/processed/X_train', 'wb') as fp:
        pickle.dump(X_train, fp)
    with open(f'../input/processed/X_val', 'wb') as fp:
        pickle.dump(X_val, fp)
    with open(f'../input/processed/X_test', 'wb') as fp:
        pickle.dump(X_test, fp)
    with open(f'../input/processed/y_train', 'wb') as fp:
        pickle.dump(y_train, fp)
    with open(f'../input/processed/y_val', 'wb') as fp:
        pickle.dump(y_val, fp)
    with open(f'../input/processed/y_test', 'wb') as fp:
        pickle.dump(y_test, fp)

    # return X_train, X_val, X_test, y_train, y_val, y_test


def load_count_vectorizer(model_dir=MODEL_DIR):
    """Loads trained count vectorizer"""
    return load(f'{MODEL_DIR}/cv.joblib')


def load_processed_data(data_dir=DATA_DIR):
    with open(f'{data_dir}/processed/X_train', 'rb') as fp:
        X_train = pickle.load(fp)
    with open(f'{data_dir}/processed/X_val', 'rb') as fp:
        X_val = pickle.load(fp)
    with open(f'{data_dir}/processed/X_test', 'rb') as fp:
        X_test = pickle.load(fp)
    with open(f'{data_dir}/processed/y_train', 'rb') as fp:
        y_train = pickle.load(fp)
    with open(f'{data_dir}/processed/y_val', 'rb') as fp:
        y_val = pickle.load(fp)
    with open(f'{data_dir}/processed/y_test', 'rb') as fp:
        y_test = pickle.load(fp)

    return X_train, X_val, X_test, y_train, y_val, y_test


def split_train_val_test(X, y):
    """3-way split of X and y by applying sklearn's train_test_split twice """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=1)

    return X_train, X_val, X_test, y_train, y_val, y_test


def extract_descriptions(data_dir=DATA_DIR):
    """Extracts and saves a pd.DataFrame of wine descriptions and points from the raw data"""
    df = pd.read_csv(f'{data_dir}/raw/winemag-data_first150k.csv')
    descriptions = df[['description', 'points']]
    descriptions.to_hdf(f'{data_dir}/processed/descriptions.hdf', key='descriptions')


def load_descriptions(data_dir=DATA_DIR, include_points=False):
    """Loads saved wine descriptions to memory, either as a pd.DataFrame with points or just a list of descriptions"""
    descriptions = pd.read_hdf(f'{data_dir}/processed/descriptions.hdf')
    if include_points:
        return descriptions
    else:
        return descriptions.description.tolist()
