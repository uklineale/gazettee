from pdf2image import convert_from_path
import os
from PIL import Image
import pytesseract

class Parser:
    def __init__(self, pdf_dir, image_dir, parsed_dir):
        self.pdf_dir = pdf_dir
        self.image_dir = image_dir
        self.parsed_dir = parsed_dir


#TODO: rotate horizontally scanned images (from books), creates garbage after OCR
    def parse_pdfs(self, pages=300):
        for filename in os.listdir(self.pdf_dir):
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
