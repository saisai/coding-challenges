"""
Validate Balanced Parentheses

This problem was recently asked by Uber:

Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced. Every opening bracket must have a corresponding closing bracket.
We can approximate this using strings.

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.

Example:
Input: "((()))"
Output: True

Input: "[()]{}"
Output: True

Input: "({[)]"
Output: False

"""


def solution(string: str) -> str:
    stack = []

    mapping = {"[": "]", "(": ")", "{": "}"}

    for value in string:
        if value in mapping:
            stack.append(value)
            continue

        if mapping[stack.pop()] != value:
            return False

    return True if not stack else False


if __name__ == "__main__":
    string = "((()))"
    assert solution(string) is True
    print(f"Solution({string}) -> ", solution(string))

    string = "([{}])()"
    assert solution(string) is True
    print(f"Solution({string}) -> ", solution(string))

    string = "()(){(())"
    assert solution(string) is False
    print(f"Solution({string}) -> ", solution(string))
