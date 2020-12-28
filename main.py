from Question import Question
from WebArticle import WebArticle
from WikipediaArticle import WikipediaArticle
from Quiz import Quiz
from QkContext import QkContext
import time
import wikipedia

#first_question = Question("What is your name")
#print(first_question)

#web_article = WebArticle('capacitor', 'https://en.wikipedia.org/wiki/Capacitor')
#web_article.open()

qk_ctx = QkContext('medium')

while (True):
    title = input('Wikipedia page to parse=')

    wiki_article = WikipediaArticle(title, qk_ctx)
    try:
        wiki_article.open()
    except wikipedia.exceptions.PageError:
        print ("Cannot find information for " + title + "!!!")
        continue

    wiki_article.parse()

    quiz = Quiz(wiki_article, 5)

    question_num = 1
    for question in quiz.questions:
        print(question.generate_question_str(question_num))
        answer = int(input("Select your answer: "))
        if question.is_correct_answer(answer):
            print("Correct Answer!\n\n")
            quiz.correct_answers += 1
        else:
            print("You didn't get that right :(. Answer is " + question.answer + ".\n\n") 
            quiz.wrong_answers += 1
        
        time.sleep(2.0)    
        question_num += 1

    print("\n=================")         
    print("Your score is " + str(quiz.correct_answers) + "/" + str(quiz.correct_answers + quiz.wrong_answers))
    print("=================\n")  

