import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    """
    path:path for the file to be loaded
    return: pandas dataframe created from file loaded
    """
    try:
        assert os.path.exists(path), "The file not found"
        dir_name, ext_name = os.path.splitext(path)
        assert ext_name == ".csv", "the file is not in format csv"
        df = pd.read_csv(path)
        # if df.isnull().any():
        #     raise ValueError("there is null value")
        # arr = df.value
        print("Loading dataset of dimension:", df.shape)
        return df

    except AssertionError as e:
        print(e)
        return None
