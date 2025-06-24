import os
import sys

# mpath =os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "find-highest_number"))
# sys.path.insert(0, mpath)
# from final.app.highest_number_finder import HighestNumberFinder

from app.topic_scores import TopicScores
from app.topic_manager import TopicManager
from app.topic_top_score import TopicTopScore
from unittest.mock import Mock


def main():
    # Arrange - test data
    physics_scores = [56, 67, 45, 89]
    art_scores = [87, 66, 78]
    comp_sci_scores = [45, 88, 97, 56]

    topic_scores = [
        TopicScores("Physics", physics_scores),
        TopicScores("Art", art_scores),
        TopicScores("Comp Sci", comp_sci_scores)
    ]

    # Create mock
    mock_finder = Mock()
    mock_finder.find_highest_number.side_effect = [89, 87, 97]

    # Inject mock into TopicManager
    manager = TopicManager(mock_finder)
    results = manager.find_topic_high_scores(topic_scores)

    # Assert-like print
    for topic in results:
        print(f"{topic.get_topic_name()}: {topic.get_top_score()}")



if __name__ == "__main__":
    main()

