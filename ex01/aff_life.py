from load_csv import load
import matplotlib.pyplot as plt


def main():
    try:
        df = load("./life_expectancy_years.csv")
        if df is None:
            raise ValueError()
        years = df.columns[1:].values
        france_data = df.loc[df["country"] == "France"].values
        # benin_data = df.loc[df["country"] == "Benin"].values
        fig, ax = plt.subplots()
        ax.plot(years, france_data[0, 1:], label="France")
        # ax.plot(years, benin_data[0,1:], label="Benin")
        ticks = years[::40]
        ax.set_title("France Life expectancy Projections")
        ax.set_xlabel("Year")
        ax.set_ylabel("Life Expectancy")
        ax.set_xticks(ticks)
        ax.legend()
        # ax.grid(True)
        plt.show()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
