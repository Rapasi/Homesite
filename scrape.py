import os
import django
import requests
import pandas as pd
import io
import datetime
import csv
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'economics.settings')
django.setup()

from economical_data.models import GeneralFinancialData


def ECB_rates(key,save=False):
    entrypoint = 'https://data-api.ecb.europa.eu/service'  # API entry point
    resource = 'data'  # Resource for data queries
    flowRef = 'FM'  # Series key for main refinancing operations interest rate
    
    parameters = {
        'startPeriod': '1900-01-01',  # Start date of the time series
        'endPeriod': datetime.date.today().strftime('%Y-%m-%d')  # End date of the time series
    }
    
    # Constructing the API request URL
    request_url = f"{entrypoint}/{resource}/{flowRef}/{key}"
    
    # Making the HTTP request
    response = requests.get(request_url, params=parameters, headers={'Accept': 'text/csv'})
    
    # Checking the response
    if response.status_code == 200:
        reader = csv.DictReader(response.text.splitlines())
        for row in reader:
            if save:
                financial_data, created = GeneralFinancialData.objects.get_or_create(
                    TITLE=row['TITLE'],
                    TIME_PERIOD=row['TIME_PERIOD'],
                    defaults={'OBS_VALUE': float(row['OBS_VALUE'])}
                )
                if created:
                    # Do something if the object is newly created (optional)
                    pass
            else:
                print(row)


def euribor_rates(key):
    entrypoint = 'https://api.boffsaopendata.fi/v4/'  # API entry point
     # Series key for main refinancing operations interest rate
    dataset="MFI_PUBL"
    url=f"{entrypoint}/observations/{dataset}"
    print(url)
    parameters = {
        'startPeriod': '1900-01-01',  # Start date of the time series
        'endPeriod': datetime.date.today().strftime('%Y-%m-%d')  # End date of the time series
    }

    # Making the HTTP request
    response = requests.get(url)
    
    # Checking the response
    if response.status_code == 200:
        response_dict = json.loads(response.text)
        print(response.text)

                
    else:
        print(response.status_code)

if __name__ == "__main__":

    ECB_rates('D.U2.EUR.4F.KR.MLFR.LEV',save=True)
    ECB_rates('D.U2.EUR.4F.KR.DFR.LEV',save=True)
    ECB_rates('D.U2.EUR.4F.KR.MRR_FR.LEV',save=True)
    #euribor_rates("M.U2.EUR.RT.MM.EURIBOR1YD_.HSTA")
