import turtle
import random

class Circuito():
    corredores = []
    __posStartY = (0,50,-50,100,-100,150,-150,200,-200)
    __colores = ("green","blue","red","darkorange","cyan","deeppink","lime","indigo","goldenrod",)
    
    
    
    def __init__(self, width, height):
        self.__screen = turtle.Screen()
        self.__screen.setup(width,height)
        self.__screen.bgcolor("lightgray")
        self.__startLine = -width/2 + 20
        self.__finishLine = width/2 - 45
        
        self.__createRunners()
    
    def __createRunners(self):
        x = int(input("Numero de corredores(1 a 9): "))
        for i in range(x):
            new_turtle = turtle.Turtle()
            new_turtle.hideturtle()
            new_turtle.speed(3)
            new_turtle.shape("turtle")
            new_turtle.shapesize(2,2,2)
            new_turtle.penup()
            new_turtle.setpos(self.__startLine, self.__posStartY[i])
            new_turtle.color(self.__colores[i])
            new_turtle.pencolor("black")
            new_turtle.showturtle()
            self.corredores.append(new_turtle)
    
    def competir(self):
        hayGanador = False
        
        while not hayGanador:
            for tortuga in self.corredores:
                avance = random.randint(5,15)
                tortuga.fd(avance)
                if tortuga.xcor() >= self.__finishLine:
                    hayGanador = True
                    print("La tortuga de color {} ha ganado".format(tortuga.color()[1]))
                    break
        
    
if __name__ == "__main__":
    circuito = Circuito(640,480)
    input("Realicen sus apuestas: ")
    circuito.competir()
    
    
