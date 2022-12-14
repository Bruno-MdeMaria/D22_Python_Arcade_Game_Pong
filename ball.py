from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1         #velocidade da bola

    def mover(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    #MÉTODO CRIADO PARA DETECTAR BATIDA NO EIXO Y(EM CIMA E EMBAIXO):
    def bater_y(self):
        self.y_move *= -1    #para mudar a direção quando bate da parede. ele está subindo em +0.5 com x -1 fica -0.5
        self.move_speed *= 0.9 #toda vez que bater na raquete a bola vai aumentar a velocidade(valor encontrado apos testes)
    
    def bater_x(self):
        self.x_move *= -1  
        self.move_speed *= 0.9
    
    #MÉTODO PARA RESETAR A BOLA QUANDO ERRAR E A BOLA SAIR:
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bater_x()

    


