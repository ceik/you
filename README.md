# Description

Python application to load data into a local MongoDB instance and from there to a Google Sheet

## Requirements
Dependencies are listed in [requirements.txt](requirements.txt). To install them run:
```bash
$ pip install -r requirements.txt
```

MongoDB needs to run locally on the default port 27017

## Configuration

A service account needs to be created and the path to the credentials file needs
to be added to [config.py](config.py). Instructions for this can be found [here](https://gspread.readthedocs.io/en/latest/oauth2.html).

A Google Sheet needs to be created and the id of it needs to be added to
[config.py](config.py). The import and aux tab in that sheet need to be configured like in
[this example](https://docs.google.com/spreadsheets/d/1WjLClbeHwbOeDDA-wFl1N-m-2se-4WVNeohCESsdLuA).
Also the service account created in the previous step needs to have edit access
to this sheet.

## Run
Run main and provide the path to the csv containing the data:
```bash
$ python main.py data/test_data.csv
```
