
from blackjackMaster import *
def main():

    print(f'ゲームを開始します。')
    #blackJackManagerクラス
    # プレイヤークラス→人クラスを継承したもの
    # 人クラスはカードクラスを持っている
    # ディーラークラス→人クラスを継承したもの
    game = blackJackMaster()
    while(game.isPlaying()):
        print(f'{"*" * 20}playing{"*" * 20}')
    game.battle()
    print(f'ゲームを終了します。')
if __name__ == "__main__":
    main()