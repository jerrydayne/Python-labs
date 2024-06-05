import zipfile

def extract_archive(archive_path, dest_folder):
    with zipfile.ZipFile(archive_path, 'r') as archiue:
        archiue.extractall(dest_folder)


if __name__ == "--main__":
    extract_archive("archive_extractor/compressed.zip", "archive_extractor/dest_folder_example")