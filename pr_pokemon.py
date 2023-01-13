from random import *
#Clase pokemon 
class Pokemon:
    def __init__(self, nombre, ataque, vida) -> None:
        self.nombre = nombre
        self.ataque = ataque
        self.vida = 100
    def gano(self):
        print(f'{self.nombre} GANO LA BATALLA!!!')
        print("MAS SUERTE LA PROXIMA VEZ")

#Creacion de pokemones
p1 = Pokemon("pikachu",15)
p2 = Pokemon("Chariza",12)
#inicializamos los valores y el turno
p1.vida = 100
p2.vida = 100
turno = randint(1,2)


while p1.vida > 0 and p2.vida > 0
    if turno == 1:
        p2.vida = p2.vida - p1.ataque
        turno = 2
    else:
        p1.vida = p1.vida - p2.ataque
        turno = 1


if p1.vida <= 0:
    p2.gano()
else:
    p1.gano()
