def broblema1():
  #Definir variable y otros
  print("Consulte su nota del curso de fundamentos:")
  notafinalJMCT=0
  #Datos de entrada
  primerauJMCT=int(input("Ingresa tu primera nota: "))
  segundauJMCT=int(input("Ingresa tu segunda nota: "))
  tercerauJMCT=int(input("Ingresa tu tercera nota: "))
  trabajoJMCT=int(input("Ingresa tu cuarta nota: "))
  #Proseso
  if primerauJMCT>=0 and primerauJMCT<=20:
      primerauJMCT=primerauJMCT*20/100
  if segundauJMCT>=0 and segundauJMCT<=20:
      segundauJMCT=segundauJMCT*15/100
  if tercerauJMCT>=0 and tercerauJMCT<=20:
      tercerauJMCT=tercerauJMCT*15/100
  if trabajoJMCT>=0 and trabajoJMCT<=20:
      cuartauJMCT=trabajoJMCT*50/100
  notafinalJMCT=primerauJMCT+segundauJMCT+tercerauJMCT+cuartauJMCT
  #datos de salida
  print("Su nota final es:",notafinalJMCT)

broblema1()