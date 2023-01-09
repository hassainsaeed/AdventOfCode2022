class FileReader:
    def __init__(self, filename):
        self.filename = filename
    
    def read_input_file(self):
        file_input = open(self.filename, 'r')
        read_file = file_input.read()
        parsed_input = read_file.split('\n')
        return parsed_input