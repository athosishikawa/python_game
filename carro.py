import random 

class Carro: 

    def __init__(self):
        #Carro jogador

        self.Carro = "|█████|"
        self.CarroX = 0
        self.CarroY = 19

        self.Carro1 = "|█▄▄▄█|"
        self.Carro1X = self.CarroX
        self.Carro1Y = self.CarroY +1

        self.Carro2 = "|█████|"
        self.Carro2X = self.CarroX
        self.Carro2Y = self.CarroY+2

        self.Carro3 = "|█   █|"
        self.Carro3X = self.CarroX
        self.Carro3Y = self.CarroY+3

        self.Carro4 = "|█▄▄▄█|"
        self.Carro4X = self.CarroX
        self.Carro4Y = self.CarroY+4

        #CarroNpc
        self.CarroNpc = '■█¤█¤█■'
        self.CarroNpcX = random.randint(0,2)
        self.CarroNpcY = 0
    
        #contador de carros
        self.countCars = 0

    def geradorCarro(self, j):
        for k in range(3):
            char = '|     |'
            
            if j==self.CarroNpcY and k==self.CarroNpcX:
                char=self.CarroNpc
            if j==self.CarroY and k==self.CarroX:
                char=self.Carro
            if j==self.Carro1Y and k==self.Carro1X:
                char=self.Carro1
            if j==self.Carro2Y and k==self.Carro2X:
                char=self.Carro2
            if j==self.Carro3Y and k==self.Carro3X:
                char=self.Carro3
            if j==self.Carro4Y and k==self.Carro4X:
                char=self.Carro4

            print(char, end='')

    def controleCarro(self, frame, speedRace):
        
        #controlando
        if frame.cont % speedRace == 1:
            self.CarroNpcY+=1
            frame.qtd += 1
            
        if self.CarroNpcY > 24:
            self.countCars += 1
            self.CarroNpcY=0
            self.CarroNpcX= random.randint(0,2)
        
        #Limitar o carro na pista
        if self.CarroX > 2:
            self.CarroX-=1
            self.Carro1X -= 1
            self.Carro2X -= 1
            self.Carro3X -= 1
            self.Carro4X -= 1

        #Limitar o carro na pista
        if self.CarroX < 0:
            self.CarroX+=1
            self.Carro1X+=1
            self.Carro2X+=1
            self.Carro3X+=1
            self.Carro4X+=1

        
        