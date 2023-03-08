from abc import ABC, abstractmethod
import random
lenguajeSetA=set()
lenguajeSetB=set()
class receptor:
    def union(self, a: set, b: set):
        resultado=a.union(b)
        if len(resultado)==0:
            print("{}\n")
        else:
            print(resultado,"\n")
    def diferencia(self, a: set, b: set):
        resultado=a.difference(b)
        if len(resultado)==0:
            print("{}\n")
        else:
            print(resultado,"\n")
    def interseccion(self, a: set, b: set):
        resultado=a.intersection(b)
        if len(resultado)==0:
            print("{}\n")
        else:
            print(resultado,"\n")
    def cerraduraEstrella(self, a:list, cant: int, nombre: str):
        cerradura=set()
        simboloA=""
        simboloB=""
        simboloNuevo=""
        while len(cerradura)<cant:
            simboloA=random.choice(a)
            simboloB=random.choice(a)
            simboloNuevo=simboloA+simboloB
            if simboloNuevo.count("#")==len(simboloNuevo):
                simboloNuevo="#"
            else:
                simboloNuevo=simboloNuevo.replace("#","")
            cerradura.add(simboloNuevo)
        print(cerradura,"\n")
        if nombre=="A":
            lenguajeSetA.update(cerradura)
        if nombre=="B":
            lenguajeSetB.update(cerradura)
    def concatenacion(self, a: list, b: list):
        lenguajeConcat=set()
        palabraA=""
        palabraB=""
        palabraNueva=""
        nLenA=len(a)
        nLenB=len(b)
        cant=nLenA*nLenB
        i=0
        j=0
        if nLenA==0 or nLenB==0:
            print("{}\n")
        else:
            while len(lenguajeConcat)<cant:
                if j<nLenB:
                    palabraA=a[i]
                    palabraB=b[j]
                    palabraNueva=palabraA+palabraB
                    if palabraNueva.count("#")==len(palabraNueva):
                        palabraNueva="#"
                    else:
                        palabraNueva=palabraNueva.replace("#","")
                    lenguajeConcat.add(palabraNueva)
                    j=j+1
                else:
                    i=i+1
                    j=0
            print(lenguajeConcat,"\n")

    def potencia(self,a: list, exp: int):
        potencia=set()
        potenciaArray=[]
        palabraA=""
        palabraB=""
        palabraNueva=""
        i=0
        j=0
        nVeces=1
        concActual=0
        conjActual=a
        while nVeces<exp:
            if j<len(a):
                if concActual==1:
                    conjActual=list(potenciaArray)
                    concActual=0
                if exp>2 and nVeces>=2:
                    palabraA=conjActual[i]
                else:
                    palabraA=a[i]
                palabraB=a[j]
                palabraNueva=palabraA+palabraB
                if palabraNueva.count("#")==len(palabraNueva):
                    palabraNueva="#"
                else:
                    palabraNueva=palabraNueva.replace("#","")
                potencia.add(palabraNueva)
                potenciaArray.append(palabraNueva)
                j=j+1
            else:
                if i==len(conjActual)-1 and j==len(a):
                    nVeces=nVeces+1
                    i=-1
                    concActual=1
                i=i+1
                j=0
        if exp==1:
            potencia=set(a)
        print(potencia,"\n")    
    def inversa(self, a:list):
        palabraInvertida=""
        lengueajeInverso=set()
        for x in a:
            for letra in x:
                palabraInvertida=letra+palabraInvertida
            lengueajeInverso.add(palabraInvertida)
            palabraInvertida=""
        print(lengueajeInverso,"\n") 
    def cardinal(self, a:set):
        cant=len(a)
        print(cant,"\n")
class interfazComando(ABC):
    @abstractmethod
    def ejecutar(self):
        pass
class comandoUnion(interfazComando):
    def __init__(self, Receptor: receptor, a: set, b: set):
        self._receptor = Receptor
        self._a = a
        self._b = b
    def ejecutar(self):
        print("\nresultado de la union de alfabetos:")
        self._receptor.union(self._a,self._b)
class comandoUnionLenguajes(interfazComando):
    def __init__(self, Receptor: receptor, a: set, b: set):
        self._receptor = Receptor
        self._a = a
        self._b = b
    def ejecutar(self):
        print("\nresultado de la union de lenguajes:")
        self._receptor.union(self._a,self._b)
class comandoDiferencia(interfazComando):
    def __init__(self, receptor: receptor, a: set, b: set):
        self._receptor = receptor
        self._a = a
        self._b = b
    def ejecutar(self):
        print("\nresultado de la diferencia de alfabetos:")
        self._receptor.diferencia(self._a,self._b)
class comandoDiferenciaLenguajes(interfazComando):
    def __init__(self, receptor: receptor, a: set, b: set):
        self._receptor = receptor
        self._a = a
        self._b = b
    def ejecutar(self):
        print("\nresultado de la diferencia de lenguajes:")
        self._receptor.diferencia(self._a,self._b)
class comandoInterseccion(interfazComando):
    def __init__(self, Receptor: receptor, a: set, b: set):
        self._receptor = Receptor
        self._a = a
        self._b = b
    def ejecutar(self):
        print("\nresultado de la interseccion de alfabetos:")
        self._receptor.interseccion(self._a,self._b)
class comandoInterseccionLenguajes(interfazComando):
    def __init__(self, Receptor: receptor, a: set, b: set):
        self._receptor = Receptor
        self._a = a
        self._b = b
    def ejecutar(self):
        print("\nresultado de la interseccion de lenguajes:")
        self._receptor.interseccion(self._a,self._b)
class comandoCerraduraEstrella(interfazComando):
    def __init__(self, Receptor: receptor, a: list, nombre: str, cant: int):
        self._receptor = Receptor
        self._a = a
        self._nombre = nombre
        self._cant = cant
    def ejecutar(self):
        print("\nresultado de la cerradura estrella del alfabeto",self._nombre,":")
        self._receptor.cerraduraEstrella(self._a,self._cant,"")
class comandoCreacionLenguaje(interfazComando):
    def __init__(self, Receptor: receptor, a: list, nombre: str, cant: int):
        self._receptor = Receptor
        self._a = a
        self._nombre = nombre
        self._cant = cant
    def ejecutar(self):
        print("\nlenguaje",self._nombre,":")
        self._receptor.cerraduraEstrella(self._a,self._cant,self._nombre)
class comandoConcatenacion(interfazComando):
    def __init__(self, Receptor: receptor, a: list, b: list):
        self._receptor = Receptor
        self._a = a
        self._b = b
    def ejecutar(self):
        print("\nresultado de la concatenacion de lenguajes:")
        self._receptor.concatenacion(self._a,self._b)
class comandoPotencia(interfazComando):
    def __init__(self, Receptor: receptor, a: list, nombre: str, exp: int):
        self._receptor = Receptor
        self._a = a
        self._nombre = nombre
        self._exp = exp
    def ejecutar(self):
        print("\nresultado de la potencial del lenguaje",self._nombre,":")
        self._receptor.potencia(self._a,self._exp)
class comandoInversa(interfazComando):
    def __init__(self, Receptor: receptor, a: list, nombre: str):
        self._receptor = Receptor
        self._a = a
        self._nombre = nombre
    def ejecutar(self):
        print("\nresultado del inverso del lenguaje",self._nombre,":")
        self._receptor.inversa(self._a)
class comandoCardinalidad(interfazComando):
    def __init__(self, Receptor: receptor, a: set, nombre: str):
        self._receptor = Receptor
        self._a = a
        self._nombre = nombre
    def ejecutar(self):
        print("\nresultado de la cardinal del lenguaje",self._nombre,":")
        self._receptor.cardinal(self._a)
class invocadora:
    def comandoInicio(self, comando: interfazComando):
        self._comandoInicio=comando
    def comandoEjecucion(self):
        if isinstance(self._comandoInicio,interfazComando):
            self._comandoInicio.ejecutar()
print('''bienvenido usuario, a continuacion ingrese los simbolos de los alfabetos
(recuerde que el '#' sera el lambda o palabra vacia) y los simbolos 
del lenguaje se separan por coma(,).\n ''')
erroresEncontrados=True
alfabeto1=""
alfabeto2=""
elementoFinal=""
elementoInicial=""
while erroresEncontrados:
    alfabeto1=input("usuario, por favor digite el primer alfabeto:")
    if len(alfabeto1)==0 or alfabeto1.isspace():
        alfabeto1=""
        break
    elif alfabeto1.isspace()!=True or len(alfabeto1)!=0:
        elementoFinal=alfabeto1[len(alfabeto1)-1]
        elementoInicial=alfabeto1[0]
        break
    if alfabeto1.find(",,")!=-1 or elementoFinal=="," or elementoInicial=="," or alfabeto1.find(" ")!=-1:
        print("\n|--error: se ha encontrado un espacio vacio o un simbolo del alfabeto 1 es un espacio vacio--|.\n")
    elif alfabeto1.find(",,")==-1 and elementoFinal!="," and elementoInicial!="," and alfabeto1.find(" ")==-1:
        erroresEncontrados=False
erroresEncontrados=True
elementoFinal=""
elementoInicial=""
while erroresEncontrados:    
    alfabeto2=input("usuario, por favor digite el segundo alfabeto:")
    if len(alfabeto2)==0 or alfabeto2.isspace():
        alfabeto2=""
        break
    elif alfabeto2.isspace()!=True or len(alfabeto2)!=0:
        elementoFinal=alfabeto2[len(alfabeto2)-1]
        elementoInicial=alfabeto2[0]
    if alfabeto2.find(",,")!=-1 or elementoFinal=="," or elementoInicial=="," or alfabeto2.find(" ")!=-1:
        print("\n|--error: se ha encontrado un espacio vacio o un simbolo del alfabeto 2 es un espacio vacio--|.\n")
    elif alfabeto2.find(",,")==-1 and elementoFinal!="," and elementoInicial!="," and alfabeto2.find(" ")==-1:
        erroresEncontrados=False
indexComa1=0
indexComa2=0
aux1=0
aux2=0
alfabetoSet1=set()
alfabetoSet2=set()
alfabetoArray1=[]
alfabetoArray2=[]
simbolo1=""
simbolo2=""
while indexComa1!=-1 or indexComa2!=-1:
    if indexComa1==0 or indexComa2==0:
        if alfabeto1=="":
            alfabetoArray1.append("")
            indexComa1=-1
        else:
            indexComa1=alfabeto1.find(",")
            aux1=indexComa1
            if indexComa1==-1:
                simbolo1=alfabeto1
            else:
                simbolo1=alfabeto1[0:indexComa1]
            if simbolo1.count("#")==len(simbolo1):
                simbolo1="#"
            else:
                simbolo1=simbolo1.replace("#","")
            alfabetoSet1.add(simbolo1)
            alfabetoArray1.append(simbolo1)            
        if alfabeto2=="":
            alfabetoArray2.append("")
            indexComa2=-1
        else:
            indexComa2=alfabeto2.find(",")
            aux2=indexComa2
            if indexComa2==-1:
                simbolo2=alfabeto2
            else:
                simbolo2=alfabeto2[0:indexComa2]
            if simbolo2.count("#")==len(simbolo2):
                simbolo2="#"
            else:
                simbolo2=simbolo2.replace("#","")
            alfabetoSet2.add(simbolo2)
            alfabetoArray2.append(simbolo2)
    else:
        if alfabeto1!="":
            indexComa1=alfabeto1.find(",",aux1+1) 
            if indexComa1==-1:
                simbolo1=alfabeto1[aux1+1:]
            else:
                simbolo1=alfabeto1[aux1+1:indexComa1]
            if simbolo1.count("#")==len(simbolo1):
                simbolo1="#"
            else:
                simbolo1=simbolo1.replace("#","")
            alfabetoSet1.add(simbolo1)
            alfabetoArray1.append(simbolo1)
            aux1=indexComa1
        if alfabeto2!="":
            indexComa2=alfabeto2.find(",",aux2+1) 
            if indexComa2==-1:
                simbolo2=alfabeto2[aux2+1:]
            else:
                simbolo2=alfabeto2[aux2+1:indexComa2]
            if simbolo2.count("#")==len(simbolo2):
                simbolo2="#"
            else:
                simbolo2=simbolo2.replace("#","")
            alfabetoSet2.add(simbolo2)
            alfabetoArray2.append(simbolo2)
            aux2=indexComa2
print("\nestos son los alfabetos:\n")
if alfabeto1=="":
    print("alfabeto A: {}\n")
else:
    print("alfabeto A:",alfabetoSet1,"\n")
if alfabeto2=="":
    print("alfabeto B: {}\n")    
else:
    print("alfabeto B:",alfabetoSet2,"\n")
opcion=0
solicitud=invocadora()
operacion=receptor()
nPalabrasLengA=""
nPalabrasLengB=""
programaIniciado=True
lenguajeArrayA=[]
lenguajeArrayB=[]
while programaIniciado:
    while opcion==0:
        opcion=input('''este es el menu del alfabeto.
    1) realizar la unión de alfabetos.
    2) realizar la diferencia entre alfabetos (A-B).
    3) realizar la intersección entre alfabetos.
    4) realizar la cerradura de estrella de los alfabetos.
    5) pasar al menu de lenguajes (cuando se pase al menu debera generar nuevos lenguajes)
    6) salir
    ingrese una opcion:''')
        if opcion.isdigit():
            opcion=int(opcion)
        if opcion==1:
            solicitud.comandoInicio(comandoUnion(operacion,alfabetoSet1,alfabetoSet2))
            solicitud.comandoEjecucion()
            opcion=0
        elif opcion==2:
            if(alfabeto1==""):
                print("\n|--error: el alfabeto A esta vacio, no se puede aplicar la diferencia--|.\n")
            else:            
                solicitud.comandoInicio(comandoDiferencia(operacion,alfabetoSet1,alfabetoSet2))
                solicitud.comandoEjecucion()
            opcion=0
        elif opcion==3:
            solicitud.comandoInicio(comandoInterseccion(operacion,alfabetoSet1,alfabetoSet2))
            solicitud.comandoEjecucion()
            opcion=0
        elif opcion==4:
            nombre=input("\nelija el alfabeto al que le desea realizar cerradura estrella (digite a o b):")
            nombre=nombre.upper()
            if alfabeto1=="" and nombre=="A":
                print("\n|--error: el alfabeto A es un conjunto vacio--|.\n")
                opcion=0
            if alfabeto2=="" and nombre=="B":
                print("\n|--error: el alfabeto B es un conjunto vacio--|.\n")
                opcion=0
            if nombre!="A" and nombre!="B":
                print("\n|--error: no ha ingresado un alfabeto valido--|.\n")
                opcion=0
            else:
                if alfabeto1!="" and nombre=="A":
                    cant=input("\ndigite la cantidad de palabras que tendra la cerradura de estrella:")
                    if cant.isdigit()!=True:
                        print("\n|--error: no ha ingresado un numero valido para la cantidad de palabras--|.\n")
                        opcion=0
                    else:
                        cant=int(cant)
                        if nombre=="A":
                            solicitud.comandoInicio(comandoCerraduraEstrella(operacion,alfabetoArray1,nombre,cant))
                        solicitud.comandoEjecucion()
                        opcion=0
                if alfabeto2!="" and nombre=="B":
                    cant=input("\ndigite la cantidad de palabras que tendra la cerradura de estrella:")
                    if cant.isdigit()!=True:
                        print("\n|--error: no ha ingresado un numero valido para la cantidad de palabras--|.\n")
                        opcion=0
                    else:
                        cant=int(cant)
                        if nombre=="B":
                            solicitud.comandoInicio(comandoCerraduraEstrella(operacion,alfabetoArray2,nombre,cant))
                        solicitud.comandoEjecucion()
                        opcion=0
        elif opcion==5:
            if alfabeto1!="":
                nPalabrasLengA=input("\ningrese el numero de palabras que tendra el lenguaje A:")
                if nPalabrasLengA.isdigit()!=True:
                    print("\n|--error: no ha ingresado un numero valido para la cantidad de palabras--|.\n")
                    opcion=0
                else:
                    cantA=int(nPalabrasLengA)
                    solicitud.comandoInicio(comandoCreacionLenguaje(operacion,alfabetoArray1,"A",cantA))
                    solicitud.comandoEjecucion()
                    lenguajeArrayA=list(lenguajeSetA)
                    if alfabeto2=="":
                        print("\nlenguaje B:")
                        print("{}\n") 
            if alfabeto2!="":
                nPalabrasLengB=input("\ningrese el numero de palabras que tendra el lenguaje B:")
                if nPalabrasLengB.isdigit()!=True:
                    print("\n|--error: no ha ingresado un numero valido para la cantidad de palabras--|.\n")
                    opcion=0
                else:
                    if alfabeto1=="":
                        print("\nlenguaje A:")
                        print("{}\n")
                    cantB=int(nPalabrasLengB)
                    solicitud.comandoInicio(comandoCreacionLenguaje(operacion,alfabetoArray2,"B",cantB))
                    solicitud.comandoEjecucion()
                    lenguajeArrayB=list(lenguajeSetB)
          
            if alfabeto1=="" and alfabeto2=="":
                print("\n|--error: ambos alfabetos son conjuntos vacios--|.\n")
                opcion=0
            else:
                opcion=5
        elif opcion==6:
            programaIniciado=False
        else:
            print("\n|--error: no ha ingresado una opcion valida--|.\n")
            opcion=0
    while opcion==5:
        opcion=input('''este es el menu del lenguaje.
    1) realizar la unión de lenguajes.
    2) realizar la diferencia entre lenguajes (A-B).
    3) realizar la intersección entre lenguajes.
    4) realizar la concatenación entre lenguajes.
    5) realizar la potencia de un lenguaje.
    6) realizar la inversa de un lenguaje.
    7) realizar la cardinalidad de un lenguaje.
    8) pasar al menu de alfabeto
    9) salir
    ingrese una opcion:''')
        if opcion.isdigit():
            opcion=int(opcion)
        if opcion==1:
            solicitud.comandoInicio(comandoUnionLenguajes(operacion,lenguajeSetA,lenguajeSetB))
            solicitud.comandoEjecucion()
            opcion=5
        elif opcion==2:
            if(alfabeto1==""):
                print("\n|--error: el lenguaje A esta vacio, no se puede aplicar la diferencia--|.\n")
            else:
                solicitud.comandoInicio(comandoDiferenciaLenguajes(operacion,lenguajeSetA,lenguajeSetB))
                solicitud.comandoEjecucion()
            opcion=5
        elif opcion==3:
            solicitud.comandoInicio(comandoInterseccionLenguajes(operacion,lenguajeSetA,lenguajeSetB))
            solicitud.comandoEjecucion()
            opcion=5
        elif opcion==4:
            solicitud.comandoInicio(comandoConcatenacion(operacion,lenguajeArrayA,lenguajeArrayB))
            solicitud.comandoEjecucion()
            opcion=5
        elif opcion==5:
            nombre=input("\nelija el lenguaje al que le desea realizar la potencia (digite a o b):")
            nombre=nombre.upper()
            if nombre!="A" and nombre!="B":
                print("\n|--error: no ha ingresado un lenguaje valido--|.\n")
            else:
                if nombre=="A" and len(lenguajeArrayA)==0:
                    print("\n|--error: el lenguaje A es un conjunto vacio--|.\n")
                elif nombre=="A" and len(lenguajeArrayA)!=0:
                    exp=input("\ndigite el exponente que tendra la potencia:")
                    if exp.isdigit()!=True:
                        print("\n|--error: no ha ingresado un numero valido para el exponente--|.\n")
                    else:
                        exp=int(exp)
                        solicitud.comandoInicio(comandoPotencia(operacion,lenguajeArrayA,nombre,exp))
                        solicitud.comandoEjecucion()
                if nombre=="B" and len(lenguajeArrayB)==0:
                    print("\n|--error: el lenguaje B es un conjunto vacio--|.\n")
                elif nombre=="B" and len(lenguajeArrayB)!=0:
                    exp=input("\ndigite el exponente que tendra la potencia:")
                    if exp.isdigit()!=True:
                        print("\n|--error: no ha ingresado un numero valido para el exponente--|.\n")
                    else:
                        exp=int(exp)
                        solicitud.comandoInicio(comandoPotencia(operacion,lenguajeArrayB,nombre,exp))
                        solicitud.comandoEjecucion()
            opcion=5
        elif opcion==6:
            nombre=input("\nelija el lenguaje al que le desea realizar la inversa (digite a o b):")
            nombre=nombre.upper()
            if nombre!="A" and nombre!="B":
                print("\n|--error: no ha ingresado un lenguaje valido--|.\n")
            else:
                if nombre=="A" and len(lenguajeArrayA)==0:
                    print("\n|--error: el lenguaje A es un conjunto vacio--|.\n")
                elif nombre=="A" and len(lenguajeArrayA)!=0:
                        solicitud.comandoInicio(comandoInversa(operacion,lenguajeArrayA,nombre))
                        solicitud.comandoEjecucion()
                if nombre=="B" and len(lenguajeArrayB)==0:
                    print("\n|--error: el lenguaje B es un conjunto vacio--|.\n")
                elif nombre=="B" and len(lenguajeArrayB)!=0:
                        solicitud.comandoInicio(comandoInversa(operacion,lenguajeArrayB,nombre))
                        solicitud.comandoEjecucion()
            opcion=5
        elif opcion==7:
            nombre=input("\nelija el lenguaje al que le desea calcular la cardinalidad (digite a o b):")
            nombre=nombre.upper()
            if nombre!="A" and nombre!="B":
                print("\n|--error: no ha ingresado un lenguaje valido--|.\n")
            else:
                if nombre=="A":
                    solicitud.comandoInicio(comandoCardinalidad(operacion,lenguajeSetA,nombre))
                elif nombre=="B":
                    solicitud.comandoInicio(comandoCardinalidad(operacion,lenguajeSetB,nombre))
                solicitud.comandoEjecucion()
            opcion=5
        elif opcion==8:
            lenguajeSetA.clear()
            lenguajeSetB.clear()
            opcion=0
        elif opcion==9:
            programaIniciado=False
        else:
            print("\n|--error: no ha ingresado una opcion valida--|.\n")
            opcion=5
    
    
    
        