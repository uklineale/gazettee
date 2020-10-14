mkdir raw_docs/
mkdir images/
mkdir parsed_texts/

#Ubuntu only
apt update
apt install tesseract-ocr libtesseract-dev
source venv/bin/activate
pip3 install -r requirements.txt