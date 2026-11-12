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

# 3a
## Before checking, I predicted it would fail on GitHub
## and pass on my laptop, because the line of httpx2 has been deleted from requirements.txt, and TestClient need it 
## Result: my prediction was right.

# 3b
Run python -m pytest -v
============================= test session starts ==============================
platform linux -- Python 3.13.18, pytest-9.2.0, pluggy-1.7.0 -- /opt/hostedtoolcache/Python/3.13.18/x64/bin/python
cachedir: .pytest_cache
rootdir: /home/runner/work/ci-practice/ci-practice
plugins: anyio-4.16.0
collecting ... collected 13 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test_main.py _________________________
test_main.py:2: in <module>
    from fastapi.testclient import TestClient    # a "pretend browser" that sends requests to your app
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/fastapi/testclient.py:1: in <module>
    from starlette.testclient import TestClient as TestClient  # noqa
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/starlette/testclient.py:34: in <module>
    raise RuntimeError(
E   RuntimeError: The starlette.testclient module requires the httpx2 package to be installed.
E   You can install this with:
E       $ pip install httpx2
=========================== short test summary info ============================
ERROR test_main.py - RuntimeError: The starlette.testclient module requires the httpx2 package to be installed.
You can install this with:
    $ pip install httpx2
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.38s ===============================
Error: Process completed with exit code 2.

## My local computer already has httpx2 installed, but the fresh computer on github does not, when I delete the line of httpx2 in requirements.txt, the computer miss it when pip install, so fail as TestClient need httpx2
## In a team, CI also helps because:
## - nobody can manually to run the tests, because GitHub runs them automatically on every push
## - if my change breaks someone's code, everyone sees the error before it is pulished into the main project


# 6
## CI is useful to run on every push instead of each person just running the tests on their laptop because we can test the program really works on a fresh laptop, not a old used laptop will full of packages