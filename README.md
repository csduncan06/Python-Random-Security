
# Python Random Investigation

A simple script that investigates how random the Python random module actually is.

<ins>Script Explanatory</ins>
1. Gets random character from digits, strings or punctuation 
2. Stores the character selected in a dictionary 
3. Repeats 1000 times 
4. If the character is already in the dictionary
5. increase value by 1, else add the character to the dictionary
6. Counts and stores how many times a character was randomly selected and prints it out

Python Random uses the [Mersenne Twister algorithm](https://en.wikipedia.org/wiki/Mersenne_Twister)
