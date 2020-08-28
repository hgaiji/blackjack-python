import random
class Card():
    marks = ["♡","♤","♢","♧"]
    nums = {1:"A",11:"J",12:"Q",13:"k" }
    
    def __init__(self, mark, num):
    # コンストラクタでカードを用意する
        self.mark = mark
        self.num = num
        self.numbers = [Card.nums[i] if i in Card.nums else str(i) for i in list(range(1,14))]
    def __repr__(self):
        return Card.marks[self.mark] + self.numbers[self.num]
class Deck():
    def __init__(self):
        self.cards = [Card(mark,num) for mark in range(4) for num in list(range(13))]
        # カードをシャッフル
        random.shuffle(self.cards)
    def next_card(self):
        return self.cards.pop(0)
