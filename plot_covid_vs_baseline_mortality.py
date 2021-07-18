#!/usr/bin/env python

import japanize_matplotlib  # NOQA
import matplotlib.pyplot as plt

import _utils


def main():
    df_covid = _utils.get_covid_data()
    df_vaccine = _utils.get_vaccine_data()
    df_baseline5 = _utils.get_baseline_data(n_date=5)
    df_baseline17 = _utils.get_baseline_data(n_date=17)
    df_baseline365 = _utils.get_baseline_data(n_date=365)

    print(df_covid)
    print(df_vaccine)
    print(df_baseline5)
    print(df_baseline17)

    df_covid = df_covid.reset_index()
    df_covid["age"] = [5, 15, 25, 35, 45, 55, 65, 75, 90]
    df_covid = df_covid.set_index("age")

    df_vaccine = df_vaccine.reset_index()
    df_vaccine["age"] = [(20 + 64) / 2, (65 + 100) / 2]
    df_vaccine = df_vaccine.set_index("age")

    df_baseline5 = df_baseline5.reset_index()
    df_baseline5["age"] = [
        25,
        35,
        45,
        55,
        (60 + 64) / 2,
        (65 + 69) / 2,
        75,
        85,
        95,
        (100 + 104) / 2,
    ]
    df_baseline5 = df_baseline5.set_index("age")

    df_baseline365 = df_baseline365.reset_index()
    df_baseline365["age"] = [
        25,
        35,
        45,
        55,
        (60 + 64) / 2,
        (65 + 69) / 2,
        75,
        85,
        95,
        (100 + 104) / 2,
    ]
    df_baseline365 = df_baseline365.set_index("age")

    df_baseline17 = df_baseline17.reset_index()
    df_baseline17["age"] = [
        25,
        35,
        45,
        55,
        (60 + 64) / 2,
        (65 + 69) / 2,
        75,
        85,
        95,
        (100 + 104) / 2,
    ]
    df_baseline17 = df_baseline17.set_index("age")

    plt.figure(figsize=(9, 9))

    label = "コロナ罹患した場合の死亡率 (平均17日)"
    plt.plot(
        df_covid.index,
        df_covid["infected_death_rate [1/10K]"],
        marker="o",
        color="tab:blue",
        label=label,
    )

    plt.plot(
        df_baseline17.index,
        df_baseline17["death_rate_no_suicide"],
        marker="o",
        color="tab:orange",
        label="17日間での自然死亡率",
    )

    label = "年齢"
    plt.xlabel(label, size=15)
    plt.xlim(20, 100)
    title = "コロナ罹患と自然死亡率比較 [万人に一人]\n（高いほど死ににくいことを表す）"
    plt.title(title, size=20)
    plt.ylim(0, 20)
    plt.grid(True)
    plt.legend(fontsize="large")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
