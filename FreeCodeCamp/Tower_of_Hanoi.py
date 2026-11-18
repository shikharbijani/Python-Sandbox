def hanoi_solver(n):
    pegs = {1: list(range(n, 0, -1)), 2: [], 3: []}
    snapshots = []

    def snapshot():
        snapshots.append(" ".join(str(pegs[i]) for i in (1, 2, 3)))

    def move(src, dst):
        pegs[dst].append(pegs[src].pop())
        snapshot()

    def solve(k, start, target):
        if k == 1:
            move(start, target)
        else:
            aux = 6 - (start + target)
            solve(k - 1, start, aux)
            move(start, target)
            solve(k - 1, aux, target)

    snapshot()
    solve(n, 1, 3)
    return "\n".join(snapshots)


def main():
    print(hanoi_solver(3))


if __name__ == "__main__":
    main()
