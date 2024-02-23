import matplotlib.pyplot as plt
from load_csv import load
import pandas as pd
import numpy as np


def convert_number(value: str) -> float:
    if value.endswith("M"):
        return (float(value[:-1]) * 1e6)
    if value.endswith("K"):
        return (float(value[:-1]) * 1e3)


def convert_country_data(df: pd.DataFrame):
    single_colum = df.loc[0:, "income_1900"]
    data_country = np.array([int(convert_number(x)) for x in single_colum])
    return data_country


def main():
    name_income = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    df_income = load(name_income)
    df_life_expect = load("life_expectancy_years.csv")
    if df_income is None or df_life_expect is None:
        return
    income_1900 = df_income[["country", "1900"]]
    income_1900 = income_1900.rename(columns={'1900': "income_1900"})
    # arr_income_1900 = convert_country_data(income_1900)
    life_1900 = df_life_expect[["country", "1900"]]
    life_1900 = life_1900.rename(columns={'1900': "life_expectancy_1900"})
    merged_data = pd.merge(income_1900, life_1900, on="country", how="left")
    if merged_data.isnull().values.any():
        print("Warning: there is null value in the life expectancy data ")
        merged_data.dropna(inplace=True)
    plt.figure(figsize=(10, 6))
    for index, row in merged_data.iterrows():
        plt.scatter(row["income_1900"], row["life_expectancy_1900"])
    plt.title("1900")
    plt.xlabel("Gross Domestic Product")
    plt.ylabel("Life expectancy")
# for amplify the scale beteween 300 and 1000
    plt.xscale('log')
# ticks for x-axis
    x_ticks = [300, 1000, 10000]
    x_labels = ['300', '1K', '10K']
    plt.xticks(x_ticks, x_labels)
    plt.xlim(300, 10001)
    # plt.legend(title="country")
    plt.show()


if __name__ == "__main__":
    main()
