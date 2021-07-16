# unsafe
f = open("data.txt", "w")
f.write("wow i can write now - overwrite now")
f.close()

# by using "a" i can append
f = open("data.txt", "a")
f.write("\nwow i can append now ")
f.close()

# safe option use withm so no need close
with open("data.txt", "a") as f:
    f.write("\nI'm new line")

with open("data.txt", "r") as f:
    print(len(str(f.read()).split(" ")))
    f.seek(0)
    for line in f:
        print(line)
