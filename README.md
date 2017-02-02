# scrapingHotelList
This script get the list of hotel in Belgium using BeautifulSoup and save the results to CSV file

http://www.fivestaralliance.com/luxury-hotels/68/europe/belgium

I added following code 

import sys
reload(sys)
sys.setdefaultencoding('utf8')

When I save the results to csv file, it occurs following error.

UnicodeEncodeError 'ascii' codec can't encode character u'\u2019' in position 59"ordinal not in range(128)

Run 

python getHotelList.py

You will get hotelList.csv file.



