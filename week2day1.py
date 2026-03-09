#code one
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def numbers(a,b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    print(add)
    print(sub)
    print(mul)
    print(div)
numbers (a,b)


#code two

def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

user_score = int(input("Enter your score: "))
grade = classify_grade(user_score)
print(f"Your grade is: {grade}")



