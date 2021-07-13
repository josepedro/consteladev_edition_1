sum = 0
for number in range(100):
    sum += number
print("Result: " + str(sum))

def check_letter_a(word):
    if "a" in word or "A" in word:
        return True
    else:
        return False

word_1 = "Caraca"
word_2 = "Tio"
ans_word_1 = check_letter_a(word_1)
ans_word_2 = check_letter_a(word_2)
print("Result word_1: " + str(ans_word_1))
print("Result word_2: " + str(ans_word_2))

class Student():
    def __init__(self, new_name):
        self.name = new_name
    def study(self, subject):
        print("Eu " + self.name + " estou estudando " + subject)

student = Student("Matheus")
print("Name: " + student.name)
student.study("React Native")
student_2 = Student("Igor")
print("Name 2: " + student_2.name)
