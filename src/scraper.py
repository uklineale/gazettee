import requests
import time
from bs4 import BeautifulSoup

# AMID_to_topic = {
#     '111' : "police_audit",
#     '112' : "city_co"
# }

# Built around Eugene gov site
class Scraper:
    error_counter = 0

    def __init__(self, out_path):
        self.out_path = out_path
        self.url = 'https://www.eugene-or.gov/ArchiveCenter/ViewFile/Item/'
        self.error_limit = 15


    def download_pages(self, start_page, end_page):
        print("Iterating through pages %s-%s" % (start_page, end_page))
        for i in range(start_page, end_page):
            url = self.url + str(i)
            pdf_page = requests.get(url)
            if pdf_page.status_code  < 299 :
                filename = self.out_path + str(i) + '.pdf'
                with open(filename, 'wb') as f:
                    f.write(pdf_page.content)
                self.error_counter = 0
            else:
                print("Failed to get page " + str(i))
                self.error_counter += 1
            
            if self.error_counter >= self.error_limit:
                print("Too many consecutive failures. Stopping.")
                return
            
            # Don't wreck govt servers
            time.sleep(2)




