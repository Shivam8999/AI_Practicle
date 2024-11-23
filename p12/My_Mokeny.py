class Monkey:
    def __init__(self, position, has_banana=False):
        self.position = position  # Position of the monkey (0 = ground, >0 = shelf)
        self.has_banana = has_banana

    def move(self, direction):
        if direction == "left":
            self.position -= 1
        elif direction == "right":
            self.position += 1

    def climb(self):
        if self.position == 0:  # Climb to the shelf if on the ground
            self.position += 1

    def pick_banana(self):
        if self.position == 1 and not self.has_banana:  # Assuming the banana is at position 1
            self.has_banana = True

class Environment:
    def __init__(self):
        self.monkey = Monkey(position=0)  # Start on the ground
        self.banana_position = 1  # Banana is on the shelf

    def is_goal_state(self):
        return self.monkey.has_banana

    def step(self, action):
        if action == "move_left":
            self.monkey.move("left")
        elif action == "move_right":
            self.monkey.move("right")
        elif action == "climb":
            self.monkey.climb()
        elif action == "pick_banana":
            self.monkey.pick_banana()

    def print_state(self):
        print(f"Monkey Position: {self.monkey.position}, Has Banana: {self.monkey.has_banana}")

def main():
    env = Environment()
    actions = ["move_right", "climb", "pick_banana"]  # Sequence of actions to get the banana

    print("Initial State:")
    env.print_state()

    for action in actions:
        env.step(action)
        env.print_state()
        if env.is_goal_state():
            print("Goal reached: Monkey has the banana!")
            break
    else:
        print("Goal not reached.")

if __name__ == "__main__":
    main()
