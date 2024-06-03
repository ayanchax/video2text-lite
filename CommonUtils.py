import os


class CommonUtils:

    def __init__(self):
        pass

    def get_file_name_without_extension(self,file_path):
        try:
            # Extract the base name (file name with extension)
            base_name = os.path.basename(file_path)

            # Split the base name to remove the extension
            return os.path.splitext(base_name)[0]
        except Exception as e:
               return None
        
    def list_files(self,dirpath, defaultSort=True, sortByName=False):
            dirpath = os.path.abspath(dirpath)
            # List all files and directories in the specified path
            all_items = os.listdir(dirpath)
            
            # Filter out only the files
            files = [dirpath+"/"+item for item in all_items if os.path.isfile(os.path.join(dirpath, item))]
            
            # Verify file existence and sort files by their modification timestamp in ascending order
            if defaultSort is True:
                existing_files = [file for file in files if os.path.exists(file)]
                existing_files.sort(key=os.path.getmtime)
                files=existing_files
            else:
                  if sortByName is True:
                      #Sort files by their names in ascending order
                      files.sort(key=lambda x: os.path.basename(x).lower())  # Sorting case-insensitively
            
            return files

    def delete_file(self, file_path):
        try:
            os.remove(os.path.abspath(file_path))
        except FileNotFoundError:
            print("File not found:", file_path)

    def delete_files(self, dirpath, file_extensions=("mp3")):
        dirpath = os.path.abspath(dirpath)
        files = self.list_files(dirpath)
        for file in files:
            if file.endswith(tuple(file_extensions)):
                self.delete_file(file)