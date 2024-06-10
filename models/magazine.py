
class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category
        self._articles = []

    def articles(self):
        return self._articles
