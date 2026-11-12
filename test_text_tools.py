import pytest

from text_tools import clean_question, count_words, check_question, is_greeting, make_message, starts_with_question_word   # import the functions we want to test


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


def test_is_greetings_for_greeting():
    assert is_greeting("Hi") == True

def test_is_greetings_for_non_greeting():
    assert is_greeting("Toh") == False

def test_is_greetings_for_spaced_greeting():
    assert is_greeting("  HeLLo ") == True


def test_make_message_valid_message():
    assert make_message("user", "What is Rag") == {"role": "user", "content": "What is Rag"}

def test_make_message_invalid_role():
    with pytest.raises(ValueError):  # because we cannot assert the wrong one == error, so we use with pytest.raises mean I expect here got error, if no error, crash
        make_message("robot", "Hello")


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



@pytest.mark.parametrize("text, expected", [
    ("Hello", False),
    ("What", True),
    ("   HoW  ", True)
])
def test_starts_word(text, expected):
    assert starts_with_question_word(text) == expected