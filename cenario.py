import random 

class Cenario:

    #Cenario
    objeto = '█'
        
    def __init__(self):
        self.objetoX = random.randint(0,8)
        self.objetoY = random.randint(-20,0)
   

    def moverObjetoCenario(self, cont, speedRace, listaCenario):
        if cont % speedRace == 0:
            for i in listaCenario:
                i.objetoY+=1

    #Reiniciar Objeto
    def reiniciarObjetoCenario(self, listaCenario):
        for i in listaCenario:
            if i.objetoY > 24:
                if listaCenario.index(i) == 0:
                    i.objetoY= 0
                if listaCenario.index(i) == 1:
                    i.objetoY= random.randint(-15,-5)
                if listaCenario.index(i) == 2:
                    i.objetoY= random.randint(-20,-10)
                if listaCenario.index(i) == 3:
                    i.objetoY= random.randint(-25,-15)
                if listaCenario.index(i) == 4:
                    i.objetoY= random.randint(-30,-20)
                i.objetoX= random.randint(0,8)

    #Gerador da faixa lateral da pista
    def pista(self, j, qtd):
        if qtd % 2 == 0:
            if j % 2 == 0:
                print('▓', end='')
            else: 
                print(' ', end='')
        else:
            if j % 2 == 0:
                print(' ', end='')
            else: 
                print('▓', end='')    

    def gerarCanteiro(self, j, listaCenario):
        for k in range(9):
            char = '░'
            for l in listaCenario:
                if j==l.objetoY and k == l.objetoX:
                    char = self.objeto
            
            print(char, end='')