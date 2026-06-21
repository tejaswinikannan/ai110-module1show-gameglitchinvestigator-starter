# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Game purpose:** A number guessing game where the player picks a difficulty (Easy / Normal / Hard), then tries to guess a secret number within a limited number of attempts based on the difficulty. Each guess returns a hint and updates a score, and the game ends when the player guesses correctly or runs out of attempts.

**Bugs found:**

1. **Hints were reversed** — when the guess was too high the game said "Go HIGHER!", and when too low it said "Go LOWER!". The comparison branches in `check_guess` had their return values swapped.
2. **Cast to string on even attempts** — on every other submission the secret was converted to a string before being passed to `check_guess`, causing alphabetical comparison instead of numeric, producing wrong hints.
3. **New game did not fully reset session state** — clicking "New Game" only reset `attempts` and `secret`, leaving `score`, `status`, and `history` carrying over from the previous round. The new secret also always used a hardcoded range of 1–100 instead of the selected difficulty range.
4. **Difficulty ranges for Normal and Hard were swapped** — Normal returned 1–100 and Hard returned 1–50, making Hard easier than Normal.
5. **"Attempts left" counter was off by one** — the display was rendered before `attempts` was incremented in the submit block, so on the final guess the screen simultaneously showed "Attempts left: 1" and "Out of attempts!".

**Fixes applied:**

- Swapped the return values in `check_guess` to correctly return  "Go LOWER!" or "Go HIGHER!".
- Removed the alternating string-cast of the secret so `check_guess` always receives two integers.
- Extended the new-game reset block to also clear `score`, `status`, and `history`, and made it use the difficulty-aware range.
- Corrected `get_range_for_difficulty` so Normal → `(1, 50)` and Hard → `(1, 100)`.
- Changed `attempts` to start at `0`, moved the increment before the `st.info()` display line so the counter always reflects the current attempt when rendered.
- Moved utility functions from `app.py` into `logic_utils.py` and imported them, keeping UI and logic separate.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User opens the app and sees "Attempts left: 8" on Normal difficulty
2. User enters a guess of 20 → game returns "Go HIGHER!"
3. User enters a guess of 70 → game returns "Go LOWER!"
4. Score updates correctly after each guess and attempts left decrements by 1
5. User enters the correct guess → game shows " Correct!" and ends with a final score

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
