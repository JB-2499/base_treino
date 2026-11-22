class Book:
    def __init__(self, title, synopsis=None, available=False, id=None):
        self.id = id
        self.title = title
        self.synopsis = synopsis
        self.available = available

    @property
    def status(self):
        return "Disponível" if self.available else "Indisponível"