"""TODO"""
from src.rules_engine.main import (
    evaluate,
    And,
    Operator,
    Or,
    Rule,
)
import pytest

# Either:
#   credit_rating is above 50
#   AND
#   flood_risk is below 10
# OR
#   revenue is above 1000000
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


class TestMain:
    def test_evaluate(self):
        assert evaluate(RULE_1, EXAMPLE_1) == EXAMPLE_1_EXP

    @pytest.mark.parametrize(
        "rule,data,exp",
        (
            # Single rules.
            (("credit_rating", "above", 50), EXAMPLE_1, True),
            (("credit_rating", "below", 50), EXAMPLE_1, False),
            (("flood_risk", "below", 10), EXAMPLE_1, True),
            (("flood_risk", "above", 10), EXAMPLE_1, False),
            (("flood_risk", "equals", 5), EXAMPLE_1, True),
            (("flood_risk", "equals", 10), EXAMPLE_1, False),
            # multiple rules.
            # TODO: Add Red test
            # ([("credit_rating", "above", 50), ("flood_risk", "below", 10)], EXAMPLE_1, True),
        )
    )
    def test_evaluate1(self, rule, data, exp):
        assert evaluate(rule, data) == exp

    @pytest.mark.parametrize(
        "a,b,operator,exp",
        (
            (5, 10, Operator.less_than, True),
            (5, 10, Operator.less_than_equal, True),
            (5, 5, Operator.less_than_equal, True),
            (10, 5, Operator.greater_than, True),
            (10, 5, Operator.greater_than_equal, True),
            (10, 10, Operator.greater_than_equal, True),
            (10, 10, Operator.equal, True),
            (10, 5, Operator.not_equal, True),
        )
    )
    def test_rule(self, a, b, operator, exp):
        assert Rule(a, b, operator).execute() == exp

    @pytest.mark.parametrize(
        "msg,rules,exp",
        (
            ("All rules return True", (Rule(5, 10, Operator.less_than), Rule(10, 5, Operator.greater_than)), True),
            ("First Rule returns False", (Rule(10, 5, Operator.less_than), Rule(10, 5, Operator.greater_than)), False),
            ("Second Rule returns False", (Rule(5, 10, Operator.less_than), Rule(5, 10, Operator.greater_than)), False),
            ("All rules return False", (Rule(10, 5, Operator.less_than), Rule(5, 10, Operator.greater_than)), False),
        )
    )
    def test_and(self, msg, rules, exp):
        print(f"Debug: {msg!r}")
        assert And(rules).execute() == exp

    @pytest.mark.parametrize(
        "msg,rules,exp",
        (
            ("All rules return True", (Rule(5, 10, Operator.less_than), Rule(10, 5, Operator.greater_than)), True),
            ("First Rule returns False", (Rule(10, 5, Operator.less_than), Rule(10, 5, Operator.greater_than)), True),
            ("Second Rule returns False", (Rule(5, 10, Operator.less_than), Rule(5, 10, Operator.greater_than)), True),
            ("All rules return False", (Rule(10, 5, Operator.less_than), Rule(5, 10, Operator.greater_than)), False),
        )
    )
    def test_or(self, msg, rules, exp):
        print(f"Debug: {msg!r}")
        assert Or(rules).execute() == exp

    def test_combined_and_or_rules(self):
        combined_rule = Or(
            (
                And((Rule(1, 1, Operator.equal),)),  # True
                And((Rule(2, 2, Operator.not_equal),)),  # False
            )
        )  # True
        assert combined_rule.execute() is True
