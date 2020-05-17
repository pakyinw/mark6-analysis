import json
import math
import calendar
from datetime import datetime

def convertJson(text):
    if not text:
        return []
    if not text.strip():
        return []
    if "<head>" in text:
        return ['error']
    
    #print('text:', text)
    
    json_array = json.loads(text)
    store_list = []

    for item in json_array:
        store_details = ''
        store_details = item['date'] 
        for no in item['no'].split('+'):
            store_details += ',' + no
        store_details += ',' + item['sno']
        store_list.append(store_details)

    return store_list

def getDateRanges():
    dateRanges = []

    now = datetime.now()
    currentDay = now.day
    currentMonth = now.month
    currentYear = now.year
    nearestMonth = math.floor(math.floor((currentMonth - 1) / 3) * 3 + 1)
    print('nearestMonth',nearestMonth)

    #
    if currentYear != 1993:
        for y in range(1993,currentYear):
            for m in range(1,11,3):
                pair = {'start': str(y) + str(m).zfill(2) + '01', 'end': str(y) + str(m+2).zfill(2) + str(calendar.monthrange(y,m+2)[1])}
                dateRanges.append (pair)

    
    #
    if nearestMonth != 1:
        for m in range(1,nearestMonth,3):
            pair = {'start': str(currentYear) + str(m).zfill(2) + '01', 'end': str(currentYear) + str(m+2).zfill(2) + str(calendar.monthrange(currentYear,m+2)[1])}
            dateRanges.append (pair)


    # today to nearest month
    firstPair = {'start': str(currentYear) + str(nearestMonth).zfill(2) + '01', 'end': str(currentYear) + str(currentMonth).zfill(2) + str(currentDay).zfill(2)}
    dateRanges.append(firstPair)

    return dateRanges