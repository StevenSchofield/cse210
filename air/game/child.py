from game.person import Person

class Child(Person):
    def __init__(self) -> None:
        super().__init__(15)
    
    def speak(self):
        return "I want a balloon!"