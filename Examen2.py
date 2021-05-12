def problema2():
  #Definir variable y otros
  print("ingrese sus datos:")
  bonoObtenidoJMCT=0.0
  #Datos de Entrada
  salarioMinimoJMCT=float(input("Ingrese el salario:"))
  puntuacionObtenidaJMCT=float(input("Ingrese la puntuación:"))
  #Proceso
  if puntuacionObtenidaJMCT<=100 and puntuacionObtenidaJMCT>=50:
    bonoObtenidoJMCT=salarioMinimoJMCT*10/100
  elif puntuacionObtenidaJMCT >=101 and puntuacionObtenidaJMCT<=150:
    bonoObtenidoJMCT=salarioMinimoJMCT*40/100
  elif puntuacionObtenidaJMCT>=151:
    bonoObtenidoJMCT=salarioMinimoJMCT*70/100
  #Datos de salida
  print("El docente obtendra un bono de:", bonoObtenidoJMCT )

problema2()