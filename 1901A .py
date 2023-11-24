num_tests = int(input())


def solve():
    number_of_stations, x = list(map(int, input().split()))
    gas_stations = list(map(int, input().split()))
    x_diff = x - gas_stations[-1]
    gas_stations.insert(0, 0)
    gas_diff = max([j - i for i, j in zip(gas_stations[:-1], gas_stations[1:])])
    res = max((2 * x_diff), (gas_diff))
    print(res)


for each_test in range(num_tests):
    solve()
