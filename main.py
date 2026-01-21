import random   
num_experiments = 10000

def single_experiment(to_switch):
    correct = random.randint(0, 2)
    guess = random.randint(0, 2)
    
    to_open = [0, 1, 2]
    to_open.remove(correct)
    if guess in to_open: to_open.remove(guess)
    
    open_door = random.choice(to_open)
    
    if to_switch: 
        guess = 3 - open_door - guess
    
    return correct == guess
    
switched_wins = 0
no_switched_wins = 0
for i in range(num_experiments):
    if single_experiment(False): no_switched_wins += 1
    if single_experiment(True): switched_wins += 1
    
print('Total experiments per case: ', num_experiments)
print('Switched wins: ', switched_wins/num_experiments, '%')
print('No switched wins: ', no_switched_wins/num_experiments, '%')