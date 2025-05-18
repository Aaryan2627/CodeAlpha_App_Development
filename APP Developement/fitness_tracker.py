import datetime

class FitnessTracker:
    def __init__(self):
        self.workouts = []
        self.goal = None

    def set_goal(self):
        self.goal = input("Set your fitness goal (e.g., 'Run 5km in under 30 minutes'): ")
        print("Goal set successfully.\n")

    def add_workout(self):
        print("\nWorkout Types: Running, Cycling, Lifting, Yoga, Other")
        w_type = input("Enter workout type: ").capitalize()
        duration = input("Duration (in minutes): ")
        notes = input("Additional notes: ")
        date = datetime.date.today()

        self.workouts.append({
            "type": w_type,
            "duration": duration,
            "notes": notes,
            "date": str(date)
        })
        print("Workout added successfully.\n")

    def view_progress(self):
        if not self.workouts:
            print("No workouts recorded yet.\n")
            return

        print("\nWorkout History:")
        for i, w in enumerate(self.workouts, 1):
            print(f"{i}. [{w['date']}] {w['type']} - {w['duration']} mins - {w['notes']}")

        print(f"\nCurrent Goal: {self.goal if self.goal else 'No goal set.'}\n")

    def run(self):
        while True:
            print("🏋️‍♀️ Fitness Tracker")
            print("1. Set Fitness Goal")
            print("2. Add Workout")
            print("3. View Progress")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.set_goal()
            elif choice == '2':
                self.add_workout()
            elif choice == '3':
                self.view_progress()
            elif choice == '4':
                print("Goodbye and stay fit!")
                break
            else:
                print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    app = FitnessTracker()
    app.run()
