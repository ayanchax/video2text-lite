import os


class CommonUtils:

    def __init__(self):
        pass
    
    def get_file_name_without_extension(self,file_path):
        """
    This method extracts the file name from a given file path and returns it without the extension.

    Parameters:
    file_path (str): The path of the file from which to extract the file name.

    Returns:
    str: The file name without the extension. If an error occurs during the process, returns None.

    Raises:
    Exception: If any error occurs during the process.
    """
        try:
            # Extract the base name (file name with extension)
            base_name = os.path.basename(file_path)

            # Split the base name to remove the extension
            return os.path.splitext(base_name)[0]
        except Exception as e:
               return None
        
    def list_files(self, dirpath: str, defaultSort=True, sortByName=False) -> list:
        """
        Get a list of files in a given directory
        """
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
        """
        Deletes a file from the filesystem.

        Parameters:
        file_path (str): The path to the file to be deleted.

        Returns:
        None

        Raises:
        FileNotFoundError: If the specified file cannot be found.
        """
        try:
            os.remove(os.path.abspath(file_path))
        except FileNotFoundError:
            print("File not found:", file_path)

    def delete_files(self, dirpath, file_extensions=("mp3")):
        """
        This function deletes files based on a specific file extension

        Returns:
        None

        Raises:
        Exception: if no files are found with the provided extension
        """
        dirpath = os.path.abspath(dirpath)
        files = self.list_files(dirpath)
        for file in files:
            if file.endswith(tuple(file_extensions)):
                self.delete_file(file)