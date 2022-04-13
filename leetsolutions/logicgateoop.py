"""
build logic gate classes, each and,or,not gate can have a connector to the next gate
# >>> g1 = AndGate("G1")
# >>> g2 = AndGate("G2")
# >>> g3 = OrGate("G3")
# >>> g4 = NotGate("G4")
# >>> c1 = Connector(g1,g3)
# >>> c2 = Connector(g2,g3)
# >>> c3 = Connector(g3,g4)
"""

class LogicGate:

    def __init__(self,n):
        self.label = n
        self.output = None

    def getlabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output



class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return input("Enter Pin A input for gate " + self.getLabel() + "-->")
        else:
            return self.pinA.getFrom().getOutput()
    def getPinB(self):
        return int(input("Enter Pin B input for gate "+ self.getlabel()+"-->"))

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot compute a doot")

class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate " + self.getlabel() + "-->"))


class AndGate(BinaryGate):

    def __init__(self,n):
        super(AndGate, self).__init__(n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):

    def __init__(self, n):
        super(OrGate, self).__init__(n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self .getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class NotGate(UnaryGate):

    def __init__(self):
        super(NotGate, self).__init__(n)

    def performGateLogic(self):
        pinin = self.getPin()

        if pinin == 0:
            return 1
        else:
            return 0

class NandGate(AndGate):

    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1

class NorGate(OrGate):

    def performGateLogic(self):
        if self.performGateLogic() == 1:
            return 0
        else:
            return 1

class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


def main():
    print()
#make some gates and connectors here
#print them

main()
