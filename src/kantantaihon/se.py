class SELibrary:
    library = set()

    @classmethod
    def add(cls, name):
        cls.library.add(name)

    @classmethod
    def get(cls):
        return cls.library
