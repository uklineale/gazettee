from src import parser, scraper, documentStore, classifier

RAW_DOCS_DIR = "raw_docs/"
IMAGE_DIR = "images/"
PARSED_DIR = "parsed_texts/"
RETITLED_DIR = "human_readable/retitled_texts/"

# Find police auditor info, summarize snippets and outcome (find patterns in what's getting dismissed)
# City council meeting minutes about police budget

def scrape(start, end):
    p = parser.Parser(RAW_DOCS_DIR, IMAGE_DIR, PARSED_DIR, RETITLED_DIR)
    s = scraper.Scraper(RAW_DOCS_DIR)

    for i in range(start, end):
        p.parse_pdfs(i)
        p.retitle(i)
        p.clean(i)

def upload():
    u = documentStore.DocumentStore(RAW_DOCS_DIR, IMAGE_DIR, PARSED_DIR, RETITLED_DIR)
    u.upload_retitled()

def main():
    test = 'here is a sentence. a sentence'
    c = classifier.Classifier('a', (1,100), (1,100))
    print(c.term_frequency(test))


if __name__ == '__main__':
    main()