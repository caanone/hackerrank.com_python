def find_day(m, d, y):
    if 2000 < y < 3000:
        SystemExit()
    from calendar import weekday, day_name
    print(day_name[weekday(y, m, d)].upper())

if __name__ == "__main__":
    date = [*map(int, input().split(" "))]
    find_day(*date)