from tkinter import *


class App(Frame):
    '''Aplikacja kalkulatora '''
    def __init__(self,master):
        super(App,self).__init__(master)

        self.rememberNumber = []
        self.holdNumbersForOperation = []


        self.displayLbl = Label(text="0",width="40",height="5")   
        self.displayLbl.grid(row=1,column=1,columnspan=4)

        self.butt1 = Button(text="1",width="10",height="5",command=self.display1,bg="magenta",font=5)
        self.butt1.grid(row=2,column=1)

        self.butt2 = Button(text="2",width="10",height="5",command=self.display2,bg="magenta",font=5)
        self.butt2.grid(row=2,column=2)

        self.butt3 = Button(text="3",width="10",height="5",command=self.display3,bg="magenta",font=5)
        self.butt3.grid(row=2,column=3)

        self.butt4 = Button(text="4",width="10",height="5",command=self.display4,bg="magenta",font=5)
        self.butt4.grid(row=3,column=1)

        self.butt5 = Button(text="5",width="10",height="5",command=self.display5,bg="magenta",font=5)
        self.butt5.grid(row=3,column=2)

        self.butt6 = Button(text="6",width="10",height="5",command=self.display6,bg="magenta",font=5)
        self.butt6.grid(row=3,column=3)

        self.butt7 = Button(text="7",width="10",height="5",command=self.display7,bg="magenta",font=5)
        self.butt7.grid(row=4,column=1)

        self.butt8 = Button(text="8",width="10",height="5",command=self.display8,bg="magenta",font=5)
        self.butt8.grid(row=4,column=2)

        self.butt9 = Button(text="9",width="10",height="5",command=self.display9,bg="magenta",font=5)
        self.butt9.grid(row=4,column=3)

        self.butt0 = Button(text="0",width="10",height="5",command=self.display0,bg="magenta",font=5)
        self.butt0.grid(row=5,column=1)

        self.buttEqual  = Button(text="=",width="10",height="5",bg="magenta",font=5,command=self.numberEquals)#
        self.buttEqual.grid(row=5,column=2)

        self.buttClear = Button(text="C",width="10",height="5",bg="magenta",font=5,command=self.clearScrean)
        self.buttClear.grid(row=5,column=3)

        self.buttMinus = Button(text="-",width="10",height="11",bg="magenta",font=5,command=self.numberMinus)
        self.buttMinus.grid(row=2,column=4,rowspan=2)

        self.buttPlus = Button(text="+",width="10",height="11",bg="magenta",font=5,command=self.numberPlus)
        self.buttPlus.grid(row=4,column=4,rowspan=2)

        #self.buttHelp = Button(text='pomoc',width="10",height="5")#,command=self.goToHelp
        #self.buttHelp.grid()  
        
    def display1(self):
        click = 1
        self.addNumberToDisplay(number = click)

    def display2(self):
        click = 2
        self.addNumberToDisplay(number = click)

    def display3(self):
        click = 3
        self.addNumberToDisplay(number = click)

    def display4(self):
        click = 4
        self.addNumberToDisplay(number = click)

    def display5(self):
        click = 5
        self.addNumberToDisplay(number = click)

    def display6(self):
        click = 6
        self.addNumberToDisplay(number = click)

    def display7(self):
        click = 7
        self.addNumberToDisplay(number = click)

    def display8(self):
        click = 8
        self.addNumberToDisplay(number = click)

    def display9(self):
        click = 9
        self.addNumberToDisplay(number = click)

    def display0(self):
        click = 0
        self.addNumberToDisplay(number = click)

    def numberPlus(self):
        addNumber = 0
        makeNumber = 0
        holdNumber = 0
        multiplier = 1
        for i in self.rememberNumber:
            holdNumber = i
            makeNumber = (makeNumber*10) + holdNumber
            multiplier *= 10   
        self.holdNumbersForOperation.append(makeNumber)
        self.rememberNumber = []
        print('Dodawane liczby :')
        print(self.holdNumbersForOperation)
        
        for i in self.holdNumbersForOperation:
            addNumber += i
        print(addNumber)

        #self.addNumberToDisplay(number=addNumber)

    def numberMinus(self):
        addNumber = 0
        makeNumber = 0
        holdNumber = 0
        multiplier = 1
        for i in self.rememberNumber:
            holdNumber = i
            makeNumber = (makeNumber*10) + holdNumber
            multiplier *= 10   
        self.holdNumbersForOperation.append(-makeNumber)
        self.rememberNumber = []
        print('Dodawane liczby :')
        print(self.holdNumbersForOperation)
        
        for i in self.holdNumbersForOperation:
            addNumber += i
        print(addNumber)    

        #self.addNumberToDisplay(number=addNumber)
        
    def addNumberToDisplay(self,number):
        '''funkcja do wyświetlania numerów'''
        printNumber = 0
        holdNumber = 0
        multiplier = 1
        self.rememberNumber.append(number)
        print("liczba wyświetlana:")
        print(self.rememberNumber)
        for i in self.rememberNumber:
            holdNumber = i
            printNumber = (printNumber*10) + holdNumber
            multiplier *= 10

        self.displayLbl['text'] = str(printNumber)

    def numberEquals(self):
        self.displayLbl['text'] = ''
        addNumber = 0
        for i in self.holdNumbersForOperation:
            addNumber += i
        self.holdNumbersForOperation = []
        self.holdNumbersForOperation.append(addNumber)
        print('Wynik dodawania: ',addNumber)
        self.addNumberToDisplay(number=addNumber)   

    def clearScrean(self):
        '''funkcja do czyszczenia wyświetlacza'''
        self.displayLbl['text'] = '0'
        self.rememberNumber = []
        self.holdNumbersForOperation= []

root = Tk()
root.configure(bg="red")
root.geometry("600x550")
root.title("Kalkulejtor")
app = App(root)
root.mainloop()


