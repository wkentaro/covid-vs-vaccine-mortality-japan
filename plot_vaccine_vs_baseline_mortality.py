#!/usr/bin/env python

import japanize_matplotlib  # NOQA
import matplotlib.pyplot as plt

import _utils


def main():
    df_covid = _utils.get_covid_data()
    df_vaccine = _utils.get_vaccine_data()
    df_baseline5 = _utils.get_baseline_data(n_date=5)
    df_baseline365 = _utils.get_baseline_data(n_date=365)

    print(df_covid)
    print(df_vaccine)

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

    # -------------------------------------------------------------------------

    plt.figure(figsize=(9, 9))

    label = "ワクチン接種後に死ぬ確率 (平均5日)"
    plt.plot(
        df_vaccine.index,
        df_vaccine["1/vaccine_death_rate [10K]"],
        marker="o",
        color="tab:green",
        label=label,
    )
    plt.plot(
        df_baseline5.index,
        df_baseline5["death_rate_no_suicide"],
        marker="o",
        color="tab:red",
        label="5日間での自然死亡率",
    )
    plt.plot(
        [(20 + 65) / 2, (65 + 100) / 2],
        [
            df_baseline5[df_baseline5.index < 65][
                "death_rate_no_suicide"
            ].mean(),
            df_baseline5[df_baseline5.index >= 65][
                "death_rate_no_suicide"
            ].mean(),
        ],
        marker="o",
        color="tab:red",
        linestyle="dashed",
        label="5日間での自然死亡率（65歳未満 or 65歳以上平均)",
    )

    label = "年齢"
    plt.xlabel(label, size=15)
    plt.xlim(20, 100)
    title = "ワクチン接種と自然死亡率比較 [万人に一人]\n（高いほど死ににくいことを表す）"
    plt.title(title, size=20)
    plt.ylim(0, 65)
    plt.grid(True)
    plt.legend(fontsize="large")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
