from demo.cli import parse_args


def main() -> None:
    cliargs = parse_args()
    command = cliargs.command(cliargs=cliargs)
    command()


if __name__ == "__main__":
    main()