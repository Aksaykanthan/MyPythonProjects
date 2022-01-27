class Question:
    def __init__(self, prompt , answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "what color  are apples ? \n (a)red \n (b) purple \n (c) Orange \n\n",
    "what color  are grapes ? \n (a)red \n (b) purple \n (c) Orange \n\n",
    "what color  are orange ? \n (a)red \n (b) purple \n (c) Orange \n\n",

]

question = [
    Question(question_prompts[0] , "a"),
    Question(question_prompts[1] , "b"),
    Question(question_prompts[2] , "c"),

]
def run_test(question):
    score = 0
    for question in question:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("you got " + str(score) + "/" + str(3) )

run_test(question)
