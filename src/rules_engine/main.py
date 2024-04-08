""" TODO: Cytora Main docstring."""
import operator
from dataclasses import dataclass
from enum import Enum


class Operator(Enum):
    less_than = operator.lt
    less_than_equal = operator.le
    greater_than = operator.gt
    greater_than_equal = operator.ge
    equal = operator.eq
    not_equal = operator.ne


@dataclass
class Rule:
    """Comparison rule instance."""
    a: int
    b: int
    operator: Operator

    def execute(self, data: dict = {}) -> bool:
        if data:
            # Assuming `self.a` is the dict Key instead of the value,
            # which I was initially using in early testing.
            self.a = data[self.a]
        return self.operator.value(self.a, self.b)


@dataclass
class And:
    """And together the results of all executed rules."""
    rules: list  # list['And'|'Or'|Rule]|tuple['And'|'Or'|Rule]

    def execute(self, data: dict = {}) -> bool:
        return all(x.execute(data) for x in self.rules)


@dataclass
class Or:
    """Or together the results of all executed rules."""
    rules: list  # list[And|'Or'|Rule]|tuple[And|'Or'|Rule]

    def execute(self, data: dict = {}) -> bool:
        return any(x.execute(data) for x in self.rules)


def evaluate(rules, data: dict = {}) -> bool:
    return rules.execute(data)

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
