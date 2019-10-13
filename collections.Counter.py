from collections import Counter

if __name__ == "__main__":
    shoes = int(input())
    shoe_sizes = Counter(input().split(" "))
    how_many_customers = int(input())
    print(shoe_sizes)
    
