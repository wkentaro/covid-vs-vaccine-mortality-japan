#!/usr/bin/env python

import matplotlib.pyplot as plt
import ndjson
import pandas
import seaborn


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

    return df


def main():
    df_covid = get_covid_data()
    df_vaccine = get_vaccine_data()

    df_covid = df_covid.reset_index()
    df_covid["age"] = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]

    df_vaccine = df_vaccine.reset_index()
    df_vaccine["age"] = [(65 + 100) / 2, (20 + 64) / 2]

    print(df_covid)
    print(df_vaccine)

    seaborn.lineplot(data=df_covid, x="age", y="1/covid_death_rate [10K]", marker="o")
    seaborn.lineplot(data=df_vaccine, x="age", y="1/vaccine_death_rate [10K]", marker="o")
    plt.xlim(20, 100)
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
