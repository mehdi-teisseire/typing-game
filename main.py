from game import gameplay

def main():
    current_level = "NORMAL" 

    while True: 
        selected_level = gameplay(
            f"media/background/{current_level}_background.jpg",
            f"media/images/{current_level}_alien.png",
            current_level
        )

        if selected_level in ['NORMAL', 'EASY', 'ENDLESS', 'HARD']:
            current_level = selected_level 

if __name__ == "__main__":
    main()

"""
from menu import run_menu
from level_one import endless_level


def main():
    run_menu()
    endless_level()

if __name__ == "__main__" :
    main()
"""