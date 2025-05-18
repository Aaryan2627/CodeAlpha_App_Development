import random
import webbrowser

quotes = [
    "The best way to get started is to quit talking and begin doing. – Walt Disney",
    "Don't let yesterday take up too much of today. – Will Rogers",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Act as if what you do makes a difference. It does. – William James"
]

def get_random_quote():
    return random.choice(quotes)

def share_on_twitter(quote):
    tweet_url = f"https://twitter.com/intent/tweet?text={quote.replace(' ', '%20')}"
    print("Opening Twitter share page...")
    webbrowser.open(tweet_url)

def run():
    while True:
        quote = get_random_quote()
        print(f"\n💬 Quote:\n{quote}\n")
        print("1. Get another quote")
        print("2. Share on Twitter")
        print("3. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            continue
        elif choice == '2':
            share_on_twitter(quote)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    run()



