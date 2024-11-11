import filehandler_helper as fh
  
def search_for_vuln(search_word: str, output_file: str, critical_confirmed: str) -> None:
    search_list = list_with_files()

    for filepath in search_list:
        word = False
        critical = False
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                if search_word in line:
                    word = True
                if critical_confirmed in line:
                    critical = True
                if word and critical:
                    with open(output_file, 'a') as output:
                        output.write(f"{critical_confirmed} : {filepath}\n")
                    break

def list_with_files() -> list:
    fp = fh.get_path_of_folder('2023')
    folders_from_folder = fh.get_folder_get_list_with_foldernames(fp)
    list_with_folder_files = {}

    for i in folders_from_folder:
        folder_path = fh.return_filepath_joined_with_file(fp, i)
        filename_list = fh.get_list_with_names_from_folder(fh.get_path_of_folder(folder_path))
        list_with_folder_files[folder_path] = filename_list

    list_with_all_files_to_search = []
    for folder, file in list_with_folder_files.items():
        for f in file:
            list_with_all_files_to_search.append(fh.return_filepath_joined_with_file(folder, f))
    return list_with_all_files_to_search