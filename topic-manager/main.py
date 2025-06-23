from app.topic_manager import TopicManager

def main():
    # Create an instance of TopicManager
    manager = TopicManager()

    # Call the method with an empty list (just for demonstration)
    results = manager.find_topic_high_scores([])

    # Print the result
    print("Top Scores:", results)

if __name__ == "__main__":
    main()

