"""
=============================================================
 O — Open/Closed Principle (OCP)
=============================================================
 "Software entities should be open for extension but closed
  for modification."

 New discount types are added by creating new strategy classes
 — the calculator never needs to be modified.
=============================================================
"""

from abc import ABC, abstractmethod


# ── Bad example ────────────────────────────────────────────

class DiscountCalculatorBad:
    """Violates OCP: must be modified every time a new type appears."""

    def calculate(self, customer_type: str, price: float) -> float:
        if customer_type == "regular":
            return price * 0.95
        elif customer_type == "premium":
            return price * 0.80
        elif customer_type == "vip":
            return price * 0.70
        return price


# ── Good example ───────────────────────────────────────────

class DiscountStrategy(ABC):
    """Abstraction for discount calculation."""

    @abstractmethod
    def calculate(self, price: float) -> float: ...


class RegularDiscount(DiscountStrategy):
    def calculate(self, price: float) -> float:
        return price * 0.95


class PremiumDiscount(DiscountStrategy):
    def calculate(self, price: float) -> float:
        return price * 0.80


class VIPDiscount(DiscountStrategy):
    def calculate(self, price: float) -> float:
        return price * 0.70


class DiscountCalculator:
    """Closed for modification, open for extension via strategies."""

    def __init__(self, strategy: DiscountStrategy) -> None:
        self._strategy = strategy

    def calculate(self, price: float) -> float:
        return self._strategy.calculate(price)


# ── Demo ───────────────────────────────────────────────────

def demo() -> None:
    print("=" * 60)
    print(" OCP — Open/Closed Principle")
    print("=" * 60)

    base_price = 100.0

    print(f"\n  Base price: ${base_price:.2f}")

    print("\n❌ Bad (modify the calculator for each new type):")
    bad_calc = DiscountCalculatorBad()
    for ctype in ("regular", "premium", "vip"):
        result = bad_calc.calculate(ctype, base_price)
        print(f"  {ctype:>8}: ${result:.2f}")

    print("\n✅ Good (extend with new strategy classes):")
    strategies: list[tuple[str, DiscountStrategy]] = [
        ("Regular", RegularDiscount()),
        ("Premium", PremiumDiscount()),
        ("VIP", VIPDiscount()),
    ]
    for label, strategy in strategies:
        calc = DiscountCalculator(strategy)
        result = calc.calculate(base_price)
        print(f"  {label:>8}: ${result:.2f}")
    print()
