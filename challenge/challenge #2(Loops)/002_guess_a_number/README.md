START

IMPORT `random module`

create a variable called `attempt`

GENERATE a random number `target` between 1 and 10

INITIALIZE `guessed = False`

WHILE guessed is not True:

DISPLAY `"Guess the number: "`

READ `guess`

IF `guess` equals `target`:

`attempt` += 1

DISPLAY `"Correct! 🎉"`

SET `guessed = True`

ELSE:

DISPLAY `"Wrong, try again!"`

`attempt` += 1

END
