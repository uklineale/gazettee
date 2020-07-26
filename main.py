from src import parser, scraper

RAW_DOCS_DIR = "raw_docs/"
IMAGE_DIR = "images/"
PARSED_DIR = "parsed_texts/"
RETITLED_DIR = "retitled_texts/"

# Find police auditor info, summarize snippets and outcome (what's getting dismissed)
# City council meeting minutes about police budget

def main():
    p = parser.Parser(RAW_DOCS_DIR, IMAGE_DIR, PARSED_DIR, RETITLED_DIR)
    s = scraper.Scraper(RAW_DOCS_DIR)
    start = 4351
    end = 4485
    # s.download_pages(4201,5700)
    # p.retitle('unnamed_4351.txt')
    for i in range(start, end):
        # p.parse_pdfs(i)
        p.retitle(i)

if __name__ == '__main__':
    main()