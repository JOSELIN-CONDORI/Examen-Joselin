def problema5():
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
  def problema4():
  #Definir variable y otros
  print("ingrese la operacion aritmeticaque desea sacar:")
  operacionaritmeticaJMCT=0
  #Datos de entrada
  problemaJMCT=int(input("ingresa la operacion aritmetica:"))
  problema1JMCT=int(input("ingresa la operacion aritmetica segunda:"))
  signoJMCT=input("ingresa la operacion que deseas hallar:")
  #proceso
  if signoJMCT=="+":
    operacionaritmeticaJMCT=problemaJMCT+problema1JMCT
  if signoJMCT=="-":
    operacionaritmeticaJMCT=problemaJMCT-problema1JMCT
  if signoJMCT=="/":
    operacionaritmeticaJMCT=problemaJMCT/problema1JMCT
  if signoJMCT=="*":
    operacionaritmeticaJMCT=problemaJMCT*problema1JMCT
  if signoJMCT=="^":
    operacionaritmeticaJMCT=problemaJMCT^problema1JMCT
  #datos de salida
  print("el resultadoo operacion es:",operacionaritmeticaJMCT)
  
#broblema1()
#problema2()
#problema3() 
problema4() 
