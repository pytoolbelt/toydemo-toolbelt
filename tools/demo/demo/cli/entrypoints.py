from pytoolbelt.toolkit.clitools import PyToolBeltCommand


class Demo(PyToolBeltCommand):

    args = {
        ("-f", "--foo"): {
            "help": "This is a foo argument",
            "action": "store_true"
        },

        ("-b", "--bar"): {
            "help": "This is a bar argument",
            "action": "store_true"
        },

        ("action",): {
            "help": "This is an action argument",
            "choices": ["act1", "act2", "act3"]
        }
    }

    help = "This is a test command"

    def __call__(self) -> int:
        action = getattr(self, self.cliargs.action)
        return action()

    def _print_foo_bar(self) -> None:
        print(f"foo is {self.cliargs.foo} -- bar is {self.cliargs.bar}")

    def act1(self) -> int:
        print("This is demo action 1")
        self._print_foo_bar()
        return 0

    def act2(self) -> int:
        print("This is demo action 2")
        self._print_foo_bar()
        return 0

    def act3(self) -> int:
        print(f"This is demo action 3")
        self._print_foo_bar()
        return 0