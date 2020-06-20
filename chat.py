# simple-chat-bot
import random
import sys
Questions = [
    "How to use firefighting robot ?",
    "what care should ?",
    "for what purpose it can use"
    ]
Answers = [
    "First fill container of robot which will help to extinguise fire then switch on it's batttery to give power to the robot to work .",
    "keep it in room temperature"
    "clean it regularly",
    "when there is any type of fire accident "
    ]

print("Hii i am firefighting robot cbatbot\n")
def list_faq():
    for i in range(len(Questions)):
        print(str(i)+" : "+Questions[i])
        
def check_for_FAQ_by_index():
    list_faq()
    question_id = input("which question do you want to answer?\n")
    response = ""

    if "bye" in question_id:
        sys.exit()
    elif int(question_id) < len(Questions):
        response = Answers[int(question_id)]
    else:
        response = "I dont know the answer to that question "
    return response
def check_for_FAQ(question):
    response =" "
    if qustion in Questions:
        index = Questions.index(question)
        response = Answers[index]
    else:
        response = "I dont know the answer to that"
    return response
while True:
    response = check_for_FAQ_by_index()
    print("\n yourbot:  "  + response)
    
