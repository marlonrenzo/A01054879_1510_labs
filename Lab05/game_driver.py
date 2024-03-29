from Lab05.lab05 import roll_die
from Lab05.lab05 import choose_inventory
from Lab05.lab05 import generate_name
from Lab05.lab05 import create_character
from Lab05.lab05 import print_character


def main():
    """
    Call all functions to run the program.
    """
    inventory = ['Longsword', 'Dagger', 'Bow', 'Staff', 'Wand', 'Shield', 'Spear', 'Axe', 'Hammer']
    print("I am now rolling a 3d6 ---> You rolled", roll_die(3, 6))
    print("I am now generating two random inventory items for you ---> ", choose_inventory(inventory, 2))
    print("I am now generating your name ---> Hello", generate_name(4))
    print("I am now creating a random character for you ---> ", create_character(8))

    print("\n..... Here is your character info below .....")
    character = create_character(8)
    character.append(choose_inventory(inventory, 3))
    print_character(character)


if __name__ == '__main__':
    main()
