
def hanoi(n, start=1, target=3):
    if n == 1:
        print_move(start, target)
    else:
        aux = 6 - (start + target)
        hanoi(n - 1, start, aux)
        print_move(start, target)
        hanoi(n - 1, aux, target)

def print_move(x,y):
     print(f"{x} -> {y}")

def main():
    hanoi(3)


if __name__ == "__main__":
    main()
