class NeedforValid:
    def __init__(self, le_string: str):
        self.le_string = le_string
        # if 0 < len(self.le_string) <= 100:
        #     SystemExit()
        self.has_alphanum = False
        self.has_alpha = False
        self.has_num = False
        self.has_lower = False
        self.has_upper = False

# You can implement with "re" module easily. I used methods in "__builtins__"
    def validate(self):
        for c in self.le_string:
            if c.isalnum():
                self.has_alphanum = True
                if c.isalpha():
                    self.has_alpha = True
                    if c.islower():
                        self.has_lower = True
                    if c.isupper():
                        self.has_upper = True
                if c.isdigit():
                    self.has_num = True


if __name__ == '__main__':
    x = NeedforValid(input())
    x.validate()

    print(x.has_alphanum, x.has_alpha, x.has_num, x.has_lower, x.has_upper, sep="\n")
