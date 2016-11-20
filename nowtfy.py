import gi
import bs4
import random
import urllib
import time
import os
import sys

gi.require_version('Notify', '0.7')
from gi.repository import Notify
from bs4 import BeautifulSoup

def get_data_from_page():
    #Read link
    dirx = os.path.dirname(os.path.realpath(sys.argv[0]))
    dirx += '/data.txt'
    infile =  open(dirx);
    link = str(infile.readline())
    infile.close()
    #Make page request and scrape off HTML
    page = urllib.urlopen(link)
    handle = page.read()
    soup = BeautifulSoup(handle, "html.parser")
    #Scrape using CSS selector
    #Example
    upcoming_events_div = soup.find('span', class_='score')
    score = upcoming_events_div.text
    append_text = 'Your score on the page is: '
    return str(append_text + score)


Notify.init("Nowtify")
#get data from page
data = get_data_from_page()
#create and show notif
my_notif = Notify.Notification.new(data)
my_notif.show()