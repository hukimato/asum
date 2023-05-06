class GeneratorModule:

    def run(self, dict_of_files: dict, path_to_destination_dir: str):
        for file_name, file_content in dict_of_files.items():
            with open(path_to_destination_dir + file_name, 'w+') as f:
                f.write(file_content)
        return 200
