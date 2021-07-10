from plot import get_covid_data
from plot import get_vaccine_data


df_covid = get_covid_data()
html = df_covid.to_html(
    formatters={
        "covid_death_rate": lambda x: f"{x:.6f}",
        "1/covid_death_rate [10K]": lambda x: f"{x:.2f}",
    }
)
with open("df_covid.html", "w") as f:
    f.write(html)

df_vaccine = get_vaccine_data()
html = df_vaccine.to_html(
    formatters={
        "vaccine_death_rate": lambda x: f"{x:.6f}",
        "1/vaccine_death_rate [10K]": lambda x: f"{x:.2f}",
    }
)
with open("df_vaccine.html", "w") as f:
    f.write(html)
