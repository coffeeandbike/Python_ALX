print("Let's subtract five numbers:")

start = 0

result_2 = 0

counter_2 = 0

while counter_2 < 5:
    number_2 = int(input("Enter number: "))
    if (counter_2 == 0):
        result_2 = start + number_2
    if (counter_2 > 0 and counter_2 < 5):
        result_2 -= number_2
    counter_2 += 1

print("Result of subtract is: ", result_2)

