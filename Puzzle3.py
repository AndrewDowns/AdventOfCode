def populatePasswords():
    passwords = []
    fh = open("Passwords.txt")
    for line in fh:
        pass_dict = dict()
        line = line.strip()
        password_parts = line.split(":")
        policy_parts = password_parts[0].split()
        min_max_parts = policy_parts[0].split("-")
        pass_dict["password"] = password_parts[1]
        pass_dict["letter"] = policy_parts[1]
        pass_dict["min"] = int(min_max_parts[0])
        pass_dict["max"] = int(min_max_parts[1])
        passwords.append(pass_dict)

    return passwords


def valid(password):
    #checks to see if a password is valid

    occurences = password["password"].count(password["letter"])

    if occurences >= password["min"] and occurences <= password["max"]:
        return True
    else:
        return False



valid_count = 0
passwords = populatePasswords()

for password in passwords:
    if valid(password):
        valid_count += 1

print(len(passwords))
print("Valid Passwords = ", valid_count)