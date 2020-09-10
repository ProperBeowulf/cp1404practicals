email_to_name = {}


def main():
    user_email = input("please enter your email: ")
    while user_email != "":
        if user_email in email_to_name:
            print("email already added")
        else:
            user_name = get_name(user_email)
            check_name = input("is your name {} (Y/n)".format(user_name)).upper()
            if check_name == "Y" or "":
                email_to_name[user_email] = user_name
            else:
                new_name = input("Enter name: ").title()
                email_to_name[user_email] = new_name
        user_email = input("please enter your email: ")
    email_list = list(email_to_name.keys())
    email_list.sort()
    for email in email_list:
        print("{} ({})".format(email_to_name[email], email))


def get_name(email):
    parts = email.split("@")[0].split(".")
    name = " ".join(parts).title()
    return name


main()
