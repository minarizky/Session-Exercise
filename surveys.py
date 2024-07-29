class Question:
    def __init__(self, question, choices):
        self.question = question
        self.choices = choices
        self.allow_comment = allow_comment

class Survey:
    def __init__(self, title, instructions, questions):
        self.title = title
        self.instructions = instructions
        self.questions = questions

satisfaction_survey = Survey(
    "Satisfaction Survey",
    "Please fill out the following survey to help us improve our services.",
    [
        Question("Are you satisfied with our service?", ["Yes", "No"]),
        Question("Would you recommend us to a friend?", ["Yes", "No"]),
        Question("How much did you spend on our service?", ["Less than $10,000", "More than $10,000"]),
        Question("Would you use our service again?", ["Yes", "No"])
    ]
)
