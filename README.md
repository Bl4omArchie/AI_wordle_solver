# AI_wordle_solver

A python wordle game with auto-solving

![Alt text](https://labs.openai.com/s/X2uchCEKfBc4QUeuiunkPcMh)

```
app.py: easy script where you call the game from command line and select your wordlist 
src
|-> wordlist.py: a python Object so you can manage a wordlist
|-> launcher.py: the script that launch the game for normal play and AI play
|-> game.py: the rules of wordle 
|-> solver.py: my algorithm that solve automaticly the game
```


## The algorithm

- How does it work ?

I'm first calculating the index of frequency of the given wordlist. It consist on making a pourcentage of occurence for each letter in the alphabet.
Then I'm taking the word that the cumulate the highest index of frequency by cumulating the IF of each letters. Note: I'm taking only words where the each letters are different from each other.
When I get the result, I'm removing from the wordlist all the wrong words. There is an example:

```
My guess: "shark"
response: "cimii"     #Reminder: c: correct, m: correct but wrong place, i: incorrect

I keep in my wordlist only:
- words starting with a 's'
- that doesn't contain any 'h', 'r' or 'k'.
- but must have an 'a' somewhere except at the third place
```

Then I repeat the operation until I found out the word.
