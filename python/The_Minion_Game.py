import re


def minion_game(sub_string, string="BANANA"):
    score = 0
    player = ""
    sub_string = sub_string.upper()
    # Check out input lenght
    if 0 < len(sub_string) <= 10**6:
        SystemExit()
    
    # Get all substrings from string and entered string
    ## Wowels
    vowelsubstrs = [string[i: j] for i in range(len(string))
        for j in range(i + 1, len(string) + 1) if string[i].startswith((*"AEIOUaeiou",))]
    enteredvowelsubstrs = [sub_string[i: j] for i in range(len(sub_string))
        for j in range(i + 1, len(sub_string) + 1) if sub_string[i].startswith((*"AEIOUaeiou",))]
    ## Constants
    constantsubstrs = [string[i: j] for i in range(len(string))
        for j in range(i + 1, len(string) + 1) if not string[i].startswith((*"AEIOUaeiou",))]
    enteredconstantsubstrs = [sub_string[i: j] for i in range(len(sub_string))
        for j in range(i + 1, len(sub_string) + 1) if not sub_string[i].startswith((*"AEIOUaeiou",))]

    # Let`s check first char of entered string for determine to which minion playing then calculate score
    if sub_string.startswith((*"AEIOUaeiou",)):
        player = "Kevin"
        for x in vowelsubstrs:
            for y in enteredvowelsubstrs:
                score += len(re.findall(f'(?={y})', x))
    else:
        player = "Stuart"
        print(enteredconstantsubstrs.count(constantsubstrs))
        # for x in constantsubstrs:
        #     for y in enteredconstantsubstrs:
        #         print(x, y, score)
        #         if y.__contains__(x):
        #             score += 1
    
    # score = len(re.findall(f'(?={sub_string})', string))
    print(f"{player} {score}")


if __name__ == '__main__':
    s = input()
    minion_game(s)
