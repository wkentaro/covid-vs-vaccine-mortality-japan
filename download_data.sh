#!/bin/bash

curl http://www.ipss.go.jp/projects/j/Choju/covid19/data/japan_deaths.xlsx -o data/japan_covid_death.xlsx

curl https://www.stat.go.jp/data/jinsui/pdf/202106.pdf -o data/japan_population.pdf

curl https://www.mhlw.go.jp/content/10601000/000802338.pdf -o data/japan_vaccine_death.pdf

curl https://vrs-data.cio.go.jp/vaccination/opendata/latest/prefecture.ndjson -o data/japan_vaccination.ndjson.gz
rm -f data/japan_vaccination.ndjson
gunzip data/japan_vaccination.ndjson.gz
