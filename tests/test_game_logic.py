from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    check_guess,
    update_score,
)


# --- get_range_for_difficulty ---

def test_range_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_range_normal():
    assert get_range_for_difficulty("Normal") == (1, 50)

def test_range_hard():
    assert get_range_for_difficulty("Hard") == (1, 100)

def test_range_unknown_defaults_to_hard():
    assert get_range_for_difficulty("???") == (1, 100)


# --- parse_guess ---

def test_parse_empty_is_error():
    assert parse_guess("") == (False, None, "Enter a guess.")

def test_parse_none_is_error():
    assert parse_guess(None) == (False, None, "Enter a guess.")

def test_parse_valid_int():
    assert parse_guess("42") == (True, 42, None)

def test_parse_float_truncates():
    assert parse_guess("42.9") == (True, 42, None)

def test_parse_non_number_is_error():
    assert parse_guess("abc") == (False, None, "That is not a number.")


# --- check_guess ---

def test_winning_guess():
    assert check_guess(50, 50) == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # Bug fix: guess above secret must be "Too High" and hint to go LOWER
    assert check_guess(60, 50) == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    assert check_guess(40, 50) == ("Too Low", "📈 Go HIGHER!")


# --- update_score ---

def test_update_score_win_adds_points():
    # attempt 0 win: 100 - 10*1 = 90 points
    assert update_score(0, "Win", 0) == 90

def test_update_score_win_floor_is_ten():
    # large attempt number floors points at 10
    assert update_score(0, "Win", 20) == 10

def test_update_score_too_low_subtracts():
    assert update_score(100, "Too Low", 1) == 95
