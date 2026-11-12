# 2
=================================== FAILURES ===================================
______________________ test_count_words_counts_each_word _______________________

    def test_count_words_counts_each_word():
>       assert count_words("we open at 9am") == 4
E       AssertionError: assert 14 == 4
E        +  where 14 = count_words('we open at 9am')

test_text_tools.py:11: AssertionError
=========================== short test summary info ============================
FAILED test_text_tools.py::test_count_words_counts_each_word - AssertionError: assert 14 == 4
 +  where 14 = count_words('we open at 9am')
========================= 1 failed, 19 passed in 0.22s =========================
Error: Process completed with exit code 1.

### the test_count_words_counts_each_word() execute the error, because the function gave 14 but what expected is 4, because the function count words change to count characters instead of words

# 3
