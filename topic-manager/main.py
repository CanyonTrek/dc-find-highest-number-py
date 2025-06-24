from app.topic_top_score import TopicTopScore
from app.topic_score_writer import TopicScoreWriter
from app.file_writer import FileWriter

def main():
    # Prepare a list of topic scores
    top_scores = [
        TopicTopScore("Physics", 89),
        TopicTopScore("Art", 87),
        TopicTopScore("Comp Sci", 97)
    ]

    # Instantiate a file writer
    file_writer = FileWriter()

    # Instantiate the TopicScoreWriter with the file writer
    writer = TopicScoreWriter(file_writer)

    # Write all topic scores to the specified file
    writer.write_scores(top_scores, filename="testfile.txt")

    print("Finished writing topic scores to testfile.txt")

if __name__ == "__main__":
    main()

