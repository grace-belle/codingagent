import functions.run_python_file as rpf

def test_run_python_file():
    print(rpf.run_python_file("calculator", "main.py"))
    print(rpf.run_python_file("calculator", "main.py", "[3 + 5]"))
    print(rpf.run_python_file("calculator", "tests.py"))
    print(rpf.run_python_file("calculator", "../main.py"))
    print(rpf.run_python_file("calculator", "nonexistent.py"))
    print(rpf.run_python_file("calculator", "lorem.txt"))

test_run_python_file()