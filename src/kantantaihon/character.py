from .colors import CHARACTER_COLORS


class CharacterManager:
    characters = dict()
    n_characters = 0

    @classmethod
    def get_character(cls, name):
        if name in cls.characters:
            return cls.characters[name]
        else:
            if cls.n_characters >= len(CHARACTER_COLORS):
                raise ValueError(
                    "Maximum number of characters reached. Please add more colors to CHARACTER_COLORS.")
            character = Character(
                name, cls.n_characters)
            cls.characters[name] = character
            cls.n_characters += 1
            return character


class Character:
    def __init__(self, name, number):
        self.name = name
        self.dialogues = []
        self.character_count = 0
        self.number = number

    def add_dialogue(self, dialogue):
        self.dialogues.append(dialogue)
        self.character_count += len(dialogue)


class GlobalDialogues:
    character_count = 0

    @classmethod
    def count(cls, dialogue):
        cls.character_count += len(dialogue)


class Listener:
    def __init__(self):
        pass
