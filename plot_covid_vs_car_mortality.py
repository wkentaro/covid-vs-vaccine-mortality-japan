#!/usr/bin/env python

import japanize_matplotlib  # NOQA
import matplotlib.pyplot as plt
import numpy as np

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

    label = "1年間にコロナ罹患かつ死ぬ確率　 (2021-01-06時点)"
    plt.plot(
        df_covid.index,
        df_covid["covid_death_rate [1/10K]"],
        marker="o",
        color="tab:purple",
        label=label,
    )

    plt.plot(
        np.linspace(0, 100),
        [13] * 50,
        color="tab:brown",
        linestyle="dashed",
        label="1年間に歩行者として自動車事故で死ぬ確率",
    )

    label = "年齢"
    plt.xlabel(label, size=15)
    plt.xlim(20, 100)
    title = "コロナ罹患と自動車事故死亡率比較 [万人に一人]\n（高いほど死ににくいことを表す）"
    plt.title(title, size=20)
    plt.ylim(0, 650)
    plt.grid(True)
    plt.legend(fontsize="large")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
