# Basic :
for i in range(151):
    print(i)

# Multiples of Five :
for i in range(5, 1001, 5):
    print(i)



# Counting, the Dojo Way :
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)


# Whoa. That Sucker's Huge :
sum = 0
for i in range(0, 500001):
    if i % 2!= 0:
        print(i)
        sum += i

print("The final sum is:", sum)


# Countdown by Fours :
current_number = 2018
while current_number > 0:
    print(current_number)
    current_number -= 4


# Flexible Counter :
lowNum = 2
highNum = 9
mult = 3

for num in range(lowNum, highNum + 1):
    if num % mult == 0:
        print(num)