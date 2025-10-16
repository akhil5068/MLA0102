def towers_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} → {target}")
        return
    towers_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} → {target}")
    towers_of_hanoi(n - 1, auxiliary, source, target)
n = 3
print("Towers of Hanoi Solution:\n")
towers_of_hanoi(n, 'A', 'B', 'C')
