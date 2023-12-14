class StickGame:
    def __init__(self, num_sticks):
        self.num_sticks = num_sticks
    
    def take_sticks(self, num):
        if num < 1 or num > 3:
            print("You can only take 1, 2, or 3 sticks.")
            return False
        
        if num > self.num_sticks:
            print("There are only", self.num_sticks, "sticks left.")
            return False
        
        self.num_sticks -= num
        return True
    
    def is_game_over(self):
        return self.num_sticks == 0
    
    def print_sticks(self):
        print("Sticks left:", self.num_sticks)
