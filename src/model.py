from sklearn.linear_model import Ridge
from joblib import dump, load
from .data import load_processed_data

MODEL_DIR = '../models'


def fit_model():
    X_train, X_val, X_test, y_train, y_val, y_test = load_processed_data()

    # Fit
    model = Ridge(alpha=0.5, random_state=0)
    model.fit(X_train, y_train)

    # Save model
    dump(model, f'{MODEL_DIR}/model.joblib')

    return model


def load_model():
    return load(f'{MODEL_DIR}/model.joblib')
