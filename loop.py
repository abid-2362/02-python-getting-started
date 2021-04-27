student_names = ["James", "Katarina", "Jessica", "Mark", "Bort", "Frank Grimes", "Max Power"]

# For Loop in Python
for name in student_names:
    if name == "Bort":
        continue
        print("Found him! " + name)
        break
    print("Currently testing " + name)


# While loop in python
num = 1
while num <= 10:
    # if num == 42:
    #    break
    print("Hello World {0}".format(num))
    num += 1
