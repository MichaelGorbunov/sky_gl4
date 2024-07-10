class Article:
    """"Knacc Ona XpaHexus cTaTbu """
    article_id: int
    title: str
    content: str
    articles = dict()

    def __init__(self, title, content):
        """ KOHCTPYKTOp Ona cTaTbu """
        self.article_id = self.get_new_id()
        self.title = title
        self.content = content

    def get_new_id(self) -> int:
        """ Metod dna nonyyexun ID cnedyowyet cTaTbu """
        if len(self.articles) > 0:
            return (max(self.articles)) + 1
        return 1

    @classmethod
    def insert(cls, title: str, content: str):
        """ MeTod dna co3daHUuA U dobaBNeHUA cTaTbU """
        new_article = cls(title, content)
        cls.articles[new_article.article_id] = new_article
        return new_article


if __name__ == '__main__':
    new_article_1 = Article.insert('test1', 'test1')
    print(new_article_1.article_id)
    new_article_2 = Article.insert('test2', 'test2')
    print(new_article_2.article_id)
