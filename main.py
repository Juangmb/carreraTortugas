import turtle

class Circuito():
    corredores = []
    __posStartY = (0,50,-50,100,-100,150,-150,200,-200)
    __colores = ("green","blue","red","orange","cyan","deeppink","lime","indigo","goldenrod",)
    
    
    
    def __init__(self, width, height):
        self.__screen = turtle.Screen()
        self.__screen.setup(width,height)
        self.__screen.bgcolor("lightgray")
        self.__startLine = -width/2 + (width/100)*5
        self.__finishLine = width/2 + (width/100)*5
        
        self.__createRunners()
    
    def __createRunners(self):
        x = int(input("Numero de corredores(1 a 9): "))
        for i in range(x):
            new_turtle = turtle.Turtle()
            new_turtle.hideturtle()
            new_turtle.shape("turtle")
            new_turtle.shapesize(3,3,3)
            new_turtle.penup()
            new_turtle.setpos(self.__startLine, self.__posStartY[i])
            new_turtle.color(self.__colores[i])
            new_turtle.pencolor("black")
            new_turtle.showturtle()
            self.corredores.append(new_turtle)
    
  
        
            

if __name__ == "__main__":
    circuito = Circuito(640,480)
    
