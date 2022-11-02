# pip install pdfminer.six
from pdfminer.high_level import extract_text
 
def extract_text_from_pdf(pdf_path):
    textpdf = extract_text(pdf_path)

    return textpdf


if __name__ == '__main__':
    print(extract_text_from_pdf('./JesseMusaResumeFall2022.pdf'))  # noqa: T001 
