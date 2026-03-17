n = int(input("Enter number of queens: "))

x = [-1] * n
count = 0

def place(k, i):
    for j in range(k):
        if x[j] == i or abs(x[j] - i) == abs(j - k):
            return False
    return True

def nqueen(k):
    global count

    for i in range(n):
        if place(k, i):
            x[k] = i

            if k == n - 1:
                count += 1
                print("Solution", count)

                for r in range(n):
                    for c in range(n):
                        if x[r] == c:
                            print("Q", end=" ")
                        else:
                            print(".", end=" ")
                    print()
                print()

            else:
                nqueen(k + 1)

nqueen(0)
