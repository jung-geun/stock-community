import random

class Game:
    def __init__(self):
        self.rules = {
            "ROCK": "Scissors",
            "PAPER": "Rock",
            "SCISSORS": "Paper"
        }
        
    
    def play(self, inputs = None)->str:
        if inputs == None:
            inputs = self.__get_random()
        inputs = inputs.upper()
        computer = self.__get_random()
        if inputs not in self.rules:
            result = "Invalid input"
        elif inputs == computer:
            result = "Draw"
        elif self.rules[inputs] == computer:
            result = "You Win"
        else:
            result = "Computer Win"
        print("You: " + inputs + " Computer: " + computer + " Result: " + result)
        
        return result
        
    def __get_random(self):
        r = random.randint(0,2)
        if r == 0:
            return "Rock"
        elif r == 1:
            return "Paper"
        else:
            return "Scissors"
    
    
if __name__ == "__main__":
    game = Game()
    print(game.play("Rock"))