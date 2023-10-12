def dont_count():
    xn, sn = list(map(int, input().split()))

    x = input()
    s = input()

    count = 0
    if s in x:
        print(count)
        return

    while True:
        x += x
        count += 1
        if s in x:
            print(count)
            return
        if len(x) > 2 * sn:
            print(-1)
            return


num_tests = int(input())

for each_test in range(num_tests):
    dont_count()
