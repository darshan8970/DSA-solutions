if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = str(input())
    if query_name in student_marks:
        A = student_marks.get(query_name)
        if 2<=n<=10 and all(0<=int(A[score])<=100 for score in range(len(A))) and 0<=len(A)<=3:
            average = sum(A)/len(A)
            print(f"{average:.2f}")
        else:
            print("Error: Constraints mismatch")
    else:
        print("Error: Student not found")
