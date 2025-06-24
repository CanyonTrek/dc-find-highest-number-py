from app.topic_top_score import TopicTopScore
from app.topic_score_writer import TopicScoreWriter
from app.file_writer import FileWriter


def main():
    # Sample data
    top_scores = [
        TopicTopScore("Physics", 89),
        TopicTopScore("Art", 78),
        TopicTopScore("Comp Sci", 97)
    ]

    # Create writer with real FileWriter
    file_writer = FileWriter()
    score_writer = TopicScoreWriter(file_writer)

    # Write the scores
    score_writer.write_scores(top_scores)

if __name__ == '__main__':
    main()

