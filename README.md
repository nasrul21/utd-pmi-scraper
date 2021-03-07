# UTD PMI Scraper
Scraper for UTD PMI (Unit Transfusi Darah, Palang Merah Indonesia) data using python

## How to use
### Setup
Inside your virtual environment, install package from requirement.txt
```
(venv) $ pip install -r requirements.txt
```
### Run scraper
```
(venv) $ python3 scraper.py [output type]
```
Example, output as JSON:
```
(venv) $ python3 scraper.py json
```
or output as CSV 
```
(venv) $ python3 scraper.py csv
```
output file will be `utd_pmi.[csv or json]`
