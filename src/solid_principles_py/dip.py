"""
=============================================================
 D — Dependency Inversion Principle (DIP)
=============================================================
 "High-level modules should not depend on low-level modules.
  Both should depend on abstractions."

 UserService depends on the Database abstraction, not on a
 concrete implementation. The concrete DB is injected at
 construction time.
=============================================================
"""

from abc import ABC, abstractmethod


# ── Bad example ────────────────────────────────────────────

class MySQLDatabaseBad:
    def execute(self, query: str) -> str:
        return f"MySQL executing: {query}"


class UserServiceBad:
    """Violates DIP: tightly coupled to MySQLDatabaseBad."""

    def __init__(self) -> None:
        self._db = MySQLDatabaseBad()  # hard dependency

    def get_users(self) -> str:
        return self._db.execute("SELECT * FROM users")


# ── Good example ───────────────────────────────────────────

class Database(ABC):
    """Abstraction that both high- and low-level modules depend on."""

    @abstractmethod
    def connect(self) -> str: ...

    @abstractmethod
    def execute(self, query: str) -> str: ...


class MySQLDatabase(Database):
    def connect(self) -> str:
        return "Connected to MySQL"

    def execute(self, query: str) -> str:
        return f"MySQL executing: {query}"


class PostgreSQLDatabase(Database):
    def connect(self) -> str:
        return "Connected to PostgreSQL"

    def execute(self, query: str) -> str:
        return f"PostgreSQL executing: {query}"


class SQLiteDatabase(Database):
    def connect(self) -> str:
        return "Connected to SQLite"

    def execute(self, query: str) -> str:
        return f"SQLite executing: {query}"


class UserService:
    """Depends on the abstraction (Database), not on any concrete DB."""

    def __init__(self, db: Database) -> None:
        self._db = db

    def get_users(self) -> str:
        return self._db.execute("SELECT * FROM users")


# ── Demo ───────────────────────────────────────────────────

def demo() -> None:
    print("=" * 60)
    print(" DIP — Dependency Inversion Principle")
    print("=" * 60)

    print("\n❌ Bad (high-level module hardwires low-level module):")
    bad_service = UserServiceBad()
    print(f"  {bad_service.get_users()}")
    print("  (Switching DB requires rewriting UserServiceBad ⚠️)")

    print("\n✅ Good (inject any Database implementation):")
    databases: list[Database] = [
        MySQLDatabase(),
        PostgreSQLDatabase(),
        SQLiteDatabase(),
    ]
    for db in databases:
        db_name = type(db).__name__
        service = UserService(db)
        print(f"  [{db_name:<20}] {service.get_users()}")
    print()
