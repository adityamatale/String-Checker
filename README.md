# DFA String Checker

## 📚 Overview

The **DFA String Checker** is a Python-based tool that leverages a **Deterministic Finite Automaton (DFA)** to validate strings based on user-defined conditions. Users can choose from multiple conditions, such as checking if a string starts and ends with certain characters, if it contains specific substrings, or if certain characters occur a specified number of times.

This program is highly customizable, allowing users to define their own DFA transitions or reuse an existing DFA configuration.



##    Features

- **Condition Types**:
    1. Check if a string starts and ends with specific characters.
    2. Count the occurrences of a particular character in the string.
    3. Ensure a string includes a given substring.
    4. Verify even and odd occurrences of characters.
    5. Check for at-least and at-most occurrence constraints.
    6. Confirm the absence of a particular substring.
    7. Ensure the string contains a substring that starts and ends with specified characters.
 
- **Customizable DFA Transitions**: 
    - Users can either define a new DFA or reuse a previous DFA configuration.
      
- **Final State Validation**: Check if the string reaches a final state after processing all characters.



## 📝 Usage

1. **Run the Script**: Execute the Python script in your terminal or IDE.
2. **Select the Condition**: Choose the condition you want to validate the string against (e.g., occurrence of a character, substring presence).
3. **Define the Alphabet**: Input the alphabet set for the DFA.
4. **Input DFA Transitions**: You can either input a new DFA or use a previously defined DFA.
5. **Enter the String**: Provide the string you wish to validate.
6. **Final Result**: The script will display the validation result based on the DFA state transitions.



## 💡 Example

### Scenario
Let's say we want to check if a string starts with "a" and ends with "b".

### Steps to Run:
1. **Condition Selection**: Choose option `1` (Starts with a string & Ends with a character).
2. **Input Alphabet**: Define the alphabet as `['a', 'b']`.
3. **Define DFA States**:
   - Enter the number of states: `2`.
   - Define `q0` (initial state) and `q1` (final state).
4. **DFA Transitions**:
   - Transition from `q0` to `q1` on input `a`.
   - Stay in `q1` on input `b`.
5. **Final State**: Set `q1` as the final state.
6. **Input String**: Enter the string `"aabb"`.

### Sample Output:
State Traversal: -> q0 -> q1 -> q1 -> q1 Yes!...The string is Valid.

