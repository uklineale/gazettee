from src import parser, scraper

RAW_DOCS_DIR = "raw_docs/"
IMAGE_DIR = "images/"
PARSED_DIR = "parsed_texts/"

# Find police auditor info, summarize snippets and outcome (what's getting dismissed)
# City council meeting minutes about police budget

def main():
    s = scraper.Scraper(RAW_DOCS_DIR)
    s.download_pages(2109, 2250)

if __name__ == '__main__':
    main()