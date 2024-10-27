from random import randint

class Comment:
    def __init__(self, text, author):
        self.deleted = None
        self.children = []
        self.val = text
        self.author = author

    def add_reply(self, reply):
        self.children.append(reply)

    def remove_reply(self):
        self.deleted = True

    def display(self, indentation = 0):
        if self.deleted:
            print('\t'*indentation + 'Цей коментар було видалено.')
        else:
            print('\t' * indentation + f'{self.author}: {self.val}')
        for child in self.children:
            child.display(indentation + 1)

if __name__ == "__main__":
    root_comment = Comment("Яка чудова книга!", "Бодя")
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
    reply1.add_reply(reply1_1)

    reply1.remove_reply()

    root_comment.display()

