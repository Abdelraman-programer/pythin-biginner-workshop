


class studen:
    def __init__(self, name,score =0 ):
        
        self.name = name
        self.score = score
    def update_score(self,new_score):
        if new_score>=0:
            self.score = new_score
        else:
            print("score must be positive")
    def display(self):
        print(f"{self.name} has score {self.score}")    

def main():
    name = input("Enter student name: ")
    student1 = studen(name)
    while True:
        change = input("Enter 'u' to update score, 'd' to display score, or 'q' to quit: ")
        if change == 'u':
            new_score = float(input("Enter new score: "))
            student1.update_score(new_score)
        elif change == 'd':
            student1.display()
        elif change == 'q':
            print("Thank you for using the student score system. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")
main()            


           
    