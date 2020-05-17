
import constant
import requests
import helper
import time
import csv

def main():
    with open('result.csv', 'w') as file:
        for range in helper.getDateRanges():
            #print (range['start'], range['end'])
            s = requests.Session()
            res = s.get(constant.url)
            cookies = dict(res.cookies)
            print (constant.url + constant.jsonurl.format(range['start'], range['end']))
            r = requests.get(constant.url + constant.jsonurl.format(range['start'], range['end']),cookies=cookies)
            while "<head>" in r.text:
                print("Error in <HEAD>")
                time.sleep(constant.rate_limit) 
                s = requests.Session()
                res = s.get(constant.url)
                cookies = dict(res.cookies)                
                r = requests.get(constant.url + constant.jsonurl.format(range['start'], range['end']),cookies=cookies)
            rows = helper.convertJson(r.text)             
            for row in rows:
                print(row)
                file.write(row + '\n')
            time.sleep(constant.rate_limit) 
main()