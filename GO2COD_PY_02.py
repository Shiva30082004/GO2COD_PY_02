'''
GO2COD PYTHON PROGRAMMING INTERNSHIP
TASK 02 : WEB SCRAPER
NAME: SHIV BHAVSAR

This program will scrap the data (eg. headlines, prices) from specific website
using BeautifulSoup and requests modules. For this program I am using a website
which is easy to scrap because some popular websites has advanced security features
in them, so it becomes more difficult to scrap data from them directly. Here
I am scraping one book selling website.

'''

from bs4 import BeautifulSoup
import requests

# URL of website to scrap
url = 'http://books.toscrape.com/'

try:
    # get the info from the url to be scrap using requests
    page = requests.get(url)

    # parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(page.text, 'html.parser')

    # find all products
    products = soup.find_all('article', class_='product_pod')

    print("Product Titles and Prices:")

    # loop through each product and extract the data
    for item in products:
        # extract the title of the product
        title = item.find('h3').find('a')['title']
        
        # extract the price of the product
        price = item.find('p', class_='price_color').text.strip()

        # display the title and price
        print("Title: ",title," - Price: ",price)

# error handling if page is not fetched or it doesn't exsist
except Exception as e:
    print("Error fetching the webpage:", e)








