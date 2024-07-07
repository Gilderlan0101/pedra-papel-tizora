import random
import time

items = {
    'pedra': 'pedra',
    'papel':'papel',
    'tizora':'tizora'
}

def jogo(items):
    while True:
            for nome, objeto in items.items():
                print(f"  {objeto}")
           
            escolhar = str(input('Escolha um item para jogar.'))
            if escolhar in items:
              
              heroi = items[escolhar]
              print('Voce escolheu: ' , heroi)
            if not escolhar:
              print('arma escolhida não esta presente...')
              continue

            inimigo_key = random.choice(list(items.keys()))
            inimigo = items[inimigo_key]
           

            time.sleep(1)
            print('pedra')
            time.sleep(1)
            print('papel')
            time.sleep(1)
            print('tizora')


            if inimigo ==  heroi:
                print('Empate --')

            

            elif (heroi == 'pedra' and inimigo == 'tizora') or (heroi == 'papel' and inimigo == 'pedra') or (heroi == 'tizora' and inimigo == 'papel'):
                print(f'{heroi} X {inimigo} - VOCE VENCEU')

            else:
                print(f'{heroi} X {inimigo} - VOCE PERDEU KKKKKKK ANIMAL ')

            

            
        
    

jogo(items)