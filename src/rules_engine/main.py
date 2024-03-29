""" TODO: Cytora Main docstring."""


def evaluate(rule, data: dict) -> bool:
    # TODO: Handle multiple rules.
    # TODO: Handle AND.
    # TODO: Handle other operators.
    obj, operator, value = rule
    v = data.get(obj, None)
    if v is None:
        return False
    if operator == "above":
        if v > value:
            return True
    return False


def main():
    print("hello world")


if __name__ == '__main__':
    main()
