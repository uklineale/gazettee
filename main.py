from src import parser, scraper, uploader

RAW_DOCS_DIR = "raw_docs/"
IMAGE_DIR = "images/"
PARSED_DIR = "parsed_texts/"
RETITLED_DIR = "retitled_texts/"

# Find police auditor info, summarize snippets and outcome (find patterns in what's getting dismissed)
# City council meeting minutes about police budget

def download(start, end):
    p = parser.Parser(RAW_DOCS_DIR, IMAGE_DIR, PARSED_DIR, RETITLED_DIR)
    s = scraper.Scraper(RAW_DOCS_DIR)

    for i in range(start, end):
        p.parse_pdfs(i)
        p.retitle(i)

def upload():
    u = uploader.Uploader(RAW_DOCS_DIR, IMAGE_DIR, PARSED_DIR, RETITLED_DIR)
    u.upload_retitled()

def main():
    upload()


if __name__ == '__main__':
    main()