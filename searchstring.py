from lxml import html
import time
from selenium import webdriver

url = "https://pokedextracker.com/u/ashketchum10/omega-ruby-living-dex" # Your URL here
latestPkmn = 495 # This is the last possible pokemon in the list

print("\n")
print("Fetching your list of uncaught pokemon")

browser = webdriver.Chrome() #replace with .Firefox(), or with the browser of your choice
browser.get(url) # Opens the website with WebDriver
time.sleep(5) # Sleep is needed for the website to load properly
browser.quit # For some reason this does not work

page = browser.page_source
tree = html.fromstring(page)


# Code for future reference
###########################
#This will create a list of caught:
#caught = tree.xpath('//*[@id="root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[@class="pokemon viewing captured"]/div[1]/p/text()[2]')


#This will create a list of uncaught
uncaught = tree.xpath('///div[@class="pokemon viewing"]/div[1]/p/text()[2]')

searchstring = ""

i = 0
for i in uncaught:
    if int(i) < latestPkmn:
        searchstring = searchstring + i + ","
    else:
       break 
searchstring = searchstring[:-1]

print("\n")
print (searchstring)