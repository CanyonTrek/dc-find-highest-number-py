import unittest
from app.topic_manager import TopicManager
from app.topic_top_score import TopicTopScore
from app.topic_scores import TopicScores

class HighestNumberFinderStub:
    def find_highest_number(self, numbers):
        return 89  # Always returns the expected max for testing


class TopicManagerTest(unittest.TestCase):
    def test_find_highest_score_in_empty_array_returns_empty_list(self):
        # Arrange
        scores = []  # List[TopicScores]
        cut = TopicManager()
        expected_result = []

        # Act
        result = cut.find_topic_high_scores(scores)

        # Assert
        self.assertEqual(result, expected_result)


    def test_find_highest_score_with_list_of_one_returns_list_of_one(self):
        # Arrange
        scores = [56, 67, 45, 89]
        topic_name = "Physics"
        topic_scores = [TopicScores(topic_name, scores)]

        cut = TopicManager()
        expected_result = [TopicTopScore(topic_name, 89)]

        # Act
        result = cut.find_topic_high_scores(topic_scores)

        # Assert
        self.assertEqual(result[0].get_topic_name(), expected_result[0].get_topic_name())
        self.assertEqual(result[0].get_top_score(), expected_result[0].get_top_score())


    def test_find_highest_score_with_one_topic_using_stub(self):
        # Arrange
        scores = [56, 67, 45, 89]
        topic_name = "Physics"
        topic_scores_list = [TopicScores(topic_name, scores)]

        hnf_stub = HighestNumberFinderStub()
        cut = TopicManager(hnf_stub)

        expected_result = [TopicTopScore(topic_name, 89)]

        # Act
        result = cut.find_topic_high_scores(topic_scores_list)

        # Assert
        self.assertEqual(result[0].get_topic_name(), expected_result[0].get_topic_name())
        self.assertEqual(result[0].get_top_score(), expected_result[0].get_top_score())


if __name__ == "__main__":
    unittest.main()

