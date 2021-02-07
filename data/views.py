from django.shortcuts import render
from django.http import HttpResponse
from data.scrape import *
import schedule
import time



def home_view(*args, **kwargs):
    
    schedule.every(10).seconds.do(scrape_data)


    while True:
        schedule.run_pending()
        time.sleep(1) 


    return HttpResponse("<h1>Scrape Home <h2>")







 