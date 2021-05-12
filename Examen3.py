def problema3():
  #Definir variable y otros
  print("¿cual de las vacunas sera aplicado usted?:")
  vacunaaplicadaJMCT=0
  #Datos de Entrada
  añosJMCT=int(input("ingresa tu edad:"))
  #proceso
  if añosJMCT>=70:
    vacunaaplicadaJMCT="se le aplica la vacuna tipo C"
  if añosJMCT>16 and añosJMCT<=69:
     sexoJMCT=input("ingresar sexo:") 
     if sexoJMCT=="varon":
       vacunaaplicadaJMCT="se le aplica la vacuna A"
     if sexoJMCT=="mujer":
       vacunaaplicadaJMCT="se le aplica la vacuna B"
  if añosJMCT<=16:
    vacunaaplicadaJMCT="se le aplica la vacuna tipo A"
  #datos de salida
  print("A la persona:",vacunaaplicadaJMCT)

problema3()  
