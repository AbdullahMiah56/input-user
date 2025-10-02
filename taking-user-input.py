a=input("Enter your seweet name:")
print("My name is:",a)

# sobai ak shathe khawar por bill bonton

a=input("How many people are you:")
b=input("total Bill:")
c=float(b)/float(a)
print("Bill per person",c)

# str er shathe int concat kora 

a="abdullah"
b=10
print(str(a)+str(b))

# f-str deye add kora

name = "Abdullah"
num= 20
print(f"{name}{num}")

name = "Abdullah"
num= 40
print(f"{name}has{num} friends")

# str er name counts

name= "Abdullah"
for character in name:
    print(character)

# koto ghula letter ache ber korar neyom

name = "Abdullah miah"
print(len(name))

# for lop deye counts korar neyom

name="Bangladesh is my Homeland"
count = 0
for character in name:
    count+=1
    print(count)

# kono letter khuje paite
name = "there is no man"
if"z" in name:
    print("o ache")
else:
    print(" nai")

# kon letter koto bar ache dekhar neyom

name="Abdullah"
print(name.lower().count("a"))

# akta letter koto bar ache dekhar neyom
name= "Hey can i help you"

frequency={}

for character in name.lower():

    # space bat delam  
    if character !=" ":
        if character in frequency:
            frequency[character] += 1
        else:
            frequency[character] = 1

for char, count in frequency.items():
    print(f"{char} --> {count} Times")



