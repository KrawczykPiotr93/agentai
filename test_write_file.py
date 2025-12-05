from functions.write_file import write_file

print("Writing to calculator, lorem.txt")
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print("-----END-----\n")

print("Writing to calculator, pkg/morelorem.txt")
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print("-----END-----\n")

print("Writing to calculator, /tmp/temp.txt")
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
print("-----END-----\n")

