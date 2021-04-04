import random
from art import logo 
print(logo)

level = input(f"Qué nivel quieres jugar?: \n 1 = Fácil \n 2 = Díficil \n ")

number_to_guess = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

guess_random = random.choice(number_to_guess)
#print(guess_random)

def game(lives):
  while lives > 0:
    guess = int(input("Ingresa un número: "))
    if guess > guess_random: 
      print(f"el {guess} es muy grande, intenta de nuevo")
      lives -=1
      print(f"Te quedan: {lives} vidas")
    if guess < guess_random: 
      print(f"el {guess} es muy pequeño, intenta de nuevo")
      lives -=1
      print(f"Te quedan: {lives} vidas")
    if guess == guess_random:
      print(f"Correcto!! el número es: {guess_random}")
      lives = 0
    if lives == 0: 
      print("Perdiste, que triste, no hay nadia peor que tu")

if level == "1": 
  game(10)
elif level == "2": 
  game(5)
else: 
  print("Ingresa una opcción correcta")