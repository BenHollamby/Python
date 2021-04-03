#to show that the class works, here is a program
from survey import AnonymousSurvey

question = "What language did you first learn to speak? "
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Press enter to quit.\n")
while True:
    response = input("Language: ")
    if response == '':
        break
    my_survey.store_response(response)

print("\nThank you for participating!")
my_survey.show_results()
