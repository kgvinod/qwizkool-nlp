from Question import Question
from WebArticle import WebArticle
from WikipediaArticle import WikipediaArticle

#first_question = Question("What is your name")
#print(first_question)

#web_article = WebArticle('capacitor', 'https://en.wikipedia.org/wiki/Capacitor')
#web_article.open()

wiki_article = WikipediaArticle('India')
wiki_article.open()
wiki_article.parse()

