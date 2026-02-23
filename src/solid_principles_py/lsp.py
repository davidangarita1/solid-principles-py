"""
=============================================================
 L — Liskov Substitution Principle (LSP)
=============================================================
 "Subtypes must be substitutable for their base types
  without altering the correctness of the program."

 Every subclass of Bird honours the move() contract,
 so client code never encounters surprising exceptions.
=============================================================
"""

from abc import ABC, abstractmethod


# ── Bad example ────────────────────────────────────────────

class BirdBad:
    def fly(self) -> str:
        return "Flying high!"


class PenguinBad(BirdBad):
    """Violates LSP: breaks the fly() contract."""

    def fly(self) -> str:
        raise NotImplementedError("Penguins can't fly!")


# ── Good example ───────────────────────────────────────────

class Bird(ABC):
    """Base abstraction with a general movement contract."""

    @abstractmethod
    def move(self) -> str: ...


class Sparrow(Bird):
    def move(self) -> str:
        return "Flying high!"


class Penguin(Bird):
    def move(self) -> str:
        return "Swimming fast!"


class Ostrich(Bird):
    def move(self) -> str:
        return "Running swiftly!"


def make_bird_move(bird: Bird) -> str:
    """Works with ANY Bird — the contract is always honoured."""
    return bird.move()


# ── Demo ───────────────────────────────────────────────────

def demo() -> None:
    print("=" * 60)
    print(" LSP — Liskov Substitution Principle")
    print("=" * 60)

    print("\n❌ Bad (substituting Penguin breaks the program):")
    bad_bird = BirdBad()
    print(f"  BirdBad   → {bad_bird.fly()}")
    try:
        bad_penguin = PenguinBad()
        bad_penguin.fly()
    except NotImplementedError as exc:
        print(f"  PenguinBad → 💥 {exc}")

    print("\n✅ Good (every Bird can be substituted safely):")
    birds: list[Bird] = [Sparrow(), Penguin(), Ostrich()]
    for bird in birds:
        label = type(bird).__name__
        print(f"  {label:<8} → {make_bird_move(bird)}")
    print()
