"""Cytora Main docstring. Executes the rules engine as per README."""
from rules_engine.engine import (
    evaluate,
    And,
    Operator,
    Or,
    Rule,
)

RULE_TEXT = """
Either:
  credit_rating is above 50
  AND
  flood_risk is below 10
OR
  revenue is above 1000000
"""
RULE_1 = Or(
    (
        And(
            (
                Rule("credit_rating", 50, Operator.greater_than),  # True
                Rule("flood_risk", 10, Operator.less_than),  # True
            )
        ),  # True
        Rule("revenue", 1000000, Operator.greater_than),  # False
    )
)  # True

EXAMPLE_1 = {
    "credit_rating": 75,
    "flood_risk": 5,
    "revenue": 1000
}
EXAMPLE_1_EXP = True


def main():
    print(f"Rule:\n{RULE_TEXT!r}\n\nIs represented as:\n\n{RULE_1!r}\n")
    print(
        f"Using the following data, should evaluate as: "
        f"{EXAMPLE_1_EXP!r}\n\n{EXAMPLE_1!r}\n"
    )
    print("Evaluation:", evaluate(RULE_1, EXAMPLE_1))


if __name__ == '__main__':
    main()
