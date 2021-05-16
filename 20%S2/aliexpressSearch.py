# aliexpressSearch.py
# Addison Hoff
# Extracts name from user inputted url, searches name on Aliexpress and returns results.
import requests
import json

class Product:
        name = ""
        price = 0
     def __init__(self, name, price):
        self.name = name
        self.price = price

     def name():
         return name

     def price():
         return price




def extractNameFromURL(productUrl):
        EcomScrapeurl = "https://mlscrape-beta.p.rapidapi.com/v1/product"

        productUrl = {"url":productUrl,"proxy":"enabled"}

        #MLScrape Keys
        scrapeHeaders = {
            'x-rapidapi-key': "ad7cccc825msha5999ab40c26e2cp1ad400jsn6a1e0b331ccc",
            'x-rapidapi-host': "mlscrape-beta.p.rapidapi.com"
            }

        productScrape = requests.request("GET", EcomScrapeurl, headers=scrapeHeaders, params=productUrl)

        jsonProduct = productScrape.json()

        productName = jsonProduct["name"]
        price = int(jsonProduct["price"]["value"])
        extractedProduct = Product(productName, price)
        return extractedProduct;

def searchAliexpress(extractedProduct):
    limit = 20

    url = "https://ali-express1.p.rapidapi.com/search"

    querystring = {"query":"{}".format(extractedProduct.name()),"from":"0","country":"CO","limit":"{}".format(limit)}

    #Aliexpress Keys
    headers = {
        'x-rapidapi-key': "ad7cccc825msha5999ab40c26e2cp1ad400jsn6a1e0b331ccc",
        'x-rapidapi-host': "ali-express1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    jsonData = response.json()

    products = []

    return jsonData

userLink = input("Please enter user link ")
extractedProduct = extractNameFromURL(userLink)
jsonResponse = searchAliexpress(extractedProduct)
for (int i = 0; i <= len(jsonResponse["data"]["searchResult"]["mods"]["itemList"]["content"]); i++):
    print("Product " + str(i) + ": " + jsonResponse["data"]["searchResult"]["mods"]["itemList"]["content"][i]["title"]["displayTitle"])
    aliPrice = int(jsonResponse["data"]["searchResult"]["mods"]["itemList"]["content"][i]["prices"]["sale_price"]["minPrice"])
    print("Price " + str(i) + ": " + aliPrice  +
    " " + (extractedProduct.price() - aliPriceprice))

print("See results: " + "https://www.aliexpress.com/af/Santa-Claus-Expression-Eggs-Keychains.html?d=y&origin=n&SearchText=" + extractedName +"&catId=0&initiative_id=SB_20210514042527")
