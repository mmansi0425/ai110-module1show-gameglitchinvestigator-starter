# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game was simply formated and had a section where I could input a guess. Once Is submitted the guess,there was a yellow box that appearted under the guess button that indicated that I should guess higher (I had guessed 3). There was also a side bar that allowed me to choose the difficulty of the game, along with showing me how many guessed I had left. 
- List at least two concrete bugs you noticed at the start  
  1. In Normal mode, you can guess numbers below -1 and above 100.
  2. No matter what number you input (even if its above 100), the hint will always tell you to "go higher"

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|200.   | Go lower hint/error|     Go higher hint         None
| -1    | go higher hint/error.|   go lower hint.         None 
| 33    | "Won"                |   attribute error     

Error for 3rd: 
AttributeError: st.session_state has no attribute "statupis". Did you forget to initialize it? More info: https://docs.streamlit.io/develop/concepts/architecture/session-state#initialization

File "/Users/mansimohanraj/AI COURSE/ai110-module1show-gameglitchinvestigator-starter/app.py", line 141, in <module>
    if st.session_state.statupis == "won":
       ^^^^^^^^^^^^^^^^^^^^^^^^^
File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages/streamlit/runtime/state/session_state_proxy.py", line 132, in __getattr__
    raise AttributeError(_missing_attr_error_message(key))

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

For this project I used ChatGPT and Claude. 

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

I asked Claude to give me suggestions on how to fix the issues with results (the opposite results). I entered the prompt: "If i enter a guess above 100 its showing go lower. if I enter a guess below 1 its showing go higher. how do I fix this". Claude responded " The messages are backwards. When your guess is too high, you need to go LOWER (not higher), and vice versa. The labels and the hint messages are mismatched. Here's the fix:". Claude then fixed the error. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I have not found anything that was incorrect or misleading with the feedback Chatgpt or Claude gave me. However, there were sometimes the AI agent I used was unclear with its answers. In cases like this, I asked the agent to better clarify it's response. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I considered a bug "fixed" after I tested it in the Streamlit app, and confirmed it behaved correctly. I also used the automated pytests to make sure the changes did not break any function. 

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I added a pytest for the "Too High" bug by checking that check_guess(60, 50) returned ("Too High", "📉 Go LOWER!"). The test passed meaning the game returned the correct answer. 
- Did AI help you design or understand any tests? How?
Yes. Ai suggested several different tests and the difficulty ranges for east test. It was easy to understand what each test was for with the AI agent. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
When a user interacts with a Streamlit app, the scirpt runs from the top every time. Session state is used to save important values (like the secret number), so they are not reset on every run. Without the session state, the game would lose its progress. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? This could be a testing habit, a prompting strategy, or a way you used Git.
I want to keep using AI agents to help write automated tests rather than testing the program manually. The tests (with AI help) made it much easier to find bugs and make fixes. The help of AI also covered any gaps of knowledge/information that I might not have thoguht of. 

- What is one thing you would do differently next time you work with AI on a coding task?
In the future, I would ask AI to focus on a single bug at a time rather than asking it multiple questions/prompts at once. By focusing on one section at a time, it could help me better understand the bugs and how to fix them. This way, I could not only learn more about code, but learn more about what causes bugs/errors. 


- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project showed me that AI-generated code can be helpful starting point, but it still needs to reviewed, tested, and sometimes corrected. I learned that developers should check AI's suggestions instead of assuming they are always correct. 
