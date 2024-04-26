from pypdf import PdfReader


def readPDFStuff(pdfName):
    # creating PDF reader
    reader = PdfReader(pdfName + ".pdf")

    # create extraction text file
    myFile = "pdfExtraction.txt"

    originalFileText = "originalfiletext.txt"

    # read/ extract text
    with open(myFile, "w", encoding="utf-8") as text_file:
        for page in reader.pages:
            text = page.extract_text()
            text_file.write(text)
            text_file.write("\n")

    # open the output text file in write mode
    with open(originalFileText, "w", encoding="utf-8") as text_file:
        for page in reader.pages:
            text = page.extract_text()
            text_file.write(text)
            text_file.write("\n")

    print("Text extracted and saved to:", myFile)
