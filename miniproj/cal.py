import datetime

def get_today_date():
    today = datetime.date.today()
    return today.strftime("%A, %d %B %Y")

def get_day_of_week(year, month, day):
    try:
        specific_date = datetime.date(year, month, day)
        return specific_date.strftime("%A")
    except ValueError:
        return "Invalid date. Please be sure the year, month, and day are correct."

def calendar():
    print("Welcome to the Calendar!")
    while True:
        print("\nOptions:")
        print("1. Show today's date")
        print("2. Find the day of the week")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            print("\nToday's Date:")
            print(get_today_date())

        elif choice == "2":
            try:
                year = int(input("\nEnter the year (e.g., 2025): "))
                month = int(input("Enter the month (1-12): "))
                day = int(input("Enter the day (1-31): "))
                day_name = get_day_of_week(year, month, day)
                print(f"The day of the week for {year}-{month}-{day} is: {day_name}")
            except ValueError:
                print("Please enter valid number for year, month, and day.")
        
        elif choice == "3":
            break
        
        else:
            print("Invalid choice. Try again")

calendar()

#drawback of
#function and class
#built-in in class based views in Django
#CRUD with file in Function and class in MVT

# djangos -form