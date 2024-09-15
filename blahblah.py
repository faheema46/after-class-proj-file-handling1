# Create the first file and write data
with open("createfile1.txt", "w") as f1:
    f1.write("This is content for the first file.")

# Create the second file and write data
with open("createfile2.txt", "w") as f2:
    f2.write("This is content for the second file.")


with open("createfile1.txt", "r") as f1:
    data1 = f1.read()
with open("createfile2.txt", "r") as f2:
    data2 = f2.read()


with open("f3.txt", "w") as f3:
    data3 = data1 + "\n\n" + data2
    f3.write(data3)


with open("f3.txt", "r") as f3:
    print(f3.read())


