import json


def get_users():
    with open("users.json", "r") as file:
        users = json.load(file)
    return users


def filter_users_by_name(name):
    users = get_users()

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    users = get_users()

    filtered_users = [user for user in users if user.get("age") == age]

    for user in filtered_users:
        print(user)


def filter_users_by_email(email):
    users = get_users()

    filtered_users = [
        user for user in users if user.get("email", "").lower() == email.lower()
    ]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = (
        input("What would you like to filter by? (name, email, age): ").strip().lower()
    )

    if filter_option == "name":
        search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(search)
    elif filter_option == "email":
        search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(search)
    elif filter_option == "age":
        search = int(input("Enter an age to filter users: ").strip())
        filter_users_by_age(search)
    else:
        print("Filtering by that option is not yet supported.")
