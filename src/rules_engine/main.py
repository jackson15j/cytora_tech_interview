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


def evaluate(rule, data: dict) -> bool:
    # TODO: Handle multiple rules.
    # TODO: Handle AND.
    # TODO: Handle other operators.
    obj, operator, value = rule
    v = data.get(obj, None)
    if v is None:
        return False
    if operator == "below":
        if v < value:
            return True
    if operator == "above":
        if v > value:
            return True
    if operator == "equals":
        if v == value:
            return True
    return False


@dataclass
class Rule:
    """Comparison rule instance."""
    a: int
    b: int
    operator: Operator

    def execute(self):
        return self.operator.value(self.a, self.b)


@dataclass
class And:
    """And together the results of all executed rules."""
    rules: list[Rule]

    def execute(self):
        return all(x.execute() for x in self.rules)


def main():
    print("hello world")


if __name__ == '__main__':
    main()
