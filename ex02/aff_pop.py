from load_csv import load
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def convert_number(value: str) -> float:
    if value.endswith("M"):
        return (float(value[:-1]) * 1e6)
    if value.endswith("K"):
        return (float(value[:-1]) * 1e3)


def country_data(df: pd.DataFrame, country: str, condition: np.ndarray):
    arr = df.loc[df["country"] == country].values[0, 1:][condition]
    data_country = np.array([int(convert_number(x)) for x in arr])
    return data_country


def main():
    try:
        df = load("./population_total.csv")
        if df is None:
            raise ValueError()
        years = df.columns[1:].values.astype(int)
        condition = years < 2050
        data_france = country_data(df, "France", condition)
        data_belgium = country_data(df, "Belgium", condition)
        fig, ax = plt.subplots()
        ax.plot(years[condition], data_france, label="France", color="green")
        ax.plot(years[condition], data_belgium, label="Belgium", color="blue")
        ax.set_title("Population Projections")
        ax.set_xlabel("Year")
        ax.set_ylabel("Population")
        ax.legend(loc="lower right")
        x_ticks = years[condition][::40]
        ax.set_xticks(x_ticks)
        y_ticks = np.arange(20e6, 80e6, 20e6)
        ax.set_yticks(y_ticks)
        ax.set_yticklabels(f'{int(y / 1e6)}M' for y in y_ticks)
        plt.show()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
