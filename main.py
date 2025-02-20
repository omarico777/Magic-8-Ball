
import random
responses = ["Yes, definetly" , " no , not now" , "ask again later", "It is certain" , "very doubtful" , "outlook is good" , "better not tell you now"
             ,"concentrate and ask again" ]

def get_random_response():
    return random.choice(responses)

def get_user_question():
    question = input("ask the magical 8 ball a question (type 'exit' to quit):")
    if question.lower() == "exit":
        return None
    return question

def res(response):
    print("\n the magic 8 ball says",response,"\n")

def play_again():
    while True:
        choice = input("do you want to ask a question(y/n):").strip().lower()
        if choice == "y":
            return True
        elif choice == "no":
            return False
        else:
            print("plz type y/n")
