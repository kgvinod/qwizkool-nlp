from Question import Question
from WebArticle import WebArticle
from WikipediaArticle import WikipediaArticle

#first_question = Question("What is your name")
#print(first_question)

#web_article = WebArticle('capacitor', 'https://en.wikipedia.org/wiki/Capacitor')
#web_article.open()

title = input('Wikipedia page to parse=')

wiki_article = WikipediaArticle(title)
wiki_article.open()
wiki_article.parse()

