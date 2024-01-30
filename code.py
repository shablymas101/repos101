import time
import winsound  # Only works on Windows, for other platforms, consider using other sound libraries

def play_bell():
    """
    Play a bell sound to signal the end of a meditation session.
    """
    duration = 1000  # milliseconds
    frequency = 440  # Hz
    winsound.Beep(frequency, duration)

def meditation_timer(duration_minutes):
    """
    Set a timer for meditation with a specified duration in minutes.
    """
    print(f"Starting {duration_minutes}-minute meditation session.")
    time.sleep(duration_minutes * 60)
    play_bell()
    print("Meditation session complete. Take a moment to breathe.")

def main():
    print("Welcome to the Simple Meditation App!")

    while True:
        print("\nMenu:")
        print("1. Start Meditation Session")
        print("2. Exit")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            duration_input = input("Enter the duration of your meditation session in minutes: ")
            try:
                duration_minutes = int(duration_input)
                meditation_timer(duration_minutes)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == "2":
            print("Exiting the Meditation App. Thank you for meditating with us!")
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
