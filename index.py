import os
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

from ImageRequest import simple_get
from bs4 import BeautifulSoup

# selenium packages
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')

current_dir = os.path.dirname(__file__)
chrome_path = os.path.join(current_dir, 'chrome_driver/chromedriver.exe')

# chrome web driver
driver = webdriver.Chrome(chrome_path, chrome_options=chrome_options)


def get_html(url):
    url1 = "https://www.selenium.dev/documentation/en/introduction/the_selenium_project_and_tools/"
    url2 = "https://www.amazon.in/Fender-CD-60CE-Dreadnought-Cutaway-Acoustic-Electric/dp/B001L8NGJW/"

    driver.get(url)
    res = driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()

    html = BeautifulSoup(res, 'html.parser')
    return html


def get_url(button_id):
    url_dictionary = {
        1: '',
        2: '',
        3: '',
        4: '',
        5: ''
    }

    return url_dictionary.get(button_id, None)


root = Tk()
root.geometry("1000x500")
root.title("webscraper")

# options frame
top_frame = Frame(root)
top_frame.place(relx=0, rely=0, relheight=0.25, relwidth=1)

# scraped details frame
bottom_frame = Frame(root)
bottom_frame.place(relx=0, rely=0.25, relheight=0.75, relwidth=1)

# iphone image button
iPhoneImage = ImageTk.PhotoImage(Image.open("./assets/iphone-11-pro.jpeg").resize((60, 60)))
B1 = ttk.Button(top_frame, text="iPhone 11 pro", image=iPhoneImage, compound=TOP)
B1.place(relx=0, rely=0, relheight=1, relwidth=0.2)

# 2th item button in top frame
asusVivoBook = ImageTk.PhotoImage(Image.open("./assets/Asus_ViviBook_14.jpg").resize((60, 60)))
B2 = ttk.Button(top_frame, text="Asus Vivo-Book 14", image=asusVivoBook, compound=TOP)
B2.place(relx=0.2, rely=0, relheight=1, relwidth=0.2)

# 3rd item button in top frame
guitar = ImageTk.PhotoImage(Image.open("./assets/guitar.jpg").resize((40, 60)))
B3 = ttk.Button(top_frame, text="Fender CD-60CE Dreadnought Cutaway Acoustic-Electric Guitar", image=guitar,
                compound=TOP)
B3.place(relx=0.4, rely=0, relheight=1, relwidth=0.2)

# 4th item button in top frame
g = ImageTk.PhotoImage(Image.open("./assets/guitar.jpg").resize((40, 60)))
B3 = ttk.Button(top_frame, text="Fender CD-60CE Dreadnought Cutaway Acoustic-Electric Guitar", image=g, compound=TOP)
B3.place(relx=0.6, rely=0, relheight=1, relwidth=0.2)

# 5th item button in top frame
gt = ImageTk.PhotoImage(Image.open("./assets/guitar.jpg").resize((40, 60)))
B3 = ttk.Button(top_frame, text="Fender CD-60CE Dreadnought Cutaway Acoustic-Electric Guitar", image=gt, compound=TOP)
B3.place(relx=0.8, rely=0, relheight=1, relwidth=0.2)

# Canvas to show scraped image of items; positioned in the left of bottom frame
scrapeCanvas = Canvas(bottom_frame, bg="pink")
scrapeCanvas.place(relx=0.025, rely=0.2, relheight=0.6, relwidth=0.25)

# price and description frame at the middle of bottom frame
price_bottom_frame = Frame(bottom_frame)
price_bottom_frame.place(relx=0.35, rely=0, relheight=1, relwidth=0.3)

# reviews frame in bottom frame at very right
reviews_bottom_frame = Frame(bottom_frame)
reviews_bottom_frame.place(relx=0.65, rely=0, relheight=1, relwidth=0.35)

# price textbox in price_bottom_frame
price_text = Text(price_bottom_frame, bg='white', fg='green', height=1, wrap=WORD)
price_text.place(relx=0.25, rely=0.3, relwidth=0.5)

price_tag = StringVar()
price_label = Label(price_bottom_frame, textvariable=price_tag, relief=RAISED)

price_tag.set("PRICE : ")
price_label.place(relx=0.25, rely=0.23)

# description textbox in price_bottom_frame
price_text = Text(price_bottom_frame, bg='white', fg='black', wrap=WORD)
price_text.place(relx=0.15, rely=0.5, relwidth=0.75, relheight=0.4)

description_tag = StringVar()
description_label = Label(price_bottom_frame, textvariable=description_tag, relief=RAISED)

description_tag.set("DESCRIPTION : ")
description_label.place(relx=0.15, rely=0.43)

# reviews listbox in reviews_bottom_frame

reviews_tag = StringVar()
reviews_label = Label(reviews_bottom_frame, textvariable=reviews_tag, relief=RAISED)

reviews_tag.set("REVIEWS : ")
reviews_label.place(relx=0.1, rely=0.05)

# vertical scrollbar of reviews list
scrollbar = Scrollbar(reviews_bottom_frame, orient="vertical")

reviews_listbox = Listbox(reviews_bottom_frame, yscrollcommand=scrollbar.set)
scrollbar.config(command=reviews_listbox.yview)
reviews_listbox.place(relx=0.1, rely=0.15, relheight=0.7, relwidth=0.8)
scrollbar.place(relx=0.9, rely=0.15, relheight=0.7)


def handle_button_clicks(button_id):
    url = get_url(button_id)

    html = get_html(url)


root.mainloop()
