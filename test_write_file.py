import functions.write_file as wf

def test_write_file():
    print(wf.write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print(wf.write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print(wf.write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

test_write_file()