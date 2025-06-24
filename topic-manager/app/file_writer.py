class FileWriter:
    def write_line(self, line, filename=None):
        if filename is None:
            filename = "output.txt"
        with open(filename, 'w') as file:
            file.write(line)

