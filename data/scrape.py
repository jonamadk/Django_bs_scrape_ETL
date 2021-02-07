
import requests
import bs4
from bs4 import BeautifulSoup 
from data.models import *
from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
from datetime import date
import pdb
=======

from datetime import date
>>>>>>> test


def scrape_data():

    url = "https://merolagani.com/LatestMarket.aspx"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    table =soup.find("div",id="ctl00_ContentPlaceHolder1_LiveTrading").find("tbody")

    rows = table.find_all("tr")

 
    details =[]
    
    for data in rows:
        date_published = date.today()
        company_name_symbol = data.find_all('td')[0].text
        change_percent_value= data.find_all('td')[3].text
        high_value = data.find_all('td')[4].text
        low_value = data.find_all('td')[5].text
        open_value = data.find_all('td')[6].text
        qty= data.find_all('td')[7].text

        


        item = LiveTradingData(company_name_symbol= company_name_symbol, high_value= float(high_value.replace(",","")),
                                    open_value= float(high_value.replace(",","")), low_value=float(open_value.replace(",","")),
<<<<<<< HEAD
                                    change_percent_value=float(change_percent_value.replace(",","")),qty=float(qty.replace(",","")),date_value=date_today)
=======
                                    change_percent_value=float(change_percent_value.replace(",","")),qty=float(qty.replace(",","")), date_published=date_published)
>>>>>>> test

        details.append(item.save())

    return details








            
        
    



        


        



