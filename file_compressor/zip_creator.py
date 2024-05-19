import zipfile
import pathlib

def create_zip(file_paths, dest_folder):
    dest_path = pathlib.Path(dest_folder, "compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        for file_path in file_paths:
            file_path = pathlib.Path(file_path)
            archive.write(file_path, arcname=file_path.name)

if __name__ == "__main__":
    create_zip(file_paths=["file_a", "file_b"], dest_folder="storage")
