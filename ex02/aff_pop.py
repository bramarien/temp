import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load

def convert_to_int(value):
    if 'B' in value:
        return int(float(value.replace('B', '')) * 1_000_000_000)
    elif 'M' in value:
        return int(float(value.replace('M', '')) * 1_000_000)
    elif 'k' in value:
        return int(float(value.replace('k', '')) * 1_000)
    else:
        return int(value)

def aff_pop(df: pd.DataFrame, country1: str, country2: str):
    df.set_index("country", inplace=True)
    row_c1 = df.loc[country1, (df.columns >= '1800') & (df.columns <= '2050')]
    row_c2 = df.loc[country2, (df.columns >= '1800') & (df.columns <= '2050')]
    c1_conv = row_c1.apply(convert_to_int)
    c2_conv = row_c2.apply(convert_to_int)
    plt.plot(row_c1.index, c1_conv.values, label=country1)
    plt.plot(row_c2.index, c2_conv.values, label=country2)
    plt.xticks(row_c1.index[::40])

    # print(row_c2.max())
    # step = int(max(row_c1.values.max(), row_c2.max()))
    # plt.yticks([step, step * 2, step * 3])
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.title('Population Projections')
    plt.legend(loc='lower right')
    plt.show()

def main():
    df = load("population_total.csv")
    try:
        if df is None:
            raise ValueError("Dataframe is None")
        aff_pop(df, "France", "China")
    except (KeyError, ValueError) as e:
            print(f"{type(e).__name__}: Invalid key for row selections")
    return 0


if __name__ == "__main__":
    main()
