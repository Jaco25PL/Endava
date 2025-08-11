import random
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

class Luchador:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, enemy):
        # When player attacks, the player by props gets punch
        damage = random.randint(15, 25)
        enemy.health -= damage


    def is_alive(self):
        # We retrun true if the player is alive
        return self.health > 0 
            
    
def main():

    player_1_name = input("Enter a name for fighter 1: ")
    player_2_name = input("Enter a name for fighter 2: ")

    player1 = Luchador(player_1_name, 100)
    player2 = Luchador(player_2_name, 100)

    print("\n")
    print(Fore.RED + "=" * 19)
    print(Fore.LIGHTRED_EX + Style.BRIGHT + "=== Foo Fighters ===")
    print(Fore.RED + "=" * 19)

    print(Fore.GREEN + Style.BRIGHT + f"\nPlayer 1 -> {player1.name} - Health -> {player1.health}")
    print(Fore.GREEN + Style.BRIGHT + f"Player 2 -> {player2.name} - Health -> {player2.health}\n")


    end_of_game = False
    round = 1

    while not end_of_game:    

        print( Fore.CYAN + f"Round {round}\n")
        round += 1

    # First, player1 attacks player 2
    # player can attack only if is alive
        if player1.is_alive():
            player1.attack(player2)
            print(f"{player1.name} Attacks {player2.name} - {player2.name} health is now: {player2.health}")
            # print("\n")

    # Now, player2 attacsk player 1
        if player2.is_alive():
            player2.attack(player1)
            print(f"{player2.name} Attacks {player1.name} - {player1.name} health is now: {player1.health}")
            print("-" * 55)

    # if player1 health is < 0 -> player 2 wins,
    # if player2 health is < 0 -> player 1 wins

        if not player1.is_alive():
            end_of_game = True
            print(Fore.GREEN + "=" * 55)
            print(f"Ufffff. The winner is {player2.name} with {player2.health} of HP")
            print("\n")
            # break

        if not player2.is_alive():
            end_of_game = True
            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "=" * 55)
            print(Fore.LIGHTGREEN_EX + Style.BRIGHT + f"\nUfffff. The winner is {player1.name} with {player1.health} of HP")
            print("\n")
            # break

    print(Fore.LIGHTRED_EX + Style.BRIGHT + "=" * 20)
    print(Fore.LIGHTRED_EX + " Thanks for playing ")
    print(Fore.LIGHTRED_EX + Style.BRIGHT + "=" * 20)

if __name__ == "__main__":
    main()

