class PokemonBinder:
    def __init__(self):
        self.binder = {}
        self.MAX_POKEDEX = 1025
        self.CARDS_PER_PAGE = 64
        self.GRID_SIZE = 8

    def menu(self):
        while True:
            print("\nBinder Menu")
            print("1. Add Pokemon Card")
            print("2. Reset Binder")
            print("3. View Binder")
            print("4. Return to Main Menu")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_card()
            elif choice == '2':
                self.reset_binder()
            elif choice == '3':
                self.view_binder()
            elif choice == '4':
                break
            else:
                print("Invalid input.")

    def add_card(self):
        try:
            number = int(input("Enter Pokedex number (1-1025): "))
            if number < 1 or number > self.MAX_POKEDEX:
                print("Invalid Pokedex number.")
                return
            if number in self.binder:
                page, row, col = self.binder[number]
                print(f"Card already exists on page {page}, position ({row+1},{col+1})")
            else:
                index = len(self.binder)
                page = index // self.CARDS_PER_PAGE + 1
                pos = index % self.CARDS_PER_PAGE
                row = pos // self.GRID_SIZE
                col = pos % self.GRID_SIZE
                self.binder[number] = (page, row, col)
                print(f"Added card #{number} on page {page}, position ({row+1},{col+1})")
                if len(self.binder) == self.MAX_POKEDEX:
                    print("You have caught them all!")
        except ValueError:
            print("Please enter a valid integer.")

    def reset_binder(self):
        confirm = input("Type 'CONFIRM' to reset or 'EXIT' to cancel: ")
        if confirm == 'CONFIRM':
            self.binder.clear()
            print("Binder has been reset.")
        else:
            print("Reset cancelled.")

    def view_binder(self):
        print("\nCurrent Cards in Binder:")
        for number in sorted(self.binder):
            page, row, col = self.binder[number]
            print(f"#{number}: Page {page}, Position ({row+1},{col+1})")
        print(f"Total cards: {len(self.binder)}")
        percent = len(self.binder) / self.MAX_POKEDEX * 100
        print(f"Completion: {percent:.2f}%")

if __name__ == "__main__":
    binder_app = PokemonBinder()
    binder_app.menu()

