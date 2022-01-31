# Get the test cases.
test_cases = int(input())


# Call teh fucntion
def compute(test_cases):
    count = 0
    
    # Run for each test case
    for test in range(int(test_cases)):
        a, b, c = list(map(int, input().split()))
        sum = a + b + c
        if sum >= 2 :
            count = count + 1
        sum = 0

    # Print the result.
    print(count)



# Call the computing function
compute(test_cases)
