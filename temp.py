# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

question_examples = open("C:\\Users\\Scott Bowling\\Documents\\KoreanTextFiles\\KoreanExampleQuestions.txt", "r", encoding="utf-8")
questionContent = question_examples.read()
"""print(content)
"""
questionList = questionContent.split(",")
question_examples.close()


verbs_examples = open("C:\\Users\\Scott Bowling\\Documents\\KoreanTextFiles\\KoreanVerbs.txt", "r", encoding="utf-8")
verbContent = verbs_examples.read()
"""print(content)
"""
verbList = verbContent.split(",")
verbs_examples.close()


flag = True


"""print(random.choice(content_list))"""


"""
if inputText.lower() == "yes":
    print(random.choice(content_list))
    my_function()
    
if inputText.lower() == "Done":
    raise SystemExit
else:
    print(random.choice(content_list))
"""



def my_function(flag):
    if flag == True:
        print(random.choice(questionList))
        print(random.choice(verbList))
        inputText = input("Did you answer the question?")
        another_function(inputText)
        
    else:       
        inputText = input("Did you answer the question?")
        another_function(inputText)
        flag = False
    
       
    
def another_function(answer):
    if answer.lower() == "yes":
        print(random.choice(questionList))
        print(random.choice(verbList))
        my_function(False)
        
    if answer.lower() == "done":
        raise SystemExit
    else:
        print("Question: " + random.choice(questionList))

my_function(True)
yes





