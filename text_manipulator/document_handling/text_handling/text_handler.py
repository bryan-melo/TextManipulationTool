class TextHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def process_text(self):
        with open(self.file_path, 'r') as infile, open('output.txt', 'w') as outfile:
            for line in infile:
                modified_line = line.replace(',', '$$')
                outfile.write(modified_line)
