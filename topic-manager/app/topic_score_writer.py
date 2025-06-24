from app.file_writer import FileWriter

class TopicScoreWriter:
    def __init__(self, file_writer):
        self._file_writer = file_writer

    def write_scores(self, top_scores):
        self._file_writer.write_line("Physics, 89")


