import random
responses = ["Yes, definetly" , " no , not now" , "ask again later", "It is certain" , "very doubtful" , "outlook is good" , "better not tell you now"
             ,"concentrate and ask again" ]

def get_random_response():
    return random.choice(responses)
    