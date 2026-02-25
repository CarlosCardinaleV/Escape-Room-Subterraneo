# Underground Escape Room

A turn-based console/GUI Python project where teams of players survive three caves by casting gem-based spells against cave locks.

## What This Project Contains

- A dataclass-based domain model for gems, players, teams, caves, locks, and spells.
- A console game runner in `src/ScapeRoomConsole.py`.
- A basic GUI helper in `src/InterfazGUI.py` for dialog-based input/output experiments.

## Core Game Concepts

The game is built around 3 resources:

- Gem health: each player has 3 gems.
- Player life: if all 3 gems of a player reach 0, that player dies.
- Cave oxygen: each cave starts with oxygen and loses it each spell round.

### Team and Progression

- Each team has exactly 3 players.
- The game has 3 caves.
- Each cave has 1 lock for that stage.
- Destroy all lock gems in cave 1 to reach cave 2, then cave 3.

### Combat Rules

Each attack round:

1. A player chooses one of their gems.
2. The team chooses one target gem on the cave lock.
3. Damage depends on attack, defense, gem type, and spell duration.

Type advantage is:

- FIRE beats METAL
- METAL beats WATER
- WATER beats FIRE

If gem types are equal, both sides take damage.

### Oxygen and Lethality

Each cave has base lethality:

- Cave 1: 0.2
- Cave 2: 0.3
- Cave 3: 0.4

After each group spell round, cave oxygen decreases by current lethality.

If players die, lethality is reduced for that cave:

- After first death: lethality becomes half.
- After second death: lethality becomes quarter of base.

### Lose and Win Conditions

You lose if:

- Cave oxygen reaches 0, or
- All players in the team are dead.

You win if:

- The team destroys lock gems in all 3 caves.

## Project Structure

- `src/Gem.py`: gem model (type, owner, health, attack, defense)
- `src/Player.py`: player model (3 gems, oxygen, alive state)
- `src/Team.py`: team model (3 players, team alive state)
- `src/Lock.py`: lock model (3 random cave gems)
- `src/Cave.py`: cave model (locks, oxygen levels, lethality levels)
- `src/Spell.py`: spell model and combat operations
- `src/ScapeRoomConsole.py`: main console implementation
- `src/InterfazGUI.py`: Tkinter GUI helper for input dialogs

## Requirements

- Python 3.9+
- No external dependencies required (uses standard library only)

## Setup

From project root:

```bash
cd src
```

(Or run commands from root using `python3 src/...`.)

## How to Run

### Console Game (main playable flow)

From project root:

```bash
python3 src/ScapeRoomConsole.py
```

You will be prompted for:

- Number of teams
- Team name
- Three player names
- Per-round spell duration
- Gem choices for players and lock targets

### GUI Demo

From project root:

```bash
python3 src/InterfazGUI.py
```

This starts a simple Tkinter dialog flow (not the full game loop).

## Typical Console Round

1. Team enters a cave.
2. For each alive player, choose an attacking gem and lock target gem.
3. Resolve combat.
4. Check for player deaths.
5. Oxygen decreases by cave lethality.
6. Check loss/win conditions.
7. Continue casting or abandon.

## Notes About Current Implementation

- The console flow is fully dataclass-compatible with current models.
- Cave status and lock status are shown each round.
- Best progress tracking is included (`best team so far`).
- Combat and survival behavior are deterministic from gem stats and player inputs.

## Troubleshooting

- `ModuleNotFoundError`: run from project root (`python3 src/ScapeRoomConsole.py`) so imports resolve as expected.
- Input errors: the console runner validates integer/float input and will re-prompt.
- Unexpected balance: gem attack/defense values are randomized at creation; each run can feel different.

## License

This project is licensed under the MIT License. See [LICENSE](./LICENSE).
