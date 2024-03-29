"""TODO"""
from src.rules_engine.main import evaluate
import pytest


RULE_1 = ("TODO","TODO","TODO")
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
            (("credit_rating", "above", 50), EXAMPLE_1, True),
            (("flood_risk", "below", 10), EXAMPLE_1, True),
            (("flood_risk", "equals", 5), EXAMPLE_1, True),
        )
    )
    def test_evaluate1(self, rule, data, exp):
        assert evaluate(rule, data) == exp
