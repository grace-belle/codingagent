import functions.get_files_info as gfi
def test_get_files_info():
    print(gfi.get_files_info("calculator", "."))
    print(gfi.get_files_info("calculator", "pkg"))
    print(gfi.get_files_info("calculator", "/bin"))
    print(gfi.get_files_info("calculator", "../"))


test_get_files_info()