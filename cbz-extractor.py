import zipfile

def extract_cbz_file(file_path, destination_path):
    try:
        with zipfile.ZipFile(file_path, 'r') as cbz_file:
            cbz_file.extractall(destination_path)
        print(f"Contents of {file_path} successfully extracted to {destination_path}.")
    except zipfile.BadZipFile:
        print(f"Error: {file_path} is not a valid CBZ file.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Usage example
cbz_file_path = '/path/to/your/file.cbz'
destination_folder = '/path/to/destination/folder'
extract_cbz_file(cbz_file_path, destination_folder)
