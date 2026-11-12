def clean_question(text):
    return text.strip().lower()           # remove spaces at both ends, then make lowercase


def count_words(text):
    return len(text.split())              # split into a list of words, then count them


def check_question(text):
    if text.strip() == "":                # only spaces, or nothing at all
        raise ValueError("Question cannot be empty")
    return text.strip()

def is_greeting(text):
    cleaned_text = clean_question(text)
    return cleaned_text in ["hi", "hello", "hey"]

def make_message(role, content):
    if role not in ["user", "bot"]:
        raise ValueError("The role must be user or bot")
    else:
        return {"role": role, "content": content}

# 5
def starts_with_question_word(text):
    return text.strip().lower().startswith(("what", "where", "when", "how"))

# (text.startswith("Hello") gives True or False
# To Check Multiple Words: Pass a tuple of strings as the first argument -> text.startswith(("Hello", "Hi", "Bye"))
"""
or alternatively

start_words = ["what", "where", "when", "how"]

return text.strip().lower().split()[0] in start_words
"""