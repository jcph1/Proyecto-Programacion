falta_menor=["intento ataque", "broken stick", "charging", "boarding", "cross checking", "delaying", "elbowing", " falling on the puck","handpass", "high sticks", "holding", "hoocking","interference","slashing","tripping" ]
falta_mayor=["fighting","interference by spectators", "checking from behind", 'leaving penalty bench', "abuse of officials", "profane language", ]
jugador_1= int(input("Ingrese el numero de jersey del jugador: "))


def falta_penalizacion():
    x=input("Ingrese el nombre de la falta: ")
    falta=0

    if x in falta_menor:
        print("Debe permanecer durante 2 minutos en el penalty box")
        falta+=1
        
    elif x in falta_mayor:
        print("Debe permanecer durante 10 minutos en el penalty box")
        falta+=3
        
    elif x not in falta_menor or x not in falta_mayor:
        print("la falta no existe o esta escrita de forma incorrecta")
    
    return falta


def misconduct(falta_penalizacion):
    
    if falta_penalizacion < 2:
        print("el jugador no esta en riesgo de misconduct")    
    else:
        print("se debe de expulsar al jugador del partido")
 
        
falta_penalizacion()
misconduct(falta_penalizacion())    