
class Cinta(object):
    simboloBlanco = " "

    def __init__(self, contenidoCinta=""):
        self.cinta = dict((enumerate(contenidoCinta)))  # Creando el diccionario con los contenidos de la cinta

    def __str__(self):
        s = ""  # re construccion de la cinta
        menorIndex = min(self.cinta.keys())  # menor indice
        mayorIndex = max(self.cinta.keys())  # mayor indice
        for i in range(menorIndex, mayorIndex):  # iteracion de la cinta entre ambos indices
            s += self.cinta[i]  # concatenacion de los valores entre ambos indices
        return s

    def __getitem__(self, index):
        if index in self.cinta:  # si se encuentra el indice en la cinta, entonces se regresa el elemento de la cinta en ese indice
            return self.cinta[index]
        else:
            return Cinta.simboloBlanco

    def __setitem__(self, pos, char):
        self.cinta[pos] = char  # setear un elemento de la cinta en cierto indice


class TuringMachine(object):
    def __init__(self, cinta="", simboloBlanco=" ", estadoInicial="", estadoFinal=None, funcionTransicion=None,
                 estadosError=None):  # construccion de la maquina de turing
        self.cinta = Cinta(cinta)  # construimos la cinta con el constructor declarado anteriormente
        self.posicionCabeza = 0  # en que posicion se encuentra la cabeza. Empezando por 0
        self.simboloBlanco = simboloBlanco  # definimos el simbolo en blanco
        self.estadoActual = estadoInicial  # estado Actual donde se encuentra nuestra MT

        if funcionTransicion == None:  # si no se ha definido funcion de transision
            self.transitionFunction = {}  # la definimos como vacia
        else:
            self.transitionFunction = funcionTransicion  # en caso de que si este definda en el input, entonces simplemente la asignamos.

        if estadoFinal == None:  # si el estado final no esta definido
            self.estadosFinales = set()  # lo definimos como estado final vacio
        else:
            self.estadosFinales = set(estadoFinal)  # si esta definido en el input, lo asignamos

        if estadosError == None:  # si no hay estados de error en el input
            self.estadosError = set()  # lo definimos como vacio
        else:
            self.estadosError = set(estadosError)  # si esta en el input, lo asignamos.

    def get_tape(self):
        return str(self.cinta)  # sirve para recuperar la cinta en string

    def pasoSiguiente(self):
        charUnderHead = self.cinta[
            self.posicionCabeza]  # obtenemos el siguiente simbolo dependiendo de la posicion donde se encuentra la cabeza
        x = (self.estadoActual, charUnderHead)  # obtenemos el estado actual y el simbolo y los juntamos en una pareja
        print(x)
        if x in self.transitionFunction:  # buscamos si la pareja existe en los estados de transicion
            y = self.transitionFunction[                x]  # si las encontramos, entonces actualizamos la posicion de la cabeza y es estado actual.
            self.cinta[self.posicionCabeza] = y[1]
            if y[2] == "R":
                self.posicionCabeza += 1
            elif y[2] == "L":
                self.posicionCabeza -= 1
            self.estadoActual = y[0]

    def final(self):
        if self.estadoActual in self.estadosFinales:  # si el estado actual existe en alguno de los estados finales
            return True  # entonces devolvemos que nos encontramos en estado final.
        else:
            return False

    def error(self):
        if self.estadoActual in self.estadosError:  # si el estado actual se encuentra en alguno de los estados de error
            print("Cinta en estado de error")
            return True  # regresamos que estamos en un estado de error.
        else:
            return False




def main():


    turingInput = input();
    initialState = input()
    initialState = eval(initialState)
    acceptingStates = input()
    acceptingStates = eval(acceptingStates)
    rejectingStates = input()
    rejectingStates = eval(rejectingStates)
    transitions = input()
    # TODO: Change to safer option ast.
    transitions = eval(transitions)
    t = TuringMachine(turingInput, estadoInicial=initialState, estadoFinal=acceptingStates, funcionTransicion=transitions,
                      estadosError=rejectingStates)
    print("Contenido de la cinta:\n" + t.get_tape())

    while not t.final() and not t.error():
        t.pasoSiguiente()

    print("Cinta resultante:")
    print(t.get_tape())


main()
