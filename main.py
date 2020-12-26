from src import parser, scraper, documentStore, classifier

RAW_DOCS_DIR = "raw_docs/"
IMAGE_DIR = "images/"
PARSED_DIR = "parsed_texts/"
RETITLED_DIR = "human_readable/retitled_texts/"

# Find police auditor info, summarize snippets and outcome (find patterns in what's getting dismissed)
# City council meeting minutes about police budget

def store(start, end):
    p = parser.Parser(RAW_DOCS_DIR, IMAGE_DIR, PARSED_DIR, RETITLED_DIR)
    s = scraper.Scraper(RAW_DOCS_DIR)
    dao = documentStore.DocumentStore(RAW_DOCS_DIR, PARSED_DIR)

    s.download_pages(start,end)
    for i in range(start, end):
        p.parse_pdfs(i)
    dao.upload(PARSED_DIR)

def analyze(start, end):
    dao = documentStore.DocumentStore(RAW_DOCS_DIR, PARSED_DIR)
    c = classifier.Classifier(PARSED_DIR)
    # for i in range(start, end):
    #     dao.download(PARSED_DIR, i)
    c.classify_pdfs()

def main():
    start = 2500
    end = 2530
    # Scrape, parse, and upload to S3/Dynamo
    # store(start,end)
    # Download and run tf-idf
    analyze(start,end)

if __name__ == '__main__':
    main()