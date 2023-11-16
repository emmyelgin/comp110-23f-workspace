"""For loop practice."""

_author_ = "730464992"

pets: list[str] = ["Louie", "Bo", "Bear"]
for item in pets:
    print(f"Good boy{item}!")


names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0, 3):
    elem: str = names[idx]
    print(f"{idx}:{elem}")