#Implement file operations (read, write).

outfile = open('write.txt' , 'w+')

string = str(input("Enter input: "))

n = outfile.write(string)

if (n <= 0):
    print("Error!")
else:
    print("\nWriting to a file successful:\n")

outfile.close()

with open('write.txt') as f:
    while True:
        c = f.read(500)
        if not c:
            print("End of File")
            break
        print("", c)
        break

