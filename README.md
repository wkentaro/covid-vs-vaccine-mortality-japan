# covid-vs-vaccine-mortality-japan

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
./plot.py [--all-age]
```

<img src="docs/plots/all_age.png" width="49%"> <img src="docs/plots/over_40.png" width="49%">

```
# Covid data table
     population [10K]  covid_death  covid_death_rate  1/covid_death_rate [10K]
age
<10               956            0      0.000000e+00                       inf
10s              1094            0      0.000000e+00                       inf
20s              1274            7      5.494505e-07                182.000000
30s              1383           27      1.952278e-06                 51.222222
40s              1791          102      5.695142e-06                 17.558824
50s              1678          309      1.841478e-05                  5.430421
60s              1534          860      5.606258e-05                  1.783721
70s              1644         2766      1.682482e-04                  0.594360
80s               936         4888      5.222222e-04                  0.191489
90+               257         2504      9.743191e-04                  0.102636

# Vaccination data table
     vaccination  vaccine_death  vaccine_death_rate  1/vaccine_death_rate [10K]
age
65+     24614681            523            0.000021                    4.706440
<65      2665544             38            0.000014                    7.014589
```


## Reference

- 日本人口(2021-06): https://www.stat.go.jp/data/jinsui/pdf/202106.pdf
- コロナによる年齢別死亡者数(2021-07-05): http://www.ipss.go.jp/projects/j/Choju/covid19/
- ワクチンによる死亡者数(2021-07-07): https://www.mhlw.go.jp/content/10601000/000802338.pdf
- ワクチン接種者数(2021-07-07): https://cio.go.jp/c19vaccine_opendata
