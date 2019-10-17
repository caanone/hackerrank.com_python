def swap_case(s: str):
    swapped_str = ""
    if 0 < len(s) <= 1000:
        pass
    for _ in range(len(s)):
        if s[_].isupper():
            swapped_str += s[_].lower()
        elif s[_].islower():
            swapped_str += s[_].upper()
        else:
            swapped_str += s[_]
    return swapped_str


if __name__ == '__main__':
    print(swap_case(str(input())))
