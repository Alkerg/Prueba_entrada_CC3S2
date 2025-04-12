class Question:
    def __init__(self, description, options, correct_answer):
        self.description = description
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        return self.correct_answer == answer
    
class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0
        self.correct_answers = 0
        self.incorrect_answers = 0

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None
    
    def answer_question(self, question, answer):
        if question.is_correct(answer):
            self.correct_answers += 1
            return True
        else:
            self.incorrect_answers += 1
            return False
    
def run_quiz():
    print("Bienvenido al juego de Trivia!")
    print("Responde las siguientes preguntas seleccionando el número de la opción correcta.")
    quiz = Quiz()
    quiz.add_question(Question('Cuál es la capital de Francia?', ['Londres', 'Berlín', 'París', 'Madrid'], 'París'))
    quiz.add_question(Question('Cuanto es 2 + 2?', ['3', '4', '5', '6'], '4'))
    quiz.add_question(Question('Cuantos huesos tiene el cuerpo humano?', ['206', '205', '204', '203'], '206'))
    
    while quiz.current_question_index < 10:
        question = quiz.get_next_question()
        if question:
            print(f"Pregunta {quiz.current_question_index}: {question.description}")
            for idx, option in enumerate(question.options):
                print(f"{idx + 1}) {option}")
            answer = input("Tu respuesta: ")
        else:
            break
    print("Juego terminado.")
    print(f"Respuestas correctas: {quiz.correct_answers} / {quiz.correct_answers + quiz.incorrect_answers}")