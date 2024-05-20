import requests
import pandas as pd

def fetch_noaa_data():
    """
    Fetches the latest Planetary K-index data from NOAA's SWPC.
    The Planetary K-index quantifies disturbances in the horizontal component of earth's magnetic field
    with an integer in the range 0-9 with 1 being calm and 5 or more indicating a geomagnetic storm.
    """
    url = "https://services.swpc.noaa.gov/json/planetary_k_index_1m.json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error on bad status
        try:
            data = response.json()
            if data:
                df = pd.DataFrame(data)
                return df
            else:
                print("No data returned from the API.")
                return pd.DataFrame()
        except ValueError as e:  # Includes simplejson.decoder.JSONDecodeError
            print("Failed to decode JSON from response: {}".format(e))
            return pd.DataFrame()
    except requests.RequestException as e:
        print(f"Error fetching data from NOAA SWPC: {e}")
        return pd.DataFrame()

def main():
    noaa_data = fetch_noaa_data()
    if not noaa_data.empty:
        print("NOAA Planetary K-index Data:")
        print(noaa_data.head())
    else:
        print("No data to display.")

if __name__ == "__main__":
    main()

