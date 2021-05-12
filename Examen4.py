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
  
problema4()