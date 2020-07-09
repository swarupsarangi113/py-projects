# Basic Python Programs
---
The problems are selected from the book [Automate the Boring Stuff With Python](https://automatetheboringstuff.com/ "Automate the Boring Stuff")

## Contents

* bulletPointAdder
---
The bulletPointAdder script will get the text from the clipboard, add
a star and space to the beginning of each line, and then paste this new
text to the clipboard. For example, if I copied the following text (for
the Wikipedia article “List of Lists of Lists”) to the clipboard:

>Input

Lists of animals

>Output

\* Lists of animals

* coin flip streaks
---
Write a program to find out how often a streak of six heads r a
streak of six tails comes up in a randomly generated list of heads and
tails. Your program breaks up the experiment into two parts: the first
part generates a list of randomly selected 'heads' and 'tails' values,
and the second part checks if there is a streak in it. Put all of this
code in a loop that repeats the experiment 10,000 times so we can find
out what percentage of the coin flips contains a streak of six heads or
tails in a row. As a hint, the function call random.randint(0, 1) will
return a 0 value 50% of the time and a 1 value the other 50% of the
time.

* collatz sequence
---
Write a function named collatz() that has one parameter named number.
If number is even, then collatz() should print number // 2 and return this value.
If number is odd, then collatz() should print and return 3 * number + 1.
Then write a program that lets the user type in an integer
and that keeps calling collatz() on that number until the function returns the value 1.
(Amazingly enough, this sequence actually works for any integer—sooner or later, using this sequence,
you’ll arrive at 1! Even mathematicians aren’t sure why.
Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”) 

* comma code
---
Say you have a list value like this: spam = ['apples', 'bananas', 'tofu',
'cats']

Write a function that takes a list value as an argument and
returns a string with all the items separated by a comma and a space,
with and inserted before the last item.

For example, passing the previous spam list to the function would return 'apples, bananas, tofu,
and cats'. But your function should be able to work with any list value
passed to it. Be sure to test the case where an empty list [] is passed
to your function

* guess the number
---
  Guess a number game.

* rock paper scissors
---
  The traditional rock paper scissors now play with computer.

* mapIt
---
Problem Statement - 1. Gets a street address from the command line arguments or clipboard
                    2. Opens the web browser to the Google Maps page for the address

* mclip
---
You want to be able to run this program with a command line argument
that is a short key phrase—for instance, agree or busy. The message
associated with that key phrase will be copied to the clipboard so that
the user can paste it into an email. This way, the user can have long,
detailed messages without having to retype them.
YOU CAN USE THIS TYPE OF SCRIPTS TO SAVE PASSWORDS FOR DIFFERENT SITES

* searcgpypi
---
This is what your program does:
1. Gets search keywords from the command line arguments
1. Retrieves the search results page
1. Opens a browser tab for each result

* zigzag
---
Prints the below paper
![Output-Image](https://github.com/swarupsarangi113/py-projects/blob/master/Projects%20from%20Auotmate%20the%20Boring%20Stuff/zigzag-output.png)
