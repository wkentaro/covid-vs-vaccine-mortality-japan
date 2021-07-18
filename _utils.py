import pandas


def get_covid_data():
    df = pandas.read_csv("./data/japan_covid_death.csv", comment="#")
    df = df.set_index("age")
    df1 = df

    df = pandas.read_csv("./data/japan_population.csv")
    df["population"] = df["male"] + df["female"]
    df = df.drop(columns=["male", "female"])
    df = df.set_index("age")
    df.loc["80+"] = df.loc["80s"] + df.loc["90+"]
    df = df.drop(["80s", "90+"])
    df2 = df

    df = pandas.concat([df1, df2], axis=1)
    df["infected_death_rate [1/10K]"] = df["infection"] / df["death"] / 1e4
    df["covid_death_rate [1/10K]"] = df["population"] / df["death"] / 1e4

    return df


def get_vaccine_data():
    df = pandas.read_csv("./data/japan_vaccination.csv", comment="#")
    df["vaccination"] = df["non_medical_workers"] + df["medical_workers"]
    df = df.drop(columns=["non_medical_workers", "medical_workers"])
    df = df.set_index("age")
    df1 = df

    df2 = pandas.read_csv("data/japan_vaccine_death.csv", comment="#")
    data = [
        {
            "age": "<65",
            "vaccine_death": df2[df2["max_age"] < 65]["vaccine_death"].sum(),
        },
        {
            "age": "65+",
            "vaccine_death": df2[df2["max_age"] >= 65]["vaccine_death"].sum(),
        },
    ]
    df = pandas.DataFrame(data)
    df = df.set_index("age")
    df2 = df

    df = pandas.concat([df1, df2], axis=1)

    df["vaccine_death_rate"] = df["vaccine_death"] / df["vaccination"]
    df["1/vaccine_death_rate"] = 1 / df["vaccine_death_rate"]
    df["1/vaccine_death_rate [10K]"] = df["1/vaccine_death_rate"] / 1e4

    df = df.drop(columns=["1/vaccine_death_rate"])

    return df


def get_baseline_data(n_date):
    df = pandas.read_csv("./data/japan_baseline_death_rate.csv", comment="#")
    df = df.set_index("age")
    df["death_rate_suicide"] = df["death_rate"] - df["death_rate_no_suicide"]
    df = df * (n_date / 365)  # N日間での自然死亡率
    df = (1 / df) / 1e4
    return df
