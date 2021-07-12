#!/usr/bin/env python

import argparse

import japanize_matplotlib  # NOQA
import matplotlib.pyplot as plt
import ndjson
import pandas


def get_covid_data():
    df = pandas.read_excel("./data/japan_covid_death.xlsx")

    ages = [
        "<10",
        "10s",
        "20s",
        "30s",
        "40s",
        "50s",
        "60s",
        "70s",
        "80s",
        "90+",
    ]
    data = []
    for age in ages:
        mask = df[df.columns[0]].str.contains(age)
        data.append(
            dict(
                age=age,
                covid_death_male=df[mask == True]["Unnamed: 1"].item(),
                covid_death_female=df[mask == True]["Unnamed: 2"].item(),
            )
        )
    df1 = pandas.DataFrame(data)
    df1 = df1.set_index("age")

    df = pandas.read_csv("./data/japan_population.csv")
    df = df.rename(
        columns={"male": "population_male", "female": "population_female"}
    )
    df2 = df.set_index("age")

    df = pandas.concat([df1, df2], axis=1)
    df["population"] = df["population_male"] + df["population_female"]
    df["covid_death"] = df["covid_death_male"] + df["covid_death_female"]
    df["covid_death_rate"] = df["covid_death"] / df["population"]
    df["1/covid_death_rate"] = 1 / df["covid_death_rate"]
    df["1/covid_death_rate [10K]"] = df["1/covid_death_rate"] / 1e4

    df["population"] = df["population"] / 1e4
    df = df.astype({"population": int})
    df = df.rename(columns={"population": "population [10K]"})

    df = df.drop(
        columns=[
            "covid_death_male",
            "covid_death_female",
            "population_male",
            "population_female",
            "1/covid_death_rate",
        ]
    )

    return df


def get_vaccine_data():
    with open("./data/japan_vaccination.ndjson") as f:
        data = ndjson.load(f)
    df = pandas.DataFrame(data)
    df = df[df["age"] != "UNK"]
    df = df[df["status"] == 1]
    df = df.replace({"-64": "<65", "65-": "65+"})
    df = df.rename(columns={"count": "vaccination"})
    df = df.groupby("age").sum()[["vaccination"]]
    df1 = df

    df2 = pandas.read_csv("data/japan_vaccine_death.csv")
    df2 = df2.set_index("age")
    df2 = df2.rename(
        columns={
            "male": "vaccine_death_male",
            "female": "vaccine_death_female",
        }
    )
    df2["vaccine_death"] = (
        df2["vaccine_death_male"] + df2["vaccine_death_female"]
    )

    df = pandas.concat([df1, df2], axis=1)

    df["vaccine_death_rate"] = df["vaccine_death"] / df["vaccination"]
    df["1/vaccine_death_rate"] = 1 / df["vaccine_death_rate"]
    df["1/vaccine_death_rate [10K]"] = df["1/vaccine_death_rate"] / 1e4

    df = df.drop(
        columns=[
            "population",
            "vaccine_death_male",
            "vaccine_death_female",
            "1/vaccine_death_rate",
        ]
    )

    return df


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--all-age", action="store_true", help="all age")
    parser.add_argument("--english", action="store_true", help="english")
    args = parser.parse_args()

    df_covid = get_covid_data()
    df_vaccine = get_vaccine_data()

    print(df_covid)
    print(df_vaccine)

    df_covid = df_covid.reset_index()
    df_covid["age"] = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
    df_covid = df_covid.set_index("age")

    df_vaccine = df_vaccine.reset_index()
    df_vaccine["age"] = [(65 + 100) / 2, (20 + 64) / 2]
    df_vaccine = df_vaccine.set_index("age")

    if not args.all_age:
        df_covid = df_covid[df_covid.index > 40]
        df_vaccine = df_vaccine[df_vaccine.index > 40]

    plt.figure(figsize=(9, 9))
    if args.english:
        label = "Mortality by COVID　 (reported until 2021-07-05)"
    else:
        label = "コロナによる死亡率　 (2021-07-05時点)"
    plt.plot(
        df_covid.index,
        df_covid["1/covid_death_rate [10K]"],
        marker="o",
        label=label,
    )
    if args.english:
        label = "Mortality by vaccination (reported until 2021-07-07)"
    else:
        label = "ワクチンによる死亡率 (2021-07-07時点)"
    plt.plot(
        df_vaccine.index,
        df_vaccine["1/vaccine_death_rate [10K]"],
        marker="o",
        label=label,
    )
    # ワクチンの死亡率がコロナを上回る年齢
    plt.vlines(54.2, ymin=-10, ymax=200, colors="k", linestyles="dashed")
    plt.xticks(list(plt.xticks()[0]) + [54.2])
    if args.english:
        label = "Age"
    else:
        label = "年齢"
    plt.xlabel(label, size=15)
    if args.all_age:
        plt.xlim(20, 100)
    else:
        plt.xlim(40, 100)
    if args.all_age:
        if args.english:
            title = "Mortality in all ages [1 person per 10K]\n（Higher means lower the mortality）"
        else:
            title = "全年齢の死亡率 [万人に一人]\n（高いほど死ににくいことを表す）"
    else:
        if args.english:
            title = "Mortality in over 40 years [1 person per 10K]\n（Higher means lower the mortality）"
        else:
            title = "40歳以上の死亡率 [万人に一人]\n（高いほど死ににくいことを表す）"
    plt.title(title, size=20)
    if args.all_age:
        plt.ylim(-10, 200)
    else:
        plt.ylim(-1, 20)
    plt.grid(True)
    plt.legend(fontsize="large")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
