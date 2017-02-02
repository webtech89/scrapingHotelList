import requests, bs4
import csv
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

list_of_rows = []

url = 'http://www.fivestaralliance.com/luxury-hotels/68/europe/belgium'

response = requests.get(url)
html = response.content

soup = bs4.BeautifulSoup(html, "html.parser")

data = soup.findAll('div', attrs={'itemprop': 'itemListElement'})



for d in data:
    row = []

    item = d.find('div', attrs = {'class' : 'hotel-name-city'})

    name = item.find('a')    
    address = d.find('p', attrs = {'class' : 'hotel_address'})
    description = d.find('p', attrs = {'itemprop' : 'description'})
    style = d.find('div', attrs = {'class' : 'hotel-brief-style-inner-right'})
    #rating = d.find('div', attrs = {'class' :'hotel-brief-rating'})
 
    row.append(name.text)
    row.append(address.text)
    row.append(description.text)
    row.append(style.text)    
    
    list_of_rows.append(row)


RESULTS = ['HotelName', 'HotelAddress','HotelDescription', 'HotelStyle']

with open("hotelList.csv", "w") as resultFile:
    writer = csv.writer(resultFile)
    writer.writerow(RESULTS)     
 
    for row in list_of_rows:        
        writer.writerow(row)   
        
resultFile.close()  

