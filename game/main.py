import random

options=('Piedra', 'Papel', 'Tijera')

computer_wins = 0
user_wins = 0
rounds = 1

while True:

  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10)

  #Contador de las partidas
  print('computer_wins', computer_wins)
  print('user_wins', user_wins)
  
  user_option = input('Piedra, papel o tijera: ').capitalize()
  computer_option = random.choice(options)
  
  if user_option not in options:
    print('Opción invalida')
    continue
  
  print('User option: ', user_option)
  print('Computer option: ', computer_option)
  
  if user_option == computer_option:
    print('Empate!')
    
  elif user_option == 'Piedra':
    if computer_option == 'Tijera':
      print('Piedra gana a tijera')
      print('user gano!')
      user_wins += 1
    else:
      print('Papel gana a piedra')
      print('Computer gano!')
      computer_wins += 1
      
  elif user_option == 'Papel':
    if computer_option == 'Piedra':
      print('Papel gana a piedra')
      print('User gano!')
      user_wins += 1
    else:
      print('Tijera gana a papel')
      print('Computer gano!')
      computer_wins += 1
      
  elif user_option == 'Tijera':
    if computer_option == 'Papel':
      print('Tijera gana a papel')
      print('User gano!')
      user_wins += 1
    else:
      print('Piedra gana a tijera')
      print('Computer gano!')
      computer_wins += 1

  if computer_wins == 2:
    print('El computador es campeón')
    break

  if user_wins == 2:
    print('El usuario es campeón')
    break

  rounds += 1