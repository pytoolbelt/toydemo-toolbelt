from pytoolbelt.toolkit.clitools import PyToolBeltCommand
from . import entrypoints

__version__ = "0.0.0"


def parse_args():
    return PyToolBeltCommand.parse(__version__, entrypoints)