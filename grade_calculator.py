# grade_calculator.py

def calculate_grade(marks):
    avg = sum(marks) / len(marks)
    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    else:
        grade = "F"
    return avg, grade

if __name__ == "__main__":
    marks = []
    print("Enter marks for 5 subjects:")
    for i in range(5):
        mark = float(input(f"Subject {i+1}: "))
        marks.append(mark)

    avg, grade = calculate_grade(marks)
    print(f"\nAverage Marks: {avg:.2f}")
    print(f"Grade: {grade}")
