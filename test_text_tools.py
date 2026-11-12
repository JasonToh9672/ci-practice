import pytest

from text_tools import clean_question, count_words, check_question, is_greeting, make_message   # import the functions we want to test


def test_clean_question_removes_spaces_and_lowercases():   # a test = a function whose name starts with test_
    assert clean_question("  What Time?  ") == "what time?"   # I expect THIS input to give THIS output


def test_count_words_counts_each_word():
    assert count_words("we open at 9am") == 4


def test_count_words_empty_text_is_zero():
    assert count_words("") == 0                             # also test the "edge case": empty text

def test_check_question_empty_raises_error():
    with pytest.raises(ValueError):                    # "inside this block, I EXPECT a ValueError"
        check_question("   ")                          # this should raise it


def test_check_question_returns_stripped_text():
    assert check_question("  hi  ") == "hi"            # and the normal case still works

# 1
def test_is_greetings_for_greeting():
    assert is_greeting("Hi") == True

def test_is_greetings_for_non_greeting():
    assert is_greeting("Toh") == False

def test_is_greetings_for_spaced_greeting():
    assert is_greeting("  HeLLo ") == True

# 2
def test_make_message_valid_message():
    assert make_message("user", "What is Rag") == {"role": "user", "content": "What is Rag"}

def test_make_message_invalid_role():
    with pytest.raises(ValueError):  # because we cannot assert the wrong one == error, so we use with pytest.raises mean I expect here got error, if no error, crash
        make_message("robot", "Hello")

# 8

@pytest.mark.parametrize(
    "text, expected", # 1) Parameter name in @pytest.mark.parametrize must match with parameter in test function
    [
        ("Hi", True),
        ("Toh", False),
        ("  HeLLo ", True)
    ]
)
def test_greeting(text, expected): # 2) The parameters in test function must match the Parameter name in @pytest.mark.parametrize
    assert is_greeting(text) == expected

"""
What parametrize is for

Your 3 is_greeting tests from exercise 1 probably look almost the same:

def test_hi_is_greeting():
    assert is_greeting("Hi") == True

def test_toh_is_not_greeting():
    assert is_greeting("Toh") == False

def test_hello_with_spaces_is_greeting():
    assert is_greeting("  HeLLo ") == True

Only two things change each time: the input text and the expected answer. parametrize lets you write the test once, and give pytest a list of (input, expected) pairs to fill in. It’s like a form letter: one letter, with only the name changing for each person.

A different example (so you can do yours yourself)

Testing count_words:

@pytest.mark.parametrize(
    "text, expected",              # 1st thing: the NAMES of the blanks, in ONE string, separated by a comma
    [                              # 2nd thing: the LIST of values to fill in
        ("we open at 9am", 4),     # 1st run: text = "we open at 9am", expected = 4
        ("", 0),                   # 2nd run: text = "",               expected = 0
        ("hello", 1),              # 3rd run: text = "hello",          expected = 1
    ],
)
def test_count_words(text, expected):        # the function's parameters must use the SAME names
    assert count_words(text) == expected

What happens:

1) pytest reads the names: "text, expected". That’s one string with both names inside it, separated by a comma. (That was the bug: you wrote them as two separate strings, "input", "expected".)
2) It takes the first pair ("we open at 9am", 4), sets text = "we open at 9am" and expected = 4, and runs the test.
3) Then it does the same for each pair. 3 pairs = 3 separate tests.
4) In python -m pytest -v, you’ll see 3 results, one per pair, like test_count_words[hello-1] PASSED. So if one fails, you know exactly which pair broke.

So parametrize always takes exactly 2 things:

	            What	                            Example
1st	    names of the blanks, in one string	    "text, expected"
2nd	    a list of tuples, one tuple per test	[("hello", 1), ...]
"""

# put @pytest.mark.parametrize on top of the test function
# make sure the blanks names sames as the test function parameter
"""

How the Mapping Works

import pytest

def add(a, b):
    return a + b

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected

When pytest reads @pytest.mark.parametrize("a, b, expected", [...]), it splits that string by commas to get three parameter names: a, b, and expected.
For the first tuple (2, 3, 5), pytest assigns the values by position:
• a gets 2
• b gets 3
• expected gets 5
Then, pytest calls test_add(a=2, b=3, expected=5). It repeats this process for the next tuple (-1, 1, 0), and so on.

Key Rules to Remember

• Exact Name Match. The names inside the string must match the parameter names in def test_add(a, b, expected):. If you write "x, y, expected" in the decorator but keep def test_add(a, b, expected):, pytest will throw a fixture lookup error.
• Any Valid Names Work. The names "a", "b", and "expected" are just conventions, not special pytest keywords. You can name them whatever makes sense for your test, such as "username, password, is_valid".
• Count Must Match. The number of names in the string must match the number of items inside each tuple. Three names require tuples of three items.
• Single Parameter Exception. If you only test one parameter (e.g., "number"), you pass a flat list of values [1, 2, 3] instead of a list of tuples.
"""