def populatePasswords():
    '''Function to loads in the passwords from the passwords file
    It will then return a structured list of dictionaries for each password'''

    passwords = []
    fh = open("Passwords.txt")
    for line in fh:
        pass_dict = dict()
        line = line.strip()
        password_parts = line.split(":")
        policy_parts = password_parts[0].split()
        position_parts = policy_parts[0].split("-")
        pass_dict["password"] = password_parts[1].strip()
        pass_dict["letter"] = policy_parts[1]
        pass_dict["first_pos"] = int(position_parts[0])
        pass_dict["second_pos"] = int(position_parts[1])
        passwords.append(pass_dict)

    return passwords


def valid(password):
    ''' A function to check to see if a password is valid
    validity is based on the rule that the letter must be contained in either gicen position but not both'''

    instances = []

    for l in password["password"]:
        if l == password["letter"]:
            instances.append(True)
        else:
            instances.append(False)


    if instances[password["first_pos"]-1] and not instances[password["second_pos"]-1]:
        return True
    elif instances[password["second_pos"]-1] and not instances[password["first_pos"]-1]:
        return True
    else:
        return False


valid_count = 0
passwords = populatePasswords()

for password in passwords:
    if valid(password):
        valid_count += 1

print("Valid Passwords = ", valid_count)