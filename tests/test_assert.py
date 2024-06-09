import pytest


def test_validdata_title():
    expect_result : str = "google"
    actual_result : str = "gmail"

    if actual_result == expect_result:
        print("test pass")
        # assert True, "Test case pass"
        assert expect_result in actual_result
    else:
        print("test fail")
        assert False, "Test case fail"