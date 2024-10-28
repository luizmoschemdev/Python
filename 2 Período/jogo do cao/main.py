from interface import menu

class dog: 
    def __init__(self, name):
        self.is_on = False
        self.name = name
        self.hunger = 0
        self.tire = 0
def main(): 
    menu()
if __name__ == "main":
    main()
    
