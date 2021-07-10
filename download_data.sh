#!/bin/bash

# http://www.ipss.go.jp/projects/j/Choju/covid19/
# @2021-07-05
curl http://www.ipss.go.jp/projects/j/Choju/covid19/data/japan_deaths.xlsx -o data/japan_covid_death.xlsx

# @2021-06
curl https://www.stat.go.jp/data/jinsui/pdf/202106.pdf -o data/japan_population.pdf

# @2021-07-07
curl https://www.mhlw.go.jp/content/10601000/000802338.pdf -o data/japan_vaccine_death.pdf

# https://cio.go.jp/c19vaccine_opendata
# @2021-07-07
curl https://vrs-data.cio.go.jp/vaccination/opendata/2021-07-07/prefecture.ndjson -o data/japan_vaccination.ndjson.gz
rm -f data/japan_vaccination.ndjson
gunzip data/japan_vaccination.ndjson.gz
