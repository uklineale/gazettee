import requests
import time
from bs4 import BeautifulSoup
import boto3

# Built around Eugene gov site
class Scraper:
    error_counter = 0

    def __init__(self, out_path):
        self.out_path = out_path
        self.url = 'https://www.eugene-or.gov/ArchiveCenter/ViewFile/Item/'
        self.error_limit = 15

    def download_documents(self, docs):
        print("Iterating through documents %s-%s" % (docs[0], docs[-1]))
        readable_docs = list(docs)

        for i in docs:
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
                readable_docs.remove(i)
            
            if self.error_counter >= self.error_limit:
                print("Too many consecutive failures. Stopping.")
                return
            
            # Don't wreck govt servers
            time.sleep(2)
        
        return readable_docs




