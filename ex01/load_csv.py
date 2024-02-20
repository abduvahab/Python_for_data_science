import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    """
    path:path for the file to be loaded
    return: pandas dataframe created from file loaded
    """
    try:
        assert os.path.exists(path), "file not found"
        dir_name, ext_name = os.path.splitext(path)
        assert ext_name == ".csv", "the file is not in csv format"
        df = pd.read_csv(path)
        return df
    except AssertionError as e:
        print(e)
        return None
