if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    st_avarage = 0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for _ in student_marks[query_name]:
        st_avarage += _
    result = st_avarage/len(student_marks[query_name])
    print("%.2f" % result)
