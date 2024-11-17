import fitz  # PyMuPDF

doc = fitz.open("pdf_to_be_processed.pdf") # open a document

for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    pix = page.get_pixmap()
    output = f"page_{page_num + 1}.jpg"
    pix.save(output)
