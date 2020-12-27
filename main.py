from src import parser, scraper, documentStore, classifier, queueClient

RAW_DOCS_DIR = "raw_docs/"
IMAGE_DIR = "images/"
PARSED_DIR = "parsed_texts/"
RETITLED_DIR = "human_readable/retitled_texts/"

# Find police auditor info, summarize snippets and outcome (find patterns in what's getting dismissed)
# City council meeting minutes about police budget

def store(start, end):
    p = parser.Parser(RAW_DOCS_DIR, IMAGE_DIR, PARSED_DIR, RETITLED_DIR)
    s = scraper.Scraper(RAW_DOCS_DIR)
    qc = queueClient.QueueClient()
    dao = documentStore.DocumentStore(RAW_DOCS_DIR, PARSED_DIR)

    docs = list(range(start, end))
    unstored_docs = [ d for d in docs if not dao.is_stored(d) ]
    readable_docs = s.download_documents(unstored_docs)
    
    for i in readable_docs:
        p.parse_pdfs(i)
        p.clean(i)
        dao.upload(i)
        qc.upload_new_doc(i)

def analyze(start, end):
    dao = documentStore.DocumentStore(RAW_DOCS_DIR, PARSED_DIR)
    for i in range(start, end):
        dao.download(PARSED_DIR, i)

def main():
    # Scrape, parse, and upload to S3/Dynamo
    store(2500,2510)
    # Download and run tf-idf
    # analyze(2500,2515)

if __name__ == '__main__':
    main()