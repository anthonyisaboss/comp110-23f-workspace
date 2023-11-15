"""Testing and importing from dict."""
__author__ = "730669473"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_test1() -> None:
    """Going to return a dict."""
    assert invert({}) == {}


def test_invert_dict() -> None:
    """Testing a normal dict."""
    assert invert({"hi": "bye", "go": "run"}) == {"bye": "hi", "run": "go"}


def test_invert_dict2() -> None:
    """Testing another dict."""
    assert invert({"you": "me"}) == {"me": "you"}


def test_color_test() -> None:
    """Testing an empty color dict.""" 
    assert favorite_color({}) == {}


def test_color_test2() -> None:
    """Testing with one color."""
    assert favorite_color({"Allie": "blue"}) == {"blue"}


def test_color_test3() -> None:
    """Testing with two colors."""
    assert favorite_color({"Allie": "blue", "Rohan": "red"}) == {"blue"}


def test_count1() -> None:
    """Going to count values."""
    assert count(["Hi", "Hi", "Bye"]) == {"Hi": 2, "Bye": 1}


def test_count2() -> None:
    """Going to count more words."""
    assert count(["Goodbye", "Hello", "run"]) == {"Goodbye": 1, "Hello": 1, "run": 1}


def test_count3() -> None:
    """Going to count 2 words."""
    assert count(["rah", "bah"]) == {"rah": 1, "bah": 1}


def test_alphabet() -> None:
    """Going to run the function."""
    assert alphabetizer(["apple", "bapple", "bape"]) == {"a": ["apple"], "b": ["bapple", "bape"]}


def test_alphabet2() -> None:
    """Going to run the function again."""
    assert alphabetizer(["anthony", "bailey"]) == {"a": ["anthony"], "b": ["bailey"]}


def test_alphabet3() -> None:
    """Going to run the function again."""
    assert alphabetizer(["friction", "hi", "frog"]) == {"f": ["friction", "frog"], "h": ["hi"]}


def test_atttendance1() -> None:
    """Going to update the attendance."""
    assert update_attendance({}, "", "") == {}


def test_attendance2() -> None:
    """Updating attendance."""
    assert update_attendance({"monday": ["anthony", "cara"]}, "monday", "jacob") == {"monday": ["anthony", "cara", "jacob"]}


def test_attendance3() -> None:
    """Updating the attendance."""
    assert update_attendance({"monday": ["anthony", "cara"]}, "monday", "jason") == {"monday": ["anthony", "cara", "jason"]}