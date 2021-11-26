# manual for the Article class:
# https://www.bibtex.com/e/article-entry/

def getArticles(fields, sort_by, filters):
    #let me get these Articles from the other layer
    pass

class Article:
    def __init__(self):
        self._author=""
        self._title=""
        self._journal=""
        self._year=""
        self._volume=""
        self._number=""
        self._pages=""
        self._month=""
        self._note=""
        #I've added every field it's not necessary to use every field

    def getAuthor(self):
        return self._author

    def getTitle(self):
        return self._title

    def getJournal(self):
        return self._journal

    #todo and so on...