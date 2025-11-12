#----- Snake Game -----#
import tkinter as tk
import random

#Configurações da janela e do jogo
#Window and game settings
game_width = 500
game_height = 500
cell_size = 20 #Tamanho de cada "quadro" da grade. #Size of each grid "cell".
cols = game_width // cell_size
rows = game_height // cell_size
initial_snake_length = 3
initial_speed = 120 #Velocidade inicial em milissegundos. #Initial speed in milliseconds.

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=game_width, height=game_height, bg="#2a003d")
        self.canvas.pack()

#Estado do jogo #Game state
        self.direction = "Right" #Direção inicial da cobra. #Initial snake direction.
        self.next_direction = self.direction
        self.speed = initial_speed
        self.score = 0
        self.running = True

#Cria a cobra no centro da tela #Create the snake in the center of the screen
        start_x = cols // 2
        start_y = rows // 2
        self.snake = [(start_x - i, start_y) for i in range(initial_snake_length)]
#Cria a comida #Create the food
        self.food = None
        self.place_food()
#Desenha pela primeira vez #Draw for the first time
        self.draw()
#Eventos de teclado #Keyboard events
        root.bind("<Up>", lambda e: self.change_direction("Up"))
        root.bind("<Down>", lambda e: self.change_direction("Down"))
        root.bind("<Left>", lambda e: self.change_direction("Left"))
        root.bind("<Right>", lambda e: self.change_direction("Right"))
        root.bind("r", lambda e: self.restart())#Para reiniciar o jogo #To restart the game
        root.bind("p", lambda e: self.toggle_pause())#Para pausar/despausar o jogo
#Label de pontuação #Score label
        self.label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 14), bg="#2a003d", fg="white")
        self.label.pack()
#Inicia o loop do jogo #Start the game loop
        self.root.after(self.speed, self.game_loop)

def get_cell_coords(self, pos): #Retorna as coordenadas da célula na tela. #Returns the cell coordinates on the screen.
    x, y = pos
    return x * cell_size, y * cell_size, (x + 1) * cell_size, (y + 1) * cell_size

def place_food(self): #Coloca a comida em uma posição aleatória que não esteja ocupada pela cobra. #Place food in a random position not occupied by the snake.
    while True:
        x = random.randint(0, cols - 1)
        y = random.randint(0, cols - 1)
        if (x, y) not in self.snake:
            self.food = (x, y)
            break
def change_direction(self, new_dir): #Muda a direção da cobra, evitando reversões diretas. #Change snake direction, avoiding direct reversals.
    opposites = {"Up": "Down", "Down": "Up", "LEft": "Right", "Right": "Left"}
    if new_dir != opposites.get(self.direction): #Evita reversões diretas. #Avoid direct reversals.
        self.next_direction = new_dir

def game_loop(self): #Loop principal do jogo #Main game loop
    if not self.running:
        return
    self.direction = self.next_direction #Atualiza direção(no início do tick para evitar multi-entrada) #Update direction (at the beginning of the tick to avoid multiple entries)

    head_x, head_y = self.snake[0]
    if self.direction == "Up":
        head_y -= 1
    elif self.direction == "Down":
        head_y += 1
    elif self.direction == "Left":
        head_x -= 1
    elif self.direction == "Right":
        head_x += 1
    
    new_head = (head_x, head_y)

    #Checar colisão com paredes #Check for collision with walls.
