name = input("Hi, my name is Taj. And yours? ")

print("Nice to meet you, {}!".format(name))
age = int(input("How old are you? "))

if 17 < age < 31:
    print("{}! I personally invite you to join our exclusive holiday celebration!".format(name))
else:
    print("Thanks for your interest in joining our holiday celebration {}!\nUnfortunately, I am unable to reserve space for you.".format(name))
