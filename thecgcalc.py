from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from PyQt5 import uic #turns a ui file into python
import math

#Widget class
class Calculator(QtWidgets.QWidget): #This will need to change based on the class used in the XML file
    def __init__(self):
        super(Calculator, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('thecgcalc.ui',self) #Load the ui file
        self.show()
        
        #number button handling (calls methods when the buttons are pressed)
        self.oneButton.clicked.connect(lambda: self.addCharacter(1))
        self.twoButton.clicked.connect(lambda: self.addCharacter(2))
        self.threeButton.clicked.connect(lambda: self.addCharacter(3))
        self.fourButton.clicked.connect(lambda: self.addCharacter(4))
        self.fiveButton.clicked.connect(lambda: self.addCharacter(5))
        self.sixButton.clicked.connect(lambda: self.addCharacter(6))
        self.sevenButton.clicked.connect(lambda: self.addCharacter(7))
        self.eightButton.clicked.connect(lambda: self.addCharacter(8))
        self.nineButton.clicked.connect(lambda: self.addCharacter(9))
        self.zeroButton.clicked.connect(lambda: self.addCharacter(0))

        self.decimalButton.clicked.connect(lambda: self.addCharacter("."))
        self.signButton.clicked.connect(lambda: self.addCharacter("-"))
        self.openBracketButton.clicked.connect(lambda: self.addCharacter("("))
        self.closeBracketButton.clicked.connect(lambda: self.addCharacter(")"))
        
        self.answer = None
        
        #function button handling
        self.addButton.clicked.connect(lambda: self.addCharacter("+"))
        self.minusButton.clicked.connect(lambda: self.addCharacter("-"))
        self.multButton.clicked.connect(lambda: self.addCharacter("*"))
        self.divButton.clicked.connect(lambda: self.addCharacter("/"))

        self.ansButton.clicked.connect(self.ansButtonMethod)
        self.logButton.clicked.connect(self.logButtonMethod)
        self.sqrtButton.clicked.connect(self.sqrtButtonMethod)
        self.expButton.clicked.connect(self.expButtonMethod)
        self.squareButton.clicked.connect(self.squareButtonMethod)
        self.sinButton.clicked.connect(self.sinButtonMethod)
        self.cosButton.clicked.connect(self.cosButtonMethod)
        self.tanButton.clicked.connect(self.tanButtonMethod)
        
        self.ACButton.clicked.connect(self.ACButtonMethod)
        self.equalsButton.clicked.connect(self.equalsButtonMethod)

        #del button
        self.delButton.clicked.connect(self.delButtonMethod)
        
    def addCharacter(self, pressed):
        if len(self.lblDisplay.text()) < 25:
            self.lblDisplay.setText(self.lblDisplay.text() + str(pressed))  

    #delete button method - deletes the last char of the string in the display
    def delButtonMethod(self):
        if self.lblDisplay.text() == "":
            pass
        else:
            self.lblDisplay.setText(self.lblDisplay.text()[0:-1])

    #ac method - clears display and removes stored answers
    def ACButtonMethod(self):
        self.lblDisplay.setText("")
        self.answer = None

    #special function buttons - straight away gives the answer of the number in the display
    def logButtonMethod(self):
        self.equalsButtonMethod()
        try:
            self.answer = math.log(self.answer)
            self.lblDisplay.setText(str(self.answer))
        except ValueError:
            self.answer = 0
            self.lblDisplay.setText("Error")

    def sqrtButtonMethod(self):
        try:
            self.answer = math.sqrt(self.answer)
            self.lblDisplay.setText(str(self.answer))
        except:
            self.answer = 0
            self.lblDisplay.setText("Error")
    
    def expButtonMethod(self):
        self.equalsButtonMethod()
        try:
            self.answer =  math.exp(self.answer)
        except OverflowError:
            self.lblDisplay.setText('Error')
            self.answer = 0
        self.lblDisplay.setText(str(self.answer))

    def squareButtonMethod(self):
        self.equalsButtonMethod()
        try:
            self.answer =  self.answer ** 2
        except OverflowError:
            self.lblDisplay.setText('Error')
            self.answer = 0
        self.lblDisplay.setText(str(self.answer))
        
    def sinButtonMethod(self):
        self.equalsButtonMethod()
        self.answer = math.sin(math.radians(self.answer))
        self.lblDisplay.setText(str(self.answer))
    def cosButtonMethod(self):
        self.equalsButtonMethod()
        self.answer = math.cos(math.radians(self.answer))
        self.lblDisplay.setText(str(self.answer))
    def tanButtonMethod(self):
        self.equalsButtonMethod()
        self.answer = math.tan(math.radians(self.answer))
        self.lblDisplay.setText(str(self.answer))

    #ans button - adds the most recent answer to the display
    def ansButtonMethod(self):
        if self.answer != None:
            self.lblDisplay.setText(self.lblDisplay.text() + str(self.answer))
            
    #equals button - takes the second number in the display and completes the operation with the first number based on the current active button
    def equalsButtonMethod(self):
        try:
            self.answer = eval(self.lblDisplay.text())
            self.lblDisplay.setText(str(self.answer))
        except:
            self.answer = None
            self.lblDisplay.setText("")
        
        
def calcMain():
    app = QtWidgets.QApplication(sys.argv)
    window = Calculator()
    app.exec()
    
calcMain()
