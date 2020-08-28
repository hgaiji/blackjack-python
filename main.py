
from person import Dealer,Player
def main():

    print(f'ゲームを開始します。')
    #blackJackManagerクラス
    # プレイヤークラス→人クラスを継承したもの
    # 人クラスはカードクラスを持っている
    # ディーラークラス→人クラスを継承したもの
    player = Player('player')
    dealer = Dealer('dealer')
if __name__ == "__main__":
    main()