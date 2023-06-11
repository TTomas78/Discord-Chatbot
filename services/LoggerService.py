import os

class LoggerService:
    def __init__(self, folder,file_name):
        self.folder = folder
        self.file_name = file_name
        self._create_file()

    def _create_file(self):
    #create the folder if not exists
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)
        #create the file
        self.write_splitter()

    def write_splitter(self):
        file = open(os.path.join(self.folder,self.file_name), "a")
        file.write("--------------------------------------------------\n")
        file.close()
    
    def log_message(self,author, message, datetime):
        file = open(os.path.join(self.folder,self.file_name), "a")
        file.write(f'{datetime}:{author}:{message}\n')
        file.close()
