question = ['for','this','I','am','awake']
print(question)
answer1 = question.copy()

answer = question
answer[0] = answer[3]
answer[1] = answer[4]
answer[2] = 'I'
answer[3] = 'am'

print(answer1)
print(answer)
print(question)