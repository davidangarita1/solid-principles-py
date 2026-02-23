"""
=============================================================
 S — Single Responsibility Principle (SRP)
=============================================================
 "A class should have only one reason to change."

 Each class encapsulates a single concern:
   • User        → holds user data
   • UserRepository → persistence logic
   • EmailService   → notification logic
=============================================================
"""


# ── Bad example ────────────────────────────────────────────

class UserBad:
    """Violates SRP: mixes data, persistence, and notifications."""

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def save_to_database(self) -> None:
        print(f"  [DB]    Saving {self.name} to database...")

    def send_welcome_email(self) -> None:
        print(f"  [EMAIL] Sending welcome email to {self.email}...")


# ── Good example ───────────────────────────────────────────

class User:
    """Only responsible for holding user data."""

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def __repr__(self) -> str:
        return f"User(name={self.name!r}, email={self.email!r})"


class UserRepository:
    """Only responsible for persisting users."""

    def save(self, user: User) -> None:
        print(f"  [DB]    Saving {user.name} to database...")


class EmailService:
    """Only responsible for sending emails."""

    def send_welcome_email(self, user: User) -> None:
        print(f"  [EMAIL] Sending welcome email to {user.email}...")


# ── Demo ───────────────────────────────────────────────────

def demo() -> None:
    print("=" * 60)
    print(" SRP — Single Responsibility Principle")
    print("=" * 60)

    print("\n❌ Bad (one class does everything):")
    bad_user = UserBad("Alice", "alice@example.com")
    bad_user.save_to_database()
    bad_user.send_welcome_email()

    print("\n✅ Good (each class has one responsibility):")
    user = User("Alice", "alice@example.com")
    repo = UserRepository()
    email_svc = EmailService()

    repo.save(user)
    email_svc.send_welcome_email(user)
    print()
