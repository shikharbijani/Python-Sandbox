def verify_card_number(digits):
    total = 0
    cleaned = digits.replace(" ", "").replace("-", "")

    for digit_place, ch in enumerate(reversed(cleaned), start=1):
        n = int(ch)
        if digit_place % 2 == 0:
            n *= 2
            if n > 9:
                n -= 9
        total += n

    return "VALID!" if total % 10 == 0 else "INVALID!"


def main():
    print(verify_card_number("4111-1111-1111-1111"))  

if __name__ == "__main__":
    main()
