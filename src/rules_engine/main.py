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


def main():
    print("hello world")


if __name__ == '__main__':
    main()
