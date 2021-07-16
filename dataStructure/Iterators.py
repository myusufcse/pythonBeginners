s = "you are cool bro. thanks for this explanation"
l = s.split()
print(l)

itr = iter(l)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
try:
    # error in the below line since it printed all the value.
    print(next(itr))
except StopIteration as si:
    print(type(si).__name__)

print(50*"*")
print(dir(l))
print(50*"*")

itr = reversed(l)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))