import PyPDF2


def extract_text(pdf_file) -> str:

    reader = PyPDF2.PdfReader(pdf_file)

    text = " ".join(
        page.extract_text()
        for page in reader.pages
        if page.extract_text()
    )

    return text