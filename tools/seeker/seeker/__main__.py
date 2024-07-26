from pathlib import Path
from seeker.seeker import print_files_in_directory


def main() -> None:
    print_files_in_directory(Path.cwd())


if __name__ == "__main__":
    main()
