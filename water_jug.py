print("Water Jug Problem")
print("Goal is to get exactly 2 Liters in Jug A")

jug_a = 0
jug_b = 0

def fill_a():
    global jug_a
    jug_a = 4
def fill_b():
    global jug_b
    jug_b = 3
def empty_a():
    global jug_a
    jug_a = 0
def empty_b():
    global jug_b
    jug_b = 0
def pour_a_to_b():
    global jug_b, jug_a
    # if jug_a + jug_b >= 7:
    #     jug_b = 3
    #     jug_a -= 3
    # elif jug_a + jug_b <= 3:
    #     jug_b += jug_a
    #     jug_a -= ()
    amt = min(jug_a, 3-jug_b)
    jug_b += amt 
    jug_a -= amt
def pour_b_to_a():
    global jug_a, jug_b
    # if jug_a + jug_b >= 7:
    #     jug_a = 4
    # elif jug_a + jug_b <= 4:
    #     jug_a += jug_b
    amt = min(jug_b, 4-jug_a)
    jug_a += amt
    jug_b -= amt
while jug_a != 2:
    print("In Jug A: ",jug_a, "L")
    print("In Jug B: ",jug_b, "L")
    print("Choices: 1-fill_a, 2-fill_b, 3-empty_a, 4-empty_b, 5-pour_a_to_b, 6-pour_b_to_a")
    choice = input("Enter your choice(1 to 6): ")
    if choice == "1":
        fill_a()
    elif choice == "2":
        fill_b()
    elif choice == "3":
        empty_a()
    elif choice == "4":
        empty_b()
    elif choice == "5":
        pour_a_to_b()
    elif choice == "6":
        pour_b_to_a()

print("Goal Achieved!!!")
print("In Jug A: ",jug_a, "L")
print("In Jug B: ",jug_b, "L")