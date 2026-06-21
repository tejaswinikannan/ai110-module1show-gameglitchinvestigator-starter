from logic_utils import check_guess, get_range_for_difficulty

# --- Existing tests (fixed: check_guess returns a tuple, not a plain string) ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug fix: hint messages were swapped ---
# Old: guess > secret said "Go HIGHER!", guess < secret said "Go LOWER!"
# Fixed: guess > secret says "Go LOWER!", guess < secret says "Go HIGHER!"

def test_too_high_message_says_go_lower():
    _, message = check_guess(60, 50)
    assert "LOWER" in message, f"Expected 'LOWER' in message but got: {message}"

def test_too_low_message_says_go_higher():
    _, message = check_guess(40, 50)
    assert "HIGHER" in message, f"Expected 'HIGHER' in message but got: {message}"


# --- Bug fix: secret was cast to str on even-numbered attempts ---
# This caused alphabetical comparison instead of numeric comparison.
# e.g. check_guess(9, "10"): "9" > "10" alphabetically = True → wrongly returned "Too High"
# e.g. check_guess(2, "10"): "2" > "10" alphabetically = True → wrongly returned "Too High"
# Fix: secret is always passed as int, so numeric comparison is used.

def test_numeric_comparison_9_vs_10():
    # 9 < 10 numerically → Too Low
    # "9" > "10" alphabetically → would have been Too High (bug)
    outcome, _ = check_guess(9, 10)
    assert outcome == "Too Low"

def test_numeric_comparison_2_vs_10():
    # 2 < 10 numerically → Too Low
    # "2" > "10" alphabetically → would have been Too High (bug)
    outcome, _ = check_guess(2, 10)
    assert outcome == "Too Low"

def test_numeric_comparison_11_vs_9():
    # 11 > 9 numerically → Too High
    # "11" < "9" alphabetically → would have been Too Low (bug)
    outcome, _ = check_guess(11, 9)
    assert outcome == "Too High"


# --- Bug fix: difficulty ranges were swapped for Normal and Hard ---
# Old: Normal → (1, 100), Hard → (1, 50)  — Hard had a smaller range, making it easier
# Fixed: Normal → (1, 50), Hard → (1, 100) — Hard has a larger range, making it harder

def test_easy_range():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_normal_range():
    assert get_range_for_difficulty("Normal") == (1, 50)

def test_hard_range():
    assert get_range_for_difficulty("Hard") == (1, 100)

def test_hard_range_wider_than_normal():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high
