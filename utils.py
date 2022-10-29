from state import State

from rich import print


def print_map(state: State):
    state.update_map()
    print()
    for key in state.cave:
        for value in key:
            print(
                value.replace("tsb", "t")
                .replace("a", "[magenta]a[/magenta]")
                .replace("b", "[red]b[/red]")
                .replace("p", "[black]p[/black]")
                .replace("s", "[green]s[/green]")
                .replace("w", "[cyan]w[/cyan]"),
                end=" ",
            )
        print("----")
