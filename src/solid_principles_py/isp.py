"""
=============================================================
 I — Interface Segregation Principle (ISP)
=============================================================
 "Clients should not be forced to depend on interfaces
  they do not use."

 Instead of one fat Worker interface, we split it into
 small, focused abstractions (Workable, Eatable, Sleepable).
 Each class implements only what it actually needs.
=============================================================
"""

from abc import ABC, abstractmethod


# ── Bad example ────────────────────────────────────────────

class WorkerBad(ABC):
    """Fat interface: forces every implementor to define all methods."""

    @abstractmethod
    def work(self) -> None: ...

    @abstractmethod
    def eat(self) -> None: ...

    @abstractmethod
    def sleep(self) -> None: ...


class HumanWorkerBad(WorkerBad):
    def work(self) -> None:
        print("  Human working...")

    def eat(self) -> None:
        print("  Human eating...")

    def sleep(self) -> None:
        print("  Human sleeping...")


class RobotBad(WorkerBad):
    """Violates ISP: forced to implement eat() and sleep()."""

    def work(self) -> None:
        print("  Robot working...")

    def eat(self) -> None:
        pass  # Robots don't eat!

    def sleep(self) -> None:
        pass  # Robots don't sleep!


# ── Good example ───────────────────────────────────────────

class Workable(ABC):
    @abstractmethod
    def work(self) -> None: ...


class Eatable(ABC):
    @abstractmethod
    def eat(self) -> None: ...


class Sleepable(ABC):
    @abstractmethod
    def sleep(self) -> None: ...


class Human(Workable, Eatable, Sleepable):
    def work(self) -> None:
        print("  Human working...")

    def eat(self) -> None:
        print("  Human eating...")

    def sleep(self) -> None:
        print("  Human sleeping...")


class Robot(Workable):
    """Implements only what makes sense — no empty stubs."""

    def work(self) -> None:
        print("  Robot working...")


# ── Demo ───────────────────────────────────────────────────

def demo() -> None:
    print("=" * 60)
    print(" ISP — Interface Segregation Principle")
    print("=" * 60)

    print("\n❌ Bad (Robot forced to implement eat/sleep):")
    bad_human = HumanWorkerBad()
    bad_robot = RobotBad()
    bad_human.work()
    bad_human.eat()
    bad_human.sleep()
    bad_robot.work()
    bad_robot.eat()   # does nothing — empty stub
    bad_robot.sleep()  # does nothing — empty stub
    print("  (Robot.eat() and Robot.sleep() are empty stubs ⚠️)")

    print("\n✅ Good (each class implements only relevant interfaces):")
    human = Human()
    robot = Robot()
    human.work()
    human.eat()
    human.sleep()
    robot.work()
    print(f"  Robot interfaces: {[c.__name__ for c in type(robot).__mro__ if c not in (Robot, object)]}")
    print()
