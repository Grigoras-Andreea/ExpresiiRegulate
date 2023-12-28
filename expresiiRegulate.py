class DeterministicFiniteAutomaton:
    
    def __init__(self, Q: list[str], E: list[str], q0: str, F: list[str], delta: list[tuple[str]]):
        self.Q: list[str] = Q
        self.E: list[str] = E
        self.q0: str = q0
        self.F: list[str] = F
        self.delta: list[tuple[str]] = delta
        
    def ReadAutomaton(self):
        self.Q: list[str] = []
        self.E: list[str] = []
        self.F: list[str] = []
        self.delta: list[tuple[str]] = []
        numar_stari = int(input("Numarul de stari: "))
        for i in range(numar_stari):
            self.Q.append(input("Stare: "))
        numar_litere = int(input("Numarul de litere: "))
        for i in range(numar_litere):
            self.E.append(input("Litera: "))
        self.q0 = input("Starea initiala: ")
        numar_stari_finale = int(input("Numarul de stari finale: "))
        for i in range(numar_stari_finale):
            self.F.append(input("Stare finala: "))
        numar_tranzitii = int(input("Numarul de tranzitii: "))
        for i in range(numar_tranzitii):
            user_input = input("Introduceti tranzitia: ")
            stare1, aux = user_input.split(",")
            litera, stare2 = aux.split("->")
            self.delta.append((stare1, litera, stare2))

    def ReadAutomatonFile(self, file_name: str):
        self.Q: list[str] = []
        self.E: list[str] = []
        self.F: list[str] = []
        self.delta: list[tuple[str]] = []
        f = open(file_name, "r")
        Q_string: str = f.readline()
        Q_string = Q_string.replace("\n", "")
        self.Q = Q_string.split(" ")
        E_string: str = f.readline()
        E_string = E_string.replace("\n", "")
        self.E = E_string.split(" ")
        self.q0 = f.readline()
        self.q0 = self.q0.replace("\n", "")
        F_string: str = f.readline()
        F_string = F_string.replace("\n", "")
        self.F = F_string.split(" ")
        numar_tranzitii = int(f.readline())
        for i in range(numar_tranzitii):
            file_input = f.readline()
            file_input = file_input.replace("\n", "")
            stare1, aux = file_input.split(",")
            litera, stare2 = aux.split("->")
            self.delta.append((stare1, litera, stare2))
            
    def IsDeterministic(self):
        existingTransitions: list = []
        for transition in self.delta:
            aux: tuple = (transition[0],transition[1])
            if aux in existingTransitions:
                return False
            existingTransitions.append(aux)
        return True

    def VerifyAutomaton(self):
        if self.q0 not in self.Q:
            return False
        for state in self.F:
            if state not in self.Q:
                return False
        for transition in self.delta:
            if transition[0] not in self.Q:
                return False
            if transition[1] not in self.E:
                return False
            if len(transition) > 2:
                for finalState in range (2, len(transition)):
                    if transition[finalState] not in self.Q:
                        return False
        if self.IsDeterministic() == False:
            return False
        return True
    
    def PrintAutomaton(self):
        print(self.Q)
        print(self.E)
        print(self.q0)
        print(self.F)
        print(self.delta)
    
    def CheckWord(self, word):
        currentState = self.q0
        for letter in word:
            foundTransition = False
            for transition in self.delta:
                if transition[0] == currentState and transition[1] == letter:
                    currentState = transition[2]
                    foundTransition = True
                    break
            if not foundTransition:
                return False  
        return currentState in self.F
    
class RegularExpression:
    
    def __init__(self, expr: str):
        self.expr: str = expr
        
    def ReadRegularExpressionFile(self, file_name: str):
        self.expr: str = ""
        f = open(file_name, "r")
        self.expr = f.readline()
        
    def VerifyRegularExpression(self):
        if self.expr == "":
            return True
        if self.expr == "lambda":
            return True
        if len(self.expr) == 1:
            if ord(self.expr) < 40 and ord(self.expr) > 43 or\
               ord(self.expr) < 48 and ord(self.expr) > 57 or\
               ord(self.expr) < 65 and ord(self.expr) > 90 or\
               ord(self.expr) < 97 and ord(self.expr) > 122 or\
               ord(self.expr) != 124:
                return False
        return True
    
    def GetRegularExpression(self):
        return self.expr
    
def main():
    
    regEx = RegularExpression("")
    regEx.ReadRegularExpressionFile('expresieRegulata.txt')
    
    if(regEx.VerifyRegularExpression() == True):
        print("Expresia regulata", regEx.GetRegularExpression(), "este o expresie valida")
    else:
        print("Expresia regulata", regEx.GetRegularExpression(), "nu este o expresie valida")
    
main()