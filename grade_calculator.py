def calculate_average(grades):
    return sum(grades) / len(grades)

def determine_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    elif average <60:
        return 'Fail'
    else:
        return 'F'

def main():
    students = ["Ahmad", "Bader", "Huda", "Mohammed"]
    grades = [[85, 78, 92], [76, 88, 90], [90, 95, 93], [52, 59, 50]]

    for i in range(len(students)):
        average = calculate_average(grades[i])
        letter_grade = determine_letter_grade(average)
        print(f"{students[i]}: Average Grade = {average}, Letter Grade = {letter_grade}")

if __name__ == "__main__":
    main()