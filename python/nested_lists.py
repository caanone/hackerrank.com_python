students = []


class Student:
    def __init__(self, name: str, score: float):
        self.name = name
        self.score = score
        self.score_idx = -1
        self.name_idx = -1
    @staticmethod
    def find_with_name_idx(st_list: list, name_idx: str):  # returns st score
        return (x.score for x in students if x.name_idx == name_idx)
    @staticmethod
    def find_with_score_idx(st_list: list, score_idx: str):  # returns st name
        return (x.name for x in students if x.score_idx == score_idx)
    @staticmethod
    def index_students(students):
        students.sort(key=lambda x: x.name)
        for idx, st in enumerate(students):
            st.name_idx = idx
        i_score = 0
        students.sort(key=lambda x: x.score)
        prev_st = students[0]
        for st in students:
            
            print("indexing " + st.name + " " + str(st.score) + " " + " index " + str(i_score) + " Condition is " + str(prev_st.score != st.score))
            if prev_st.score != st.score:
                st.score_idx = i_score
                # i_score -= 1
            else:
                st.score_idx = prev_st.score_idx
                # i_score += 1
                
            prev_st = st


if __name__ == '__main__':
    # Development purposes
    """
    from pronounceable import generate_word
    import random
    for _ in range(5):
        st = Student(generate_word(), random.randint(25, 100))
        students.append(st)
    """
    for _ in range(int(input())):
        name = input()
        score = float(input())
        st = Student(name, score)
        students.append(st)
    Student.index_students(students)

    for x in [_.name_idx for _ in students]:
        for y in [__ for __ in students if __.score_idx == 2]:
            if y.score_idx == x:
                # print(f"Student name: {y.name} \t score: {y.score} \t s_idx {y.score_idx} \t n_idx {y.name_idx} ")
                print(f"{y.name}")
    for y in [_ for _ in students]:
        print(f"Student name: {y.name} \t score: {y.score} \t s_idx {y.score_idx} \t n_idx {y.name_idx} ")
