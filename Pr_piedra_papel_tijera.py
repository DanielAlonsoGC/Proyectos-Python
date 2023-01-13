import random
import tkinter
def f_boton1():
    etiqueta2["text"]= texto1.get()
    etiqueta5["text"]= "Tu eleccion"
def f_boton2():
    usuario1=etiqueta2["text"]
    computer1 = random.choice(['r', 'p', 't'])
    etiqueta3["text"]= computer1
    etiqueta4["text"]=play(usuario1,computer1)
    etiqueta6["text"]= "Eleccion de la PC"
def play(user,computer):
    if user == computer:
        return 'It\'s a tie'
    if is_win(user, computer):
        return 'You won!'

    return 'You lost'

def is_win(player, opponent):
    if(player == 'r' and opponent == 't') or (player == 't' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

if __name__ == '__main__':
    ventana = tkinter.Tk()
    ventana.title("Piedra, papel o tijera")
    #mensaje
    etiqueta1 = tkinter.Label(ventana,text="¿que escoges:\n'r' para roca\n'p' para papel\n't' para tijera?",font="Calibri 10")
    etiqueta1.grid(row = 2,column=0, padx=5, pady=5)
    #creacion de widgets para el usurio
    texto1 = tkinter.Entry(ventana, font="Calibri 20",width=1)
    texto1.grid(row = 3,column= 0 , padx=5, pady=5)
    
    boton1 = tkinter.Button(ventana,text ="enviar",command= f_boton1,width = 5)
    boton1.grid(row = 4,column= 0, padx=5, pady=5) 

    etiqueta5 = tkinter.Label(ventana,font="Calibri 20")
    etiqueta5.grid(row = 1,column=3, padx=5, pady=5)

    etiqueta2 = tkinter.Label(ventana,font="Calibri 20")
    etiqueta2.grid(row = 2,column=3, padx=5, pady=5)

    etiqueta6 = tkinter.Label(ventana,font="Calibri 20")
    etiqueta6.grid(row = 4,column=3, padx=5, pady=5)

    boton2 = tkinter.Button(ventana,text ="Generar valor de COM y jugar ",command= f_boton2,width = 30)
    boton2.grid(row = 6,column= 3, padx=5, pady=5)
    
    etiqueta3 = tkinter.Label(ventana,font="Calibri 20")
    etiqueta3.grid(row = 5,column=3, padx=5, pady=5)
    #FINAL DEL JUEGO
    etiqueta4 = tkinter.Label(ventana,font="Calibri 20")
    etiqueta4.grid(row = 3,column=5, padx=5, pady=5)

    ventana.mainloop()
