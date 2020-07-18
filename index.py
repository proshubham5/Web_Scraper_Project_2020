import os
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

from bs4 import BeautifulSoup

# selenium packages
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')

current_dir = os.path.dirname(__file__)
chrome_path = os.path.join(current_dir, 'chrome_driver/chromedriver.exe')


def get_html(url):
    # chrome web driver
    driver = webdriver.Chrome(chrome_path, chrome_options=chrome_options)

    driver.get(url)
    res = driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()

    html = BeautifulSoup(res, 'html.parser')
    return html


def get_url(button_id):
    url_dictionary = {
        1: 'https://www.amazon.in/Apple-iPhone-Pro-Max-64GB/dp/B07XVLMZHH/',
        2: 'https://www.amazon.in/Apple-MacBook-Air-13-3-inch-MQD32HN/dp/B073Q5R6VR/',
        3: 'https://www.amazon.in/Fender-CD-60CE-Dreadnought-Cutaway-Acoustic-Electric/dp/B001L8NGJW/',
        4: 'https://www.amazon.in/Nike-AIR-Vapormax-Run-Utility/dp/B07JWBWRG5/',
        5: 'https://www.amazon.in/All-new-Echo-Dot-3rd-Gen/dp/B07PFFMP9P/'
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

# Canvas to show scraped image of items; positioned in the left of bottom frame
scrapeCanvas = Label(bottom_frame, bg="pink")
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
feature_vertical_scrollbar = Scrollbar(price_bottom_frame, orient="vertical")
feature_horizontal_scrollbar = Scrollbar(price_bottom_frame, orient="horizontal")

feature_listbox = Listbox(price_bottom_frame, yscrollcommand=feature_vertical_scrollbar.set,
                          xscrollcommand=feature_horizontal_scrollbar.set)
feature_vertical_scrollbar.config(command=feature_listbox.yview)
feature_horizontal_scrollbar.config(command=feature_listbox.xview)
feature_listbox.place(relx=0.15, rely=0.5, relwidth=0.75, relheight=0.4)
feature_vertical_scrollbar.place(relx=0.9, rely=0.5, relheight=0.4)
feature_horizontal_scrollbar.place(relx=0.15, rely=0.9, relwidth=0.75)

description_tag = StringVar()
description_label = Label(price_bottom_frame, textvariable=description_tag, relief=RAISED)

description_tag.set("FEATURES : ")
description_label.place(relx=0.15, rely=0.43)

# reviews listbox in reviews_bottom_frame

reviews_tag = StringVar()
reviews_label = Label(reviews_bottom_frame, textvariable=reviews_tag, relief=RAISED)

reviews_tag.set("REVIEWS : ")
reviews_label.place(relx=0.1, rely=0.05)

# vertical scrollbar of reviews list
review_vertical_scrollbar = Scrollbar(reviews_bottom_frame, orient="vertical")
review_horizontal_scrollbar = Scrollbar(reviews_bottom_frame, orient="horizontal")

reviews_textbox = Text(reviews_bottom_frame, yscrollcommand=review_vertical_scrollbar.set,
                       xscrollcommand=review_horizontal_scrollbar.set, bg='white', fg='black')
review_vertical_scrollbar.config(command=reviews_textbox.yview)
review_horizontal_scrollbar.config(command=reviews_textbox.xview)
reviews_textbox.place(relx=0.1, rely=0.15, relheight=0.7, relwidth=0.8)
review_vertical_scrollbar.place(relx=0.9, rely=0.15, relheight=0.7)
review_horizontal_scrollbar.place(relx=0.1, rely=0.85, relwidth=0.8)


def handle_button_clicks(button_id):
    url = get_url(button_id)

    html = get_html(url)

    photo_url = ''
    if button_id == 1:
        photo_url = "./assets/iphone-11-pro.jpeg"
    elif button_id == 2:
        photo_url = "./assets/Apple_macbook_air.jpg"
    elif button_id == 3:
        photo_url = "./assets/guitar.jpg"
    elif button_id == 4:
        photo_url = "./assets/nike_shoes.jpg"
    elif button_id == 5:
        photo_url = "./assets/echo_dot.jpg"

    image = ImageTk.PhotoImage(Image.open(photo_url).resize((250, 225)))
    scrapeCanvas.configure(image=image)
    scrapeCanvas.image = image

    price_div = html.select('#priceblock_ourprice')
    price = price_div[0].get_text()
    price_text.delete(1.0, END)
    price_text.insert(1.0, price)

    review_outer = html.select('#cm-cr-dp-review-list')
    review_div = review_outer[0].select('div')[0].select('div')[0].select('div')[0].find_all('div', class_="a-expander-content reviewText review-text-content a-expander-partial-collapse-content")[0].find_all('span')
    if len(review_div) > 0:
        review = review_div[0].get_text()
        reviews_textbox.delete(1.0, END)
        reviews_textbox.insert(1.0, review)

    desc_li_array = html.select('#featurebullets_feature_div')[0].find_all('li')
    feature_listbox.delete(0, END)
    for li in desc_li_array:
        m_feature = li.find('span').get_text(strip=True)
        feature_listbox.insert(END, '* ' + m_feature)


# iphone image button
iPhoneImage = ImageTk.PhotoImage(Image.open("./assets/iphone-11-pro.jpeg").resize((60, 60)))
B1 = ttk.Button(top_frame, text="iPhone 11 pro", image=iPhoneImage, compound=TOP,
                command=lambda: handle_button_clicks(1))
B1.place(relx=0, rely=0, relheight=1, relwidth=0.2)

# 2th item button in top frame
MacBook = ImageTk.PhotoImage(Image.open("./assets/Apple_macbook_Air.jpg").resize((60, 60)))
B2 = ttk.Button(top_frame, text="Apple Macbook Air", image=MacBook, compound=TOP,
                command=lambda: handle_button_clicks(2))
B2.place(relx=0.2, rely=0, relheight=1, relwidth=0.2)

# 3rd item button in top frame
guitar = ImageTk.PhotoImage(Image.open("./assets/guitar.jpg").resize((40, 60)))
B3 = ttk.Button(top_frame, text="Fender CD-60CE Dreadnought Cutaway Acoustic-Electric Guitar", image=guitar,
                compound=TOP, command=lambda: handle_button_clicks(3))
B3.place(relx=0.4, rely=0, relheight=1, relwidth=0.2)

# 4th item button in top frame
g = ImageTk.PhotoImage(Image.open("./assets/nike_shoes.jpg").resize((40, 60)))
B4 = ttk.Button(top_frame, text="Nike AIR Vapormax Run Utility Shoes", image=g, compound=TOP,
                command=lambda: handle_button_clicks(4))
B4.place(relx=0.6, rely=0, relheight=1, relwidth=0.2)

# 5th item button in top frame
gt = ImageTk.PhotoImage(Image.open("./assets/echo_dot.jpg").resize((40, 60)))
B5 = ttk.Button(top_frame, text="Echo Dot 3rd Generation", image=gt, compound=TOP,
                command=lambda: handle_button_clicks(5))
B5.place(relx=0.8, rely=0, relheight=1, relwidth=0.2)



root.mainloop()
