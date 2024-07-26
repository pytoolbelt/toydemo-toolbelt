from pathlib import Path


def print_files_in_directory(directory: Path) -> None:
    for path in directory.iterdir():
        if path.is_file():
            print(path)
