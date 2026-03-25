import functions.get_file_content as gfc

def test_get_file_content():
    print(gfc.get_file_content("calculator", "lorem.txt"))
    print(gfc.get_file_content("calculator", "main.py"))
    print(gfc.get_file_content("calculator", "pkg/calculator.py"))
    print(gfc.get_file_content("calculator", "/bin/cat"))
    print(gfc.get_file_content("calculator", "pkg/does_not_exist.py"))

test_get_file_content()