class book(object):
    def __init__(self, book_fp):
        self.book = {}
        self.init_book(book_fp)
    
    def init_book(self, bookfp):

        period_ind = bookfp.rfind(".")
        filetype = bookfp[period_ind + 1:]

        if filetype == "pdf":
            self.load_pdf(bookfp)

        elif filetype == "json":
            self.load_json(bookfp)

        else:
            raise TypeError("filetype not supported")

    def load_pdf(self, fp):
        from PyPDF2 import PdfFileReader as pyPdfReader

        with open(fp, "rb") as pdf_file:
            
            reader = pyPdfReader(pdf_file, strict=True)
            
            for i in range(reader.getNumPages()):
                page = reader.getPage(i)
                self.book[i] = page.extractText()
        print(self.book)
    
    def save_book(self, fp):
        import json

        with open(fp, "w") as outfile:
            json.dump(self.book, outfile)

    def load_json(self, fp):
        import json

        with open(fp, "r") as json_file:
            self.book = json.load(json_file)

    def search_pages(self, text):
        pass

if __name__ == "__main__":
    from tkinter import Tk
    from tkinter import filedialog

    root = Tk()
    root.withdraw()
    
    file_path = filedialog.askopenfilename()
    
    bk = book(file_path)
    exit_bool = False
    while not exit_bool:
        
