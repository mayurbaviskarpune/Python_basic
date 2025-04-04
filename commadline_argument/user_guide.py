import argparse

parser = argparse.ArgumentParser(description="add details about the script")

parser.add_argument("-a","--num",default=10,help="eneter a number")
parser.add_argument("-env","--environment",help="enter a environment",required=True)

args = parser.parse_args()

print(args.num)
print(args.environment)
    # *name_or_flags: str,
    # action: str | type[Action] = ...,
    # nargs: int | str | None = None,
    # const: Any = ...,
    # default: Any = ...,
    # type: _ActionType = ...,
    # choices: Iterable[_T@add_argument] | None = ...,
    # required: bool = ...,
    # help: str | None = ...,
    # metavar: str | tuple[str, ...] | None = ...,
    # dest: str | None = ...,
    # version: str = ...,
    # **kwargs: Any