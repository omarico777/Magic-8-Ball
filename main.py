def get_user_question():
    question = input("ask the magical 8 ball a question (type 'exit' to quit):")
    if question.lower() == "exit":
        return None
    return question

    