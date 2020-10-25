from graphics import*
win = GraphWin('Tic-Tac-Toe', 500, 500)
squares = 9
count=0
win.items=[]
#Create a class with the form of  the tictactoe program and Messages
class Board:  
     tittle = Text(Point(250 , 50), 'TicTacToe Game')
     tittle.setTextColor('black')
     tittle.setSize(12)
     tittle.draw(win)
     vertical = Line(Point(200, 100), Point(200, 400)) 
     vertical.setOutline('black')
     vertical.draw(win)

     vertical2 = Line(Point(300, 100), Point(300, 400)) 
     vertical2.setOutline('black')
     vertical2.draw(win)

     horizontal = Line(Point(100, 200), Point(400, 200)) 
     horizontal.setOutline('black')
     horizontal.draw(win)

     horizontal2 = Line(Point(100, 300), Point(400, 300))
     horizontal2.setOutline('black')
     horizontal2.draw(win)
     
     buttonRes = Rectangle(Point(200,450), Point(300,475))
     buttonRes.setFill('black')
     buttonRes.setOutline('white')
     buttonRes.draw(win)

     restart = Text(Point(250,463), 'Restart')
     restart.setTextColor('cyan')
     restart.setStyle('bold')
     restart.setSize(10)
     restart.draw(win)

     #Display this message with the other ones when I start the game and when restart button is touched
     
     #beforeStart = Text(Point(250, 422), 'Click one of the squares to start the game')
     #beforeStart.setTextColor('black')
     #beforeStart.setSize(10)
     #beforeStart.draw(win)
     
     Display(self,items,squares)
  

class Function:
    def __init__(self, squares , items):
        self.squares = squares
        self.items = []
        self.tile = tile
        self.beforeStart = beforeStart
        self.winner1 = winner1
        #self.winner1 = MessageX(self)
        self.winner2 = winner2
        #self.winner2 = MessageO(self)
        self.tie = tie
        #self.tie = Tie_Message(self)
        self.message = message
        #self.message = ERROR(self)
        self.p1 = p1
        self.X = X
        self.Y = Y

    
    def Message(self) :
        self.beforeStart = Text(Point(250, 422), 'Click one of the squares to start the game')
        self.beforeStart.setTextColor('black')
        self.beforeStart.setSize(10)
        self.beforeStart.draw(win)

    def MessageX(self):
        self.winner1 = Text(Point(250, 422), "X won the game")
        self.winner1.setTextColor('black')
        self.winner1.setSize(10)
        self.winner1.draw(win)
        print(AfterThis())
        
    def MessageO(self):
        self.winner2 = Text(Point(250, 422),  " O won the game")
        self.winner2.setTextColor('black')
        self.winner2.setSize(10)
        self.winner2.draw(win)
        print(AfterThis())
        
    def Tie_Message(self):
        self.tie = Text(Point(250, 422), "Is a tie ! Press restart to try again")
        self.tie.setTextColor('black')
        self.tie.setSize(10)
        self.tie.draw(win)
        print(AfterThis())
        
    def ERROR(self):
        self.message = Text(Point(250, 422), "ERROR you cannot repeat the option taken...")
        self.message.setTextColor('red')
        self.message.setSize(10)
        self.message.draw(win)
        
    def AfterThis(self , message):
        self.p1 = self.getMouse()
        if ((self.p1.getX()>100 and self.p1.getX()<200) and (self.p1.getY()>450 and self.p1.getY()<475)) :
            restart ()
        else :
            clear(win)
            self.message = Text(Point(250, 422),  "Click on 'Restart' to play again")
            self.message.setTextColor('black')
            self.message.setSize(10)
            self.message.draw(win)
            seld.p1 = win.getMouse()
            if ((self.p1.getX()>200 and self.p1.getX()<300) and (self.p1.getY()>450 and self.p1.getY()<475)) :
                restart ()
            else :
                print(AfterThis())

        
    def Display(self ,items, squares):
        for i in range(self.squares):
            self.items[i].setTextColor('red')
            self.items[i].setStyle('bold')
            self.items[i].setSize(10)
            self.items[i].draw(win)

    def theSquarelsit(self,items,squares , tile):
        for i in range(self.squares):
            self.tile = Text(Point(150+(i%3)*100, 150+(i//3)*100), i+1)
            self.items.apped(self.tile)
    
    def theIf():
        if (self.items[0].getText()== self.items[1].getText() and self.items[1].getText()== self.items[2].getText()):
            if self.items[0].getText()== 'X' :
                MessegeX()
            elif self.items[0].getText()== 'O' :
                MessegeO()
                return False
        elif (self.items[3].getText()==self.items[4].getText() and self.items[4].getText()== self.items[5].getText()):
           if self.items[3].getText()== 'X' :
               MessageX()
           elif self.items[3].getText()== 'O' :
               MessageO()
               return False
            
        elif (self.items[6].getText()==self.items[7].getText() and self.items[7].getText()==self.items[8].getText()):
           if self.items[6].getText()== 'X' :
               MessageX()
           elif self.items[6].getText()== 'O' :
               MessageO()
               return False
        elif (self.items[0].getText()== self.items[3].getText() and self.items[3].getText()== self.items[6].getText()):
            if self.items[0].getText()== 'X' :
                MessageX()
            elif self.items[0].getText()== 'O' :
                Message()
                return False
        elif (self.items[1].getText()== self.items[4].getText() and self.items[4].getText()== self.items[7].getText()):
            if self.items[1].getText()== 'X' :
                MessageX()
            elif self.items[1].getText()== 'O' :
                MessageO()
                return False
        elif (self.items[2].getText()== self.items[5].getText() and self.items[5].getText()== self.items[8].getText()):
            if self.items[2].getText()== 'X' :
                MessageX()
            elif self.items[2].getText()== 'O' :
                MessageO()
                return False
        elif (self.items[0].getText()==self.items[4].getText() and self.items[4].getText()==self.items[8].getText()):
            if self.items[0].getText()== 'X' :
                MessageX()
            elif self.items[0].getText()== 'O' :
                MessageO()
                return False
        elif (self.items[2].getText()==self.items[4].getText() and self.items[4].getText()==self.items[6].getText()):
            if self.items[2].getText()== 'X' :
                MessageX()
            elif self.items[2].getText()== 'O' :
                MessageO()
                return False
        else :
            for i in range(self.squares):
                if self.items[i].getText() not in ['X','O'] :
                    return True
            Tie_Message()
            return False
    def restart(self):
        for i in range(self.squares):
            self.items[i].setText(str(i+1))
            print(clear(self))
            print(Message(self))
            print(Press(self))
    def Press(self):
        while (theIf(self)):
            self.p1 = self.getMouse()
            if ( (self.p1.getX()>100 and self.p1.getX()<400) and (self.p1.getY()>100 and self.p1.getY()<400)):
                self.X = int((p1.getX()-100)//100)
                self.Y = int((p1.getY()-100)//100)
                global count
                if not (self.items[Y*3+X].getText()=='X') and not (self.items[Y*3+X].getText()=='O') :
                    if count % 2 == 0 :
                        self.items[Y*3+X].setText('X')
                    else :
                        self.items[Y*3+X].setText('O')
                    count+=1
                    clear(self)
                else :
                    ERROR()
            elif ((self.p1.getX()>200 and self.p1.getX()<300) and (self.p1.getY()>450 and self.p1.getY()<475)) :
                restart (self)
                  
    def clear(self):
        for self.item in self.items[:]:
            self.item.undraw()
            self.update()
        print(Board())

        
#The main to print the clases
def main():
    print(theSquarelist(self))
    Board()
    Function()
    print(Message(self))
    print(Press(self))
    
main()





