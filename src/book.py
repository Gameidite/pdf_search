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
    
    def save_book(self, fp):
        import json

        with open(fp + ".json", "w+") as outfile:
            json.dump(self.book, outfile)

    def load_json(self, fp):
        import json

        with open(fp, "r") as json_file:
            self.book = json.load(json_file)

    def search_pages(self, text):
        pass

def get_options_str(options):
    options_str = ""
    for i in options:
        options_str += i +" "
    return options_str


if __name__ == "__main__":
    from tkinter import Tk
    from tkinter import filedialog

    options = ["exit", "save book"]
    root = Tk()
    root.withdraw()
    
    file_path = filedialog.askopenfilename(filetypes=[("PDF", "*.pdf"), ("JSON", "*.json")])
    
    file_name_ind = file_path.rfind("/")
    file_type_ind = file_path.rfind(".")
    file_name = file_path[file_name_ind+1:file_type_ind]

    bk = book(file_path)
    
    while 1:
        
        choice = input("Enter options("+ get_options_str(options) + "): ")
        if choice.lower() == "exit":
            break
        if choice.lower() == "save book":
            folder_path = filedialog.askdirectory()
            
            bk.save_book(folder_path + "/" + file_name)
