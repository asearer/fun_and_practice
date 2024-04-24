from datetime import datetime

def low_high_date_sort(date_list, date_format="%Y %m %d"):
    # Sorts dates from lowest to highest based on the given date format
    return sorted(date_list, key=lambda date: datetime.strptime(date, date_format))
