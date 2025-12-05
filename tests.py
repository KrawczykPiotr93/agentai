from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

print("Running test case calculator main.py")
print(get_file_content("calculator", "main.py"))
print("-----END-----\n")

print("Running test case calculator pkg/calculator.py")
print(get_file_content("calculator", "pkg/calculator.py"))
print("-----END-----\n")

print("Running test case calculator /bin/cat")
print(get_file_content("calculator", "/bin/cat"))
print("-----END-----\n")

print("Running test case calculator pkg/does_not_exist.py")
print(get_file_content("calculator", "pkg/does_not_exist.py"))
print("-----END-----\n")

