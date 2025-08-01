def factor(num):
    if num == 1:
        return 1
    else:
        return num * factor(num - 1)
print(factor(5))  # Output: 120


def fibnocci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibnocci(n - 1) + fibnocci(n - 2)
print(fibnocci(5))  # Output: 5


def fibnacci_series(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        series = fibnacci_series(n - 1)
        series.append(series[-1] + series[-2])
        return series
print(fibnacci_series(5))  # Output: [0, 1, 1, 2, 3]



def fib_series(num):
    if(num==0):
        return 0
    elif(num == 1):
        return 1
    else:
        return fib_series(num-1)+fib_series(num-2)
for i in range(9):
    print(fib_series(i))



    def move_tower(n, source, target, auxiliary, moves):
        if n == 1:
            moves.append(f"Move disk 1 from {source} to {target}")
        else:
            move_tower(n - 1, source, auxiliary, target, moves)
            moves.append(f"Move disk {n} from {source} to {target}")
            move_tower(n - 1, auxiliary, target, source, moves)

# Input: number of disks
    num = int(input("Enter number of disks: "))

# List to hold the moves
    moves = []

# Call the function
    move_tower(num, 'A', 'C', 'B', moves)

# Print the steps
    for move in moves:
        print(move)
