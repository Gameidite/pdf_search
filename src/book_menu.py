
def get_options_str(options):
    options_str = ""
    options_len = len(options)

    for i in range(options_len):
        options_str += options[i]

        if i != options_len - 1:    
            options_str += ", "
    
    return options_str


if __name__ == "__main__":
    from tkinter import Tk
    from tkinter import filedialog
    from book import book

    options = ["exit", "save book", "load new book"]
    root = Tk()
    root.withdraw()
    
    #replace tkinter filedialog with win32 dialog later
    file_path = filedialog.askopenfilename(filetypes=[("PDF", "*.pdf"), ("JSON", "*.json")])
    
    file_name_ind = file_path.rfind("/")
    file_type_ind = file_path.rfind(".")
    file_name = file_path[file_name_ind+1:file_type_ind]

    bk = book(file_path)
    
    while 1:
        
        choice = input("Enter options("+ get_options_str(options) + "): ").lower()
        #when an interface is made, replace this with == and use int values to make it
        #slightly more efficient
        
        if "save" in choice:
            folder_path = filedialog.askdirectory()
            
            bk.save_book(folder_path + "/" + file_name)

        elif "open" in choice:
            new_fp = filedialog.askopenfilename(filetypes=[("PDF", "*.pdf"), ("JSON", "*.json")])
            
            bk.init_book(new_fp)

        else:
            break
