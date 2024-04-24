from datetime import datetime

# Sorts dates from highest to lowest
def high_low_date_sort(date_list, date_format="%Y %m %d"):
    return sorted(date_list, key=lambda date: datetime.strptime(date, date_format), reverse=True)

