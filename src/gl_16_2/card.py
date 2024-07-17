import time
import random


class Card():  # класс Карта
    NumsList = ["Джокер", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Валет", "Дама", "Король", "Туз"]
    MastList = ["пик", "крестей", "бубей", "червей"]

    def __init__(self, i, j):  # конструктор
        self.Mastb = self.MastList[i - 1]  # карта
        self.Num = self.NumsList[j - 1]  # масть


# ----------------------------------------
class DeckOfCards():  # класс Колода карт
    def __init__(self):  # конструктор
        self.deck = [None] * 56  # список из 56 карт
        k = 0
        for i in range(1, 4 + 1):
            for j in range(1, 14 + 1):
                self.deck[k] = Card(i, j)  # очередная карта
                k += 1

    def shuffle(self):  # перемешивание карт
        random.shuffle(self.deck);

    def get(self, i):  # вытаскивание i-й карты из колоды
        if 0 <= i <= 55:
            answer = self.deck[i].Num
            answer += " "
            answer += self.deck[i].Mastb
            return answer
        else:
            answer = "В колоде только 56 карт"
            return answer


# ----------------------------------------
deck = DeckOfCards()  # создали колоду
deck.shuffle()  # перемешали
# print('Выберите карту из колоды в 56 карт:')
# n = int(input())
# if n <= 56:
#     card = deck.get(n - 1)
#     print('Вы взяли карту: ', card, end='.\n')
# else:
#     print("В колоде только 56 карт")

for n in range(1,56):
    card = deck.get(n - 1)
    print('Вы взяли карту: ', card, end='.\n')
