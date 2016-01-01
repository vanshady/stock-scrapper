import re
import urllib2
import csv
from bs4 import BeautifulSoup

nameOfStocks = []

try:
    with open('stockNames.csv' ,'rb') as csvfile:
         reader = csv.reader(csvfile, delimiter=',')
         for row in reader:
            nameOfStocks = row
            break
except IOError:
        print 'Cannot open stockNames.csv'

url = "https://www.google.com/finance?q="
valueOfStocks = {}
for stock in nameOfStocks:
    data = urllib2.urlopen(url+stock).read().decode("utf-8")
    soup = BeautifulSoup(data, "html.parser")
    tag = soup.find("meta",{"itemprop":"price"})
    value = tag["content"]
    valueOfStocks[stock] = value
    #print("The value of " + stock + " is " + value)

with open('stock.csv', 'w') as csvfile:
    fieldnames = ['stock', 'value']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for stock in nameOfStocks:
        writer.writerow({'stock': stock, 'value': valueOfStocks[stock]})
