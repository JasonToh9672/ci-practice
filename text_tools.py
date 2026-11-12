def clean_question(text):
    return text.strip().lower()           # remove spaces at both ends, then make lowercase


def count_words(text):
    return len(text.split())              # split into a list of words, then count them


def check_question(text):
    if text.strip() == "":                # only spaces, or nothing at all
        raise ValueError("Question cannot be empty")
    return text.strip()
# 1
def is_greeting(text):
    cleaned_text = clean_question(text)
    return cleaned_text in ["hi", "hello", "hey"]

# 2
def make_message(role, content):
    if role not in ["user", "bot"]:
        raise ValueError("The role must be user or bot")
    else:
        return {"role": role, "content": content}

# 3
"""
test_text_tools.py .F........                                                                                                        [100%]

================================================================ FAILURES =================================================================
____________________________________________________ test_count_words_counts_each_word ____________________________________________________

    def test_count_words_counts_each_word():
>       assert count_words("we open at 9am") == 4
E       AssertionError: assert 14 == 4
E        +  where 14 = count_words('we open at 9am')

test_text_tools.py:11: AssertionError
========================================================= short test summary info =========================================================
FAILED test_text_tools.py::test_count_words_counts_each_word - AssertionError: assert 14 == 4
======================================================= 1 failed, 9 passed in 0.13s =======================================================
"""
# because in test_count_words_counts_each_word(), we assert the sentence is count as words instead of characters
# without .split(), it counts the characters including the space, so assert count_words("we open at 9am") == 4
# because "we open at 9am" is 14 characters including space, so give assertion error
# fix it back to count words, len(text.split()) in count_words()
