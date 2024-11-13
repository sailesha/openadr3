import requests
import zipfile
import io
import pandas as pd
from datetime import datetime, timedelta


OASIS_URL = "http://oasis.caiso.com/oasisapi/SingleZip"
#NODE = "TH_NP15_GEN-APND"
NODE = "SLAP_PGEB-APND"


class PriceInfo:
    def __init__(self, start_time, end_time, hour, price):
        self.start_time = start_time
        self.end_time = end_time
        self.hour = hour
        self.price = price


def _get_prices_as_csv(start_date, end_date, node):
    """
    Fetches CAISO Day-Ahead Market prices as a CSV string for a specific node and date range.
    
    :param start_date: Start date in YYYYMMDD format.
    :param end_date: End date in YYYYMMDD format.
    :param node: Node identifier (default is NP15 trading hub for the East Bay region).
    :return: CSV data as a string if successful, None otherwise.
    """
    url = "http://oasis.caiso.com/oasisapi/SingleZip"
    params = {
        "queryname": "PRC_LMP",
        "version": "1",
        "startdatetime": f"{start_date}T07:00-0000",  # CAISO time format
        "enddatetime": f"{end_date}T07:00-0000",
        "market_run_id": "DAM",  # Day-Ahead Market
        "node": node,
        "resultformat": "6"  # CSV in zip format
    }

    # Send request to CAISO API
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        # Read the zip file from the response content
        with zipfile.ZipFile(io.BytesIO(response.content)) as zfile:
            # Extract the first file in the zip (should be a CSV)
            csv_filename = zfile.namelist()[0]
            with zfile.open(csv_filename) as csvfile:
                # Decode CSV data to a string
                csv_data = csvfile.read().decode('utf-8')
                return csv_data
    else:
        print(f"Error: {response.status_code}")
        return None


def _get_day_ahead_prices(start_date, end_date, node):
    # Get the CSV data as a string
    csv_data = _get_prices_as_csv(start_date, end_date, node)
    
    if csv_data:
        # Read CSV data into a DataFrame
        df = pd.read_csv(io.StringIO(csv_data))
        prices = []
        
        # Print the price for each hour
        for _, row in df.iterrows():
            if row["LMP_TYPE"] == "LMP":
                price = PriceInfo(
                    start_time = row['INTERVALSTARTTIME_GMT'],
                    end_time=row['INTERVALENDTIME_GMT'],
                    hour=row['OPR_HR'],
                    price=row['MW']
                )
                prices.append(price)
        prices.sort(key=lambda x: x.hour)
        return prices
    else:
        print("Failed to retrieve data.")
        return None


def get_day_ahead_prices():
    start_date = (datetime.now()).strftime("%Y%m%d")
    end_date = (datetime.now() + timedelta(days=1)).strftime("%Y%m%d")
    # start_date = "20241112"
    # end_date = "20241113"
    prices = _get_day_ahead_prices(start_date, end_date, NODE)
    # for price in prices:
    #     print(f"Hour: {price.hour}, Price: {price.price}")
    return prices
