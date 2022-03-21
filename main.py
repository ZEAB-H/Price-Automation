import requests
import bs4
import time
import tkinter
from tkinter import messagebox


while True:
    Laptop = requests.get("https://www.flipkart.com/hp-pavilion-core-i5-11th-gen-16-gb-512-gb-ssd-windows-11-home-14-dv1001tu-thin-light-laptop/p/itmc20c712eaccc5")
    soup = bs4.BeautifulSoup(Laptop.text,'xml')
    price = soup.find("", {"class":'_3I9_wc _2p6lqe'})
    prices=[]
    prices.append(price.text)
    actual_price=prices[0]
    actual_price = actual_price[1:3] + actual_price[4:7]
    price=int(actual_price)
    time.sleep(10)
    if price>29000:
            tkinter.messagebox.showinfo(title="Prompt", message= " you should NOT buy, the price of the Laptop became "+ price)
    elif price<29000:
           tkinter.messagebox.showinfo(title="Prompt", message=" you should buy, the price of the Laptop became " + price)
