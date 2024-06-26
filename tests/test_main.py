"""Test of rules engine and problem requirements"""
from src.rules_engine.engine import (
    evaluate,
    And,
    Operator,
    Or,
    Rule,
)
from src.rules_engine.main import(
    EXAMPLE_1,
    EXAMPLE_1_EXP,
    RULE_1,
)
import pytest


class TestMain:
    def test_evaluate(self):
        assert evaluate(RULE_1, EXAMPLE_1) == EXAMPLE_1_EXP

    @pytest.mark.parametrize(
        "rule,data,exp",
        (
            # Single rules.
            (Rule("credit_rating", 50, Operator.greater_than), EXAMPLE_1, True),
            (Rule("credit_rating", 50, Operator.less_than), EXAMPLE_1, False),
            (Rule("flood_risk", 10, Operator.less_than), EXAMPLE_1, True),
            (Rule("flood_risk", 10, Operator.greater_than), EXAMPLE_1, False),
            (Rule("flood_risk", 5, Operator.equal), EXAMPLE_1, True),
            (Rule("flood_risk", 10, Operator.equal), EXAMPLE_1, False),
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
