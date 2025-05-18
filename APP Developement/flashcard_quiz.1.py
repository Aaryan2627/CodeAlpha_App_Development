class FlashcardQuizApp:
    def __init__(self):
        self.flashcards = []

    def add_flashcard(self, question, answer):
        self.flashcards.append({'question': question, 'answer': answer})

    def quiz(self):
        if not self.flashcards:
            print("No flashcards available. Add some first.")
            return

        score = 0
        for i, card in enumerate(self.flashcards):
            print(f"\nQ{i+1}: {card['question']}")
            user_answer = input("Your answer: ").strip().lower()
            if user_answer == card['answer'].strip().lower():
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer is: {card['answer']}")

        print(f"\nQuiz complete! Your score: {score}/{len(self.flashcards)}\n")

    def run(self):
        while True:
            print("Flashcard Quiz App")
            print("1. Add Flashcard")
            print("2. Take Quiz")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                question = input("Enter the question: ")
                answer = input("Enter the answer: ")
                self.add_flashcard(question, answer)
                print("Flashcard added.\n")
            elif choice == '2':
                self.quiz()
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    app = FlashcardQuizApp()
    app.run()


