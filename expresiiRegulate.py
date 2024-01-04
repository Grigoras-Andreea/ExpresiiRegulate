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
        numar_stari = int(input("Numărul de stari: "))
        for i in range(numar_stari):
            self.Q.append(input("Stare: "))
        numar_litere = int(input("Numărul de litere: "))
        for i in range(numar_litere):
            self.E.append(input("Literă: "))
        self.q0 = input("Starea inițială: ")
        numar_stari_finale = int(input("Numărul de stări finale: "))
        for i in range(numar_stari_finale):
            self.F.append(input("Stare finală: "))
        numar_tranzitii = int(input("Numărul de tranziții: "))
        for i in range(numar_tranzitii):
            user_input = input("Introduceți tranziția: ")
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
        
    def VerifyBrackets(self):
        parenthesesStack = []
        for simbol in self.expr:
            if simbol == '(':
                parenthesesStack.append(simbol)
            elif simbol == ')':
                if not parenthesesStack:
                    return False
                if parenthesesStack[-1] == '(' or parenthesesStack[-1] == ')':
                    return False
                parenthesesStack.pop()
        if not parenthesesStack:
            return True
        return False
        
    def VerifyRegularExpression(self):
        if self.expr == "":
            return True
        if self.expr == "lambda":
            return True
        for simbol in self.expr:
            if ord(simbol) < 40 or\
               ord(simbol) > 42 and ord(simbol) < 46 or\
               ord(simbol) > 46 and ord(simbol) < 48 or\
               ord(simbol) > 57 and ord(simbol) < 65 or\
               ord(simbol) > 90 and ord(simbol) < 97 or\
               ord(simbol) > 122 and ord(simbol) < 124 or\
               ord(simbol) > 124 or\
               simbol == " ":
                return False
        return True
    
    def GetRegularExpression(self):
        return self.expr
    
    def ReversePolishNotation(self):
        RPN = []
        operatorStack = []
        operatorPriorities = {'|' : 1, '.' : 2, '*' : 3}
        for simbol in self.expr:
            if simbol.isalnum():
                RPN.append(simbol)
            else:
                if simbol == '(':
                    operatorStack.append(simbol)
                else:
                    if simbol == ')':
                        while operatorStack and operatorStack[-1] != '(':
                            RPN.append(operatorStack[-1])
                            operatorStack.pop()
                        if operatorStack:
                            operatorStack.pop()
                    else:
                        while operatorStack and operatorPriorities.get(operatorStack[-1], 0) >= operatorPriorities.get(simbol, 0):
                            RPN.append(operatorStack[-1])
                            operatorStack.pop()
                        operatorStack.append(simbol)
        while operatorStack:
            RPN.append(operatorStack[-1])
            operatorStack.pop()
        return ''.join(RPN)
    
    def RegularExpressionInAFN(self):
        RPN = self.ReversePolishNotation()
        
        return True
    
    def RegularExpressionInAFD(self):
        # Transformare expresie regulată în AFD
        # E pusă temporar ca să meargă meniul
        return True
    
def main():
    
    # TEST

    regEx = RegularExpression("")
    regEx.ReadRegularExpressionFile('regEx.txt')
    
    print(regEx.GetRegularExpression())
    print(regEx.ReversePolishNotation())

    # TEST

    '''
    regEx = RegularExpression("")
    regEx.ReadRegularExpressionFile('regEx.txt')
    
    if not regEx.VerifyRegularExpression():
        print("Expresia regulată", regEx.GetRegularExpression(), "nu este o expresie validă.")
        return
    
    print("Expresia regulată", regEx.GetRegularExpression(), "este o expresie validă.")
    M = regEx.RegularExpressionInAFD()
      
    while True:
        print("\nMeniu:")
        print("a. Afișarea automatului M atât în consolă, cât și într-un fișier de ieșire;")
        print("b. Afișarea inteligibilă a expresiei regulate r din fișier;")
        print("c. Verificare cuvânt în automat;")
        print("x. Ieșire.")
            
        optiune = input("Alegeți o opțiune: ")
            
        if optiune == 'a':
                print(M)
                
        elif optiune == 'b':
                print(regEx.GetRegularExpression())
                
        elif optiune == 'c':
            word = input("Introduceți cuvântul de verificat: ")
            if M.verifyAutomaton():
                if M.IsDeterministic():
                   if M.checkWord(word):
                       print(f"Cuvântul '{word}' este acceptat de automat.")
                   else:
                       print(f"Cuvântul '{word}' nu este acceptat de automat.")
                
        elif optiune == 'x':
            break

        else:
            print("Opțiune invalidă. Reîncercați.")
    '''
    
main()