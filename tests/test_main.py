"""TODO"""
from src.rules_engine.main import evaluate

RULE_1 = "TODO"
EXAMPLE_1 = {
    "credit_rating": 75,
    "flood_risk": 5,
    "revenue": 1000
}
EXAMPLE_1_EXP = True


class TestMain:
    def test_evaluate(self):
        assert evaluate(RULE_1, EXAMPLE_1) == EXAMPLE_1_EXP
