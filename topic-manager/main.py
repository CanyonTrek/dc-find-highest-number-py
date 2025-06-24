import os
import sys

mpath =os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "find-highest_number"))
sys.path.insert(0, mpath)

from final.app.highest_number_finder import HighestNumberFinder

from app.topic_scores import TopicScores
from app.topic_manager import TopicManager

def main():
    # Create example topic scores
    topics = [
        TopicScores("Physics", [56, 67, 45, 89]),
        TopicScores("Art", [87, 66, 78]),
        TopicScores("Comp Sci", [45, 88, 97, 56])
    ]

    # Use the real HighestNumberFinder
    finder = HighestNumberFinder()
    manager = TopicManager(finder)

    # Find top scores
    top_scores = manager.find_topic_high_scores(topics)

    # Print results
    print("Top scores by topic:")
    for ts in top_scores:
        print(f"{ts.get_topic_name()} - {ts.get_top_score()}")

if __name__ == "__main__":
    main()

