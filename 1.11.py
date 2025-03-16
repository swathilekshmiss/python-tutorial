def evencubes(n):
    total = 0
    for i in range(2, n + 1, 2):
        total += i ** 3
n = int(input("Enter a positive integer: "))
print(f"Sum of cubes of even numbers: {total}")
evencubes(n)
