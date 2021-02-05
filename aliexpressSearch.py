import requests
import json

def extractNameFromURL(productUrl):
        EcomScrapeurl = "https://mlscrape-beta.p.rapidapi.com/v1/product"

        productUrl = {"url":productUrl,"proxy":"enabled"}

        scrapeHeaders = {
            'x-rapidapi-key': "ad7cccc825msha5999ab40c26e2cp1ad400jsn6a1e0b331ccc",
            'x-rapidapi-host': "mlscrape-beta.p.rapidapi.com"
            }

        productScrape = requests.request("GET", EcomScrapeurl, headers=scrapeHeaders, params=productUrl)

        jsonProduct = productScrape.json()

        productName = jsonProduct["name"]
        return productName;

def searchAliexpress(productName):
    limit = 20

    url = "https://ali-express1.p.rapidapi.com/search"

    querystring = {"query":"{}".format(productName),"from":"0","country":"CO","limit":"{}".format(limit)}

    headers = {
        'x-rapidapi-key': "ad7cccc825msha5999ab40c26e2cp1ad400jsn6a1e0b331ccc",
        'x-rapidapi-host': "ali-express1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    jsonData = response.json()

    products = []

    i = 0
    for i in range(limit):
        title = jsonData[i]["productElements"]["title"]["title"]
        price = jsonData[i]["productElements"]["price"]["sell_price"]["formatedAmount"]
        imageURL = jsonData[i]["productElements"]["image"]["imgUrl"]
        product = {"Title":title, "price":price, "imageURL": imageURL}
        products.append(product)
    return products

URL = "https://motrendy.com/collections/toys-kids-gift/products/eggs"

PRODUCT_NAME = extractNameFromURL(URL)
productList = searchAliexpress(PRODUCT_NAME)

for product in productList:
    #FIX!!!!
    print(product["Title"] + " " + product["price"].partition())
