def count_occurrences(target_number, n):
    count = 0
    for num in range(0, n+1):
        count += str(num).count(str(target_number))
    return count

while True:
    n = int(input("Enter the value of n (or 0 to exit): "))
    if n == 0:
        break
    target_number = int(input("Enter the target number: "))
    occurrences = count_occurrences(target_number, n)
    print(f"The number of occurrences of {target_number} till {n}: {occurrences}")

