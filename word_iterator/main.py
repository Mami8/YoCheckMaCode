import meine_libs as file_manager

directory = input("Please, enter the firectory to scan.\n>> ")

keyword = input("Now enter the keyword to be searched for.\n>> ")

pdf_files, docx_files, all_files, other_files, isError = file_manager.file_founder(directory)


if isError == 1:
    print ("An error occurred Whilst creating the list of files.\n", all_files)

print(all_files, pdf_files, docx_files, other_files)

result, isError = file_manager.iterate(keyword, all_files)

if isError == 1:
    print ("An error occurred while searching.\n", result)

elif isError == 0:
    print ("File was found.\n\t", result)