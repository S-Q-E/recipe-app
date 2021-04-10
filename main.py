from menus.main_menu import MainMenu

def main():
    main_menu = MainMenu()
    main_menu.show()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Bye!")