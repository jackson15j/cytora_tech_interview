"""TODO"""
from src.rules_engine.main import (
    evaluate,
    Operator,
    Rule,
)
import pytest


RULE_1 = ("TODO","TODO","TODO")
EXAMPLE_1 = {
    "credit_rating": 75,
    "flood_risk": 5,
    "revenue": 1000
}
EXAMPLE_1_EXP = True


class TestMain:
    @pytest.mark.skip("TODO")
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
