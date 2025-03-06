import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def aff_life(df: pd.DataFrame, country: str):
    if not 'country' in df.columns:
        raise ValueError("The dataframe doesnt contain country column")
    df.set_index("country", inplace=True)
    row = df.loc[country]
    plt.plot(row.index, row.values)
    plt.xticks(row.index[::40])
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.title(f'{country} Life expectancy Projections')
    plt.show()


def main():
    df = load("life_expectancy_years.csv")
    try:
        if df is None:
            raise ValueError("Dataframe is None")
        aff_life(df, "France")
    except (KeyError, ValueError) as e:
            print(f"{type(e).__name__}: Invalid key for row selections")
    return 0


if __name__ == "__main__":
    main()
