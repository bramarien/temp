import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load

def convert_to_string(value):
    if value >= 1_000_000_000:
        return f"{int(value / 1_000_000_000)}B"
    elif value >= 1_000_000:
        return f"{int(value / 1_000_000)}M"
    elif value >= 1_000:
        return f"{int(value / 1_000)}k"
    else:
        return f"{int(value)}"

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
    plt.plot(row_c1.index, c1_conv.values, label=country1, color="green")
    plt.plot(row_c2.index, c2_conv.values, label=country2, color="blue")
    plt.xticks(row_c1.index[::40])
    min_v = min(c1_conv.min(), c2_conv.min())
    max_v = max(c1_conv.max(), c2_conv.max())
    tick_25 = min_v + 0.3 * (max_v - min_v)
    tick_50 = min_v + 0.6 * (max_v - min_v)
    tick_75 = min_v + 0.9 * (max_v - min_v)
    ticks = [tick_25, tick_50, tick_75]
    ticks_label = [convert_to_string(tick) for tick in ticks]
    plt.yticks(ticks, ticks_label)
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
        aff_pop(df, "France", "Belgium")
    except (KeyError, ValueError) as e:
            print(f"{type(e).__name__}: Invalid key for row selections")
    return 0


if __name__ == "__main__":
    main()
