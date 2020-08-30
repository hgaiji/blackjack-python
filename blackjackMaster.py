from person import Dealer,Player
class blackJackMaster:
    def __init__(self):
        self.player = Player('player')
        self.dealer = Dealer('Dealer')
        self.player_turn = True
    def _convert(self,cards):
        numbers = list(map(lambda x: x._convert(),cards))
        return list(map(lambda x: 10 if x > 10 else x, numbers))
    def getTotal(self,person):
        cards = self._convert(person.hands)
        return sum(cards)
    #プレイヤーの手札の合計が21を超えているかどうか
    def isBurst(self):
        card_number_sum = self.getTotal(self.player)
        print(f'プレイヤーの手札のカードの合計は{card_number_sum}です。')
        return card_number_sum > 21
    def selectDrawing(self,isDraw):
        self.player.isDraw = isDraw
    def dealerIsDraw(self):
        # ディーラーは、自分の手札が17以上になるまで引き続ける
        d_card_num_sum = self.getTotal(self.dealer)
        print(f'ディーラーの手札のカードの合計は{d_card_num_sum}です。')
        return d_card_num_sum > 17
    def isPlaying(self):
        if self.player_turn:
            isDraw = True if int(input("カードをひきますか？ 引く:0,引かない:1 →")) == 0 else False
            self.selectDrawing(isDraw)
        # 引数を受け取ってカードを引く選択をしたらisDrawをtrue
        if self.player.isDraw:
            print(f'{"="*20}プレイヤーのターン{"="*20}')
            self.player.drawCard(False)
            return False if self.isBurst() else True
        print(f'{"="*20}ディーラーのターン{"="*20}')
        self.player_turn = False
        self.dealer.drawCard(False)
        return False if self.dealerIsDraw() else True
    def subs(self,person):
        return abs(21 - self.getTotal(person))
    def battle(self):
        
        # プレイヤーとディーラーが引き終えたら勝負。より21に近い方の勝ち
        if self.isBurst():
            print(f'バースト！！')
            print(f'ディーラーの勝ち') 
            return
        print(f'バトル！')
        print(f'プレイヤーの手札合計は{self.player.hands}')
        print(f'ディーラーの手札合計は{self.dealer.hands}')
        condition = self.subs(self.dealer) - self.subs(self.player)
        print(f'{"*"*20}勝敗結果{"*"*20}')
        if condition == 0:
            print('引き分け')
        elif condition < 0:
            print('ディーラーの勝ち')
        else:
            print(f'プレイヤーの勝ち')