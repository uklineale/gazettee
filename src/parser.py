from pdf2image import convert_from_path
import os
import time
from shutil import copyfile
import re
from PIL import Image
import pytesseract
from sklearn.feature_extraction.text import TfidfVectorizer

POLICY_LINES = 5
TITLE_LINES = 20

class Parser:
    def __init__(self, pdf_dir, image_dir, parsed_dir, retitled_dir):
        self.pdf_dir = pdf_dir
        self.image_dir = image_dir
        self.parsed_dir = parsed_dir
        self.retitled_dir = retitled_dir

    def clean(self, id):
        f = open(self.parsed_dir + str(id) + '.txt', 'r+')
        
        unclean = f.read()
        no_empty_lines = re.sub('^\s+', '', unclean)

        f.seek(0)
        f.write(no_empty_lines)
        f.close()

    # Only works on EPD police policy documents
    # TODO: parse dates in rename
    def retitle(self, id):
        filename = str(id) + ".txt"
        title = ''

        try:
            with open(self.parsed_dir + filename) as f:
                whitespace_matcher = re.compile('^\s+')
                lines = [next(f) for x in range(TITLE_LINES)]
                lines = [x for x in lines if whitespace_matcher.match(x) is None]
                title = ''
                print(lines)

                for i in range(len(lines)):
                    line = lines[i]
                    if 'PURPOSE AND SCOPE' in line and i > 1:
                        subject = lines[i-1]
                        trimmed = subject.lower().replace("\n","")
                        snaked = trimmed.replace(" ", "_")

                        title = str(id) + "_police_" + snaked + ".txt"
                        print("Writing " + title)

            if title is not '': 
                copyfile(self.parsed_dir + filename, self.retitled_dir + title)        
            else:
                print("Skipping " + filename)
        except Exception as e:
            print("Exception!!")
            print(e)
            return 

            
#TODO: rotate horizontally scanned images (from books), creates garbage after OCR
    def parse_pdfs(self, id, pages=300):
        try:
            if self.already_parsed(id):
                print("Skipping " + str(id))
                return

            filename = str(id) + ".pdf"
            print("Parsing " + filename)
            pages = convert_from_path(self.pdf_dir + filename, pages)

            page_num = 0
            for page in pages:
                image_name = "page_" + str(page_num) + ".jpg"
                page.save(self.image_dir + image_name, 'JPEG')
                page_num += 1

            base = os.path.splitext(filename)[0]
            out = open(self.parsed_dir + base + '.txt', 'a')

            for i in range(page_num):
                image_path = self.image_dir + "page_" + str(i) + ".jpg"
                text = str(pytesseract.image_to_string(Image.open(image_path)))
                text = text.replace('-\n', '')
                out.write(text)
            
            out.close()

            [os.remove(self.image_dir + f) for f in os.listdir(self.image_dir)]   
        except Exception as e:
            print("Exception!!")
            print(e)
            return

    def already_parsed(self, id):
        return os.path.exists(self.parsed_dir + str(id) + ".txt")

    
