BEGIN

INPUT user_score

IF 90 <= user_score <= 100 THEN
print: 'GradeA'
JUMP OUT OF THE LOOP

IF 80 <= user_score <= 89 THEN
print: 'GradeB'
JUMP OUT OF THE LOOP

IF 70 <= user_score <= 79 THEN
print: 'GradeC'
JUMP OUT OF THE LOOP

IF 60 <= user_score <= 69 THEN
print: 'GradeD'
JUMP OUT OF THE LOOP

IF user_score < 60 THEN
print: 'GradeE'
JUMP OUT OF THE LOOP

IF user_score > 100 or user_score < 0 THEN
print: 'ERROR'
USER WILL BE ASKED TO ENTER THEIR SCORE AGAIN UNTIL IT'S IN THE RIGHT RANGE

END