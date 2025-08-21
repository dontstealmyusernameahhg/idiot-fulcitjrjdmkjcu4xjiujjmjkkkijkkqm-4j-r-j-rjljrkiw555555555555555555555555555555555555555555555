import random
class FruitQuiz:
    def __init__(self):
        self.fruits = ["apple", "banana", "cherry", "date", "elderberry"]
        self.selected_fruit = random.choice(self.fruits)
        self.fruit_colors = {'apple': 'red', 'banana': 'yellow', 'cherry': 'red', 'date': 'brown', 'elderberry': 'black'}

    def get_fruit(self):
        return self.selected_fruit

    def reset_fruit(self):
        self.selected_fruit = random.choice(self.fruits)

    def quiz(self):
        while True:
            fruit = self.get_fruit()
            color = self.fruit_colors[fruit]
            answer = input(f"What color is the {fruit}? ")
            if answer.lower() == color:
                print("Correct!")
                break
            else:
                print(f"Wrong! The color of {fruit} is {color}. Try again.")
                self.reset_fruit()
                try:
                    option = int(input("Do you want to continue? (1 for Yes, 0 for No): "))
                except ValueError:
                    print("Invalid input. Exiting the quiz.")
                    break
                if option == 0:
                    print("Thank you for playing!")
                    break

print("Welcome to Fruit Quiz!")
fq = FruitQuiz()
fq.quiz()
print("Goodbye!")