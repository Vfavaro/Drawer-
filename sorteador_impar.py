import random 
import time 
def desafio (): 
 
    vida=100 #quantidade de vidas 
    tentativa = 0 #tentativas do usuário 
    contador=0 #tempo de jogo 
    numero_primo = random.randint(2, 97) #Sorteador de 2 até 97 
    if (numero_primo == 2) or(numero_primo == 3)or (numero_primo == 5)or(numero_primo == 7)or(numero_primo == 11) or (numero_primo %2 !=0 ) and (numero_primo %3 !=0 ) and (numero_primo %5 !=0 ) and (numero_primo %7 !=0 ) and (numero_primo %11 !=0 ): 
        print("\n-----JOGO DA SORTE------\n" 
              "\n|A máquina escolherá um número primo de 0 a 100|\n""|Você ,jogador, tentará advinhar,caso erre, perderá vida|\n""\n|VIDA INICIAL =100|\n""|PERDE VIDA = diferença do sua aposta,com o número o da máquina|\n ") 
    else: 
        desafio() 
 
 
    while vida >=0 and tentativa<3 and contador<=10: #enquanto vida for maior ou igual a zero, tentativas menor que 3 e o contador menor que 10s 
        jogador = int(input("\nInsira sua aposta :  \n")) 
 
        if jogador > numero_primo:#para a diferença não ser número inteiro negativas 
            dif=jogador - numero_primo 
        else: 
            dif= numero_primo - jogador 
 
        vida-=dif #VIDA = VIDA - DIF 
        #condições 
        if jogador == numero_primo: 
            print("VOCÊ ACERTOU, PARABÉNS") 
            break 
        elif vida <= 0: 
            print("OPS, suas vidas acabaram GAMER OVER") 
            break 
        elif tentativa==2: 
            print("SUAS TENTATIVAS ACABARAM") 
            break 
        else: 
            print("TENTE NOVAMENTE ,vidas: ",vida) 
            tentativa += 1 
 
    #contagem iniciada após o primeiro input do usuário 
    while contador<10: 
        contador= contador+1 
        time.sleep(1) 
        if contador == 10: 
         print("SEU TEMPO ACABOU") 
         break 
 
if __name__ == "__main__": 
   desafio() 

 