import faltas,golazos,timer


menu="""
Partido numero: x
1.Ingrese el nombre del equipo1:         Ingrese el nombre del equipo2:
2.Hora de inicio del partido:
3.Ingrese falta(si hubo falta):
4.Ingrese golazo:

    5.Resultados del partido:acabe el temporizador


"""
menu=int(input)

#numeral 1 
equipo1=input("Equipo local")
equipo2=input("Equipo visitante")
print(equipo1, "vs",equipo2)
#numeral 2 
timer.iniciar()

#numeral 3
falta_penalizacion=faltas.falta_penalizacion()
faltas.misconduct(falta_penalizacion)    

#numeral 4
equipo=input("Que equipo hizo el gol?: ")
if equipo=="visitante":
    golazos.gol2()
elif equipo=="local":
    golazos.gol1()
    

#numeral 5
print("marcador final:","local",golazos.gol1(),":","visitante",golazos.gol2())
print("")



