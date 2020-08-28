from card import Deck
#人クラスを定義する
# 人クラスはプレイヤークラスとディーラくらすの親クラス
class Person:
    def __init__(self,name):
        self.name = name
        #カードを持っている。→cardクラス
        self.deck = Deck()
        self.hands = []
    # カードを引く
    def drawCard(self,isOpen):
        print(f'{self.name}はカードをひきます。')
        draw_card = self.deck.next_card()
        if isOpen:
            print(f'引いたカードは{draw_card}です。') 
        self.hands.append(draw_card)

class Player(Person):
    def __init__(self, name):
        super(Player,self).__init__(name)
        for i in [True, True]:
            self.drawCard(i)
class Dealer(Person):
    def __init__(self, name):
        super(Dealer,self).__init__(name)
        for i in [True,False]:
            self.drawCard(i)