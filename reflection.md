# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  The hint provided was mostly opposite for any number guessed.
  Once the game was over, couldnt start a new game, perhaps the session variables were not reset.
  No error message on entering a digit outside the expected number range(eg: 104).
  The number attempts left counter was not maintaining accurate count.


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input             | Expected Behavior | Actual Behavior       | Console Output / Error    |
|-------------------|-------------------|-----------------------|---------------------------|
|Secret 21 Guess 22 | Go Higher Hint    | Go Lower Hint         | Hint displaying opposite  |
|Click New game     | Reset the page    | Clear values manually | The text box must be reset|
|Input 103          | Throw an error    | Go Higher             | No error/warning displayed|

---

## 2. How did you use AI as a teammate?

- I have used claude as my AI teamate
- One important suggestion from AI was that the signatures and docstrings were present in logic.utils but all the implementation is actually present in app.py
- AI rightly identified that the number range given for normal and hard were interchanged and the function update_score looks buggy.
- There is a bug in the code where the entered guess was converted to string on even attempts and hence would show wrong hint.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
