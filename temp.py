hwAvg      = 97.7
collabAvg  = 99.3
quizAvg    = 83.4
midtermAvg = 81.3

final = midtermAvg         # the default if you do not opt-in to take the final
tp = 89                  # your tp3 grade.  You can try different values...
passedParticipation = True # Set this to False if needed

divisor = 0.9 if passedParticipation else 1.0
grade = (0.10*quizAvg +
         0.15*hwAvg +
         0.20*collabAvg +
         0.15*midtermAvg +
         0.20*tp +
         0.10*final) / divisor

print(f'Standard (non-AMG) grade: {round(grade, 1)}')
