import PyPDF2

file_path = 'model.pdf'
pages=[]

with open(file_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    
    extracted_text = ""

    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        extracted_text += page.extract_text()
        pages.append(page.extract_text())
    
    questions=[]

    text=""
    for page in pages:
        for i in range(len(page)-1):
            if page[i]=='\n' and page[i+1].isdigit():
                print(text)
                questions.append(text)
                print("end")
                text=""
            else:
                text+=page[i]



