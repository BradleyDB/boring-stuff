# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 21:47:49 2020

@author: bradl
"""

####################

'''Not for commercial or bulk use.
This is designed to get the pricing, manufacurer and product names from
backcountry.com listed products.

The way backcountry codes their pricing requires additional conditional
statements to retrieve pricing information depending on if it is a regular
or sale priced item. This is why pricing has it's own function.

'''


####################


import requests, bs4, re

def get_text(product_url):
    #this function returns the desired text from the product
    item = {} #empty dict for item properties
    #Retrieves Web Data
    result = requests.get(product_url)
    result.raise_for_status()    
    soup = bs4.BeautifulSoup(result.text, 'html.parser')
    css_path = soup.select('#content > div > div.product-overview.js-product-overview > section.product-buybox.js-product-buybox.qa-product-buybox > div.product-pricing.js-item-price')
    
    def price(css_path):
        #this function looks to see if the item is regular or sale priced and grab the appropriate CSS selectors
        no_price = ['Price Not Found']
        if '''class="product-pricing__discount"''' not in str(css_path):
          #this grabs the standard price
            reg_price = soup.select('#content > div > div.product-overview.js-product-overview > section.product-buybox.js-product-buybox.qa-product-buybox > div.product-pricing.js-item-price > span')    
            no_sale = reg_price[0].text.strip()
            return no_sale
        elif '''class="product-pricing__discount"''' in str(css_path):
           #this grabs the regular and sale and price
            get_prices = soup.select('#content > div > div.product-overview.js-product-overview > section.product-buybox.js-product-buybox.qa-product-buybox > div.product-pricing.js-item-price')
            prices = get_prices[0].text.strip()
            sale_price = re.compile(r'''(\$\d+[.]\d+)''', re.VERBOSE)
            final_sale_price = sale_price.findall(prices)                               
            all_prices = {'Sale Price:':final_sale_price[0], 'Regular Price:':final_sale_price[1]}
            return all_prices
        else:
            #returns if no pricing information is found
            return no_price
    
   
    #Retrieves item information from CSS paths
    manufacturer = soup.select('#content > div > div.product-overview.js-product-overview > section.product-buybox.js-product-buybox.qa-product-buybox > div.product-buybox-intro > h1 > span')
    name = soup.select('#js-bottomline-section')
    
    #calls the price function to determine if the price is on sale or not, 
    #and return the price value(s)
    price = price(css_path)
    
    
   #Pairs cleaned up values from URL retriever with key names and adds them to a dict
    new_manufacturer = {'Manufacturer: ' : manufacturer[0].text.strip()}
    new_name = {'Name: ' : name[0].text.strip()}
    new_price = {'Price: ' : price}
    property_list = [new_manufacturer, new_name, new_price]
    
    
    #Adds new key value pairs to the item dict. Should I change item to list and append?
    for thing in property_list:
        item.update(thing)

    return item

#Returning the outputs
shirt = get_text('https://www.backcountry.com/arc-teryx-component-t-shirt-mens?skid=ARCZ93E-BLAHEA-L&ti=U2VhcmNoIFJlc3VsdHM6YXJjdGVyeXggbWVuczoxOjM6YXJjdGVyeXggbWVucw==')
pack = get_text('https://www.backcountry.com/the-north-face-hydra-26l-backpack-tnf05cf?skid=TNF05CF-CITYELOR-SM&ti=UExQIFJ1bGUgQmFzZWQ6QW4gQWR2ZW50dXJlLUZpbGxlZCBGYXRoZXIncyBEYXk6MTo3Og==')

print(pack)
print(shirt)