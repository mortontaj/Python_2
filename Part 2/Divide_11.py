# number = 0
# while number / 11 != 1 or number == 0:
#     print(number)
#     if number / 11 == 1:
#         break
#     number += 1

# for i in range(0, 100, 7):
#     print(i)
#     if i > 0 and i % 11 == 0:
#         break

i = 0
while i < 21:
    if (i % 3 == 0 or i % 5 == 0):
        i += 1
        continue
    else:
        print(i)
    i += 1

# for x in range(21):
#     if x % 3 == 0 or x % 5 == 0:
#         continue
#     print(x)

