from time import sleep
from state import State
from utils import print_map
from logging import basicConfig, warning, info
from rich.logging import RichHandler

FORMAT = "%(message)s"
basicConfig(level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()])

state = State()


def inspect():
    x, y = state.agent.position()

    match state.original_cave[y][x]:
        case "p":
            return ["Pit"]
        case "b":
            return ["Breeze"]
        case "w":
            return ["Wumpus"]
        case "s":
            return ["Stench"]
        case "tsb":
            return ["Glitter", "Stench", "Breeze"]
        case " " | "a":
            return ["Safe"]
        case _:
            return []


def process():
    found_teasure = False
    _exit = None

    while True:

        def log(call, text: str):
            def toStr(it):
                return ", ".join(map(str, it))

            call(
                f"{text} position={state.agent.position()} unsafe_positions={toStr(state.agent.unsafe_positions)} safe_positions={toStr(state.agent.safe_positions)}"
            )

        if found_teasure:
            if _exit:
                state.agent.x, state.agent.y = _exit
                break

        inspection = inspect()
        for attr in inspection:
            match attr:
                case "Safe":
                    if not _exit:
                        _exit = state.agent.position()
                    log(info, "safe position moving forward")
                    state.agent.safe_positions.append(state.agent.position())
                    state.agent.forward()

                    if state.agent.position() in state.agent.seen:
                        log(info, "I alreadly seen is place. Turning right.")
                        state.agent.turn(True)
                        continue

                    if state.agent.in_wall():
                        log(warning, "Found a wall. Turning right")
                        state.agent.turn(True)

                case "Breeze":
                    x, y = state.agent.position()
                    log(warning, "found breeze position")
                    state.agent.safe_positions.append(state.agent.position())

                    state.agent.unsafe_positions.add((x, y + 1))
                    state.agent.unsafe_positions.add((x + 1, y))
                    state.agent.seen.add(state.agent.position())

                    log(info, "rolling back to safe position")
                    safex, safey = list(
                        filter(
                            lambda p: p != state.agent.position(),
                            state.agent.safe_positions,
                        )
                    )[0]
                    state.agent.x = safex
                    state.agent.y = safey

                case "Stench":
                    log(warning, "here is a stench. Wumpus may be here.")
                    x, y = state.agent.position()
                    state.agent.safe_positions.append(state.agent.position())
                    state.agent.unsafe_positions.add((x, y + 1))
                    log(info, "y+1 may be unsafe. so i'm going to x+1")
                    state.agent.x += 1
                case "Glitter":
                    log(info, "AYO Found glitter here, so teasure is here!")
                    log(info, "Trying to leave the cave")
                    found_teasure = True
                    state.agent.safe_positions.append(state.agent.position())
                case not_handled:
                    log(warning, f"Not handled: {not_handled}")

        print_map(state)
        sleep(0.5)


state.next_generation()
info(f"started generation={state.generation}")
print_map(state)
process()
print_map(state)
