import threading
import os
import random 
import WConio2 as WConio2
import cursor
import interface
import time
import datetime
import pickle
import pygame
from cenario import Cenario
from carro import Carro
from frameControlador import FrameControlador



def play_music():
    pygame.init()
    pygame.mixer.music.load("TokyoDrift.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(1000)
    
def stop_music():
    pygame.mixer.music.stop()




cursor.hide()
os.system('cls')

scoresList = {}
flag = 0

while flag == 0:
    interface.menu()
    os.system('cls')
    cursor.hide()
    # RECEBE NOME DO JOGADOR
    nomeJogador = input("Digite seu nome: ").upper()
    

    #DISPARO DO TEMPO
    start = time.time()
    # INICIALIZAÇÃO DA MUSICA
    
    # INICIALIZAÇÃO DA MUSICA
    thread = threading.Thread(target=play_music)
    thread.start()

    # CARRO 
    carro = Carro()

    listaCenario = [Cenario() for _ in range(5)]

    listaCenario2 = [Cenario() for _ in range(5)]

    frame = FrameControlador()

    running = True
    paused = False

    #logica geral
    while running:
        
        WConio2.gotoxy(0,0)   
        # DIMENSÃO DA PISTA
        
        for j in range(26):   

            #Canteiro Esquerdo
            Cenario().gerarCanteiro(j, listaCenario)

            print(' ║', end='')

            Cenario().pista(j, frame.qtd)
            
            carro.geradorCarro(j)

            Cenario().pista(j, frame.qtd)
            print('║ ', end='')

            #Caneteiro Direito
            Cenario().gerarCanteiro(j, listaCenario2)
            print('')

        print('='*45)
        disparador = round(time.time()-start)

        # PONTUAÇÃO  - MULTIPLICADOR DE QUANTIDADE DE CARROS POR 50 PONTOS 
        nivel = carro.countCars // 15 +1
        actualScore = (carro.countCars *(nivel * 50))

        # DISPLAY TIMER
        hora = disparador //3600
        min =  disparador // 60
        seg = disparador % 60
        
        # CAR SPEED
        speed = round(disparador * 0.8) 
        # PAINEL            
        speedRace = 30 - (round(carro.countCars * 0.2))   

        #PAINEL

        print("Time:",(datetime.time(hora,min,seg))," Speed:", speed, "km/h   ","Score:", str(actualScore).zfill(7))
        print("Blocks Overtaking :", carro.countCars) 
        print("Nivel:", nivel)


        #Mover e Reiniciar o Cenário
        Cenario().moverObjetoCenario(frame.cont, speedRace, listaCenario)
        Cenario().moverObjetoCenario(frame.cont, speedRace, listaCenario2)
        Cenario().reiniciarObjetoCenario(listaCenario)
        Cenario().reiniciarObjetoCenario(listaCenario2)

        #controlando
        carro.controleCarro(frame, speedRace)

        def gameOver():
            fileHighscore = open('highscore.bin', 'wb')
            print('\nGAME OVER')
            
            # Verifica se o jogador já está no dicionário de scores
            if nomeJogador in scoresList:
                if actualScore > scoresList[nomeJogador]:
                    scoresList[nomeJogador] = actualScore
            else:
                scoresList[nomeJogador] = actualScore
                
            # Obtém uma lista de tuplas com as chaves e valores do dicionário
            scoresList_ordenada = scoresList.items()

            # Ordena a lista de tuplas por valores
            scoresList_ordenada = sorted(scoresList_ordenada, key=lambda x: x[1], reverse=True)

            # Obtém apenas os 5 primeiros valores    
            top_five = scoresList_ordenada[:5]    

            # Salvando no arquivo
            pickle.dump(top_five, fileHighscore)
            fileHighscore.close()
            stop_music()
            thread.join()
            
        if carro.CarroY == carro.CarroNpcY and carro.CarroX == carro.CarroNpcX:
            gameOver()   #colisão
            break

        if carro.Carro1Y == carro.CarroNpcY and carro.Carro1X == carro.CarroNpcX:        
            gameOver()  
            break

        if carro.Carro2Y == carro.CarroNpcY and carro.Carro2X == carro.CarroNpcX:   
            gameOver() 
            break

        if carro.Carro4Y == carro.CarroNpcY and carro.Carro3X == carro.CarroNpcX:    
            gameOver() 
            break

        # CONTROLE DO PERSONAGEM
        if WConio2.kbhit():
                   
            (key, symbol) = WConio2.getch()

            if symbol.upper() == 'A' or symbol == '\x4b':  
                carro.CarroX-=1
                carro.Carro1X-=1
                carro.Carro2X-=1
                carro.Carro3X-=1
                carro.Carro4X-=1
                
            if symbol.upper() == 'D' or symbol == '\x4d':   
                carro.CarroX+=1
                carro.Carro1X+=1
                carro.Carro2X+=1
                carro.Carro3X+=1
                carro.Carro4X+=1
            
            if symbol == chr(27):
                stop_music()
                thread.join()
                running = False
            
            
            
         
        frame.cont+=1
