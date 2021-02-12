

def read_data():
    """A function to read the Card and Door public keys from the input.txt file
    :return card_public_key: string
    :return door_public_key: string"""
    fh = open("input.txt")
    return fh.read().split("\n")


def get_loop_size(public_key, subject):
    """A Function to determine the loop size for a given public key

    ------------
    public_key:
    The given public key to be used to calculate the loop size

    subject:
    The starting subject for this problem

    ------------

    :parameter public_key: integer
    :parameter subject: integer
    :return i: integer"""
    my_key = 1
    i = 0
    while my_key != public_key:
        i += 1
        my_key *= subject
        my_key = my_key % 20201227
    return i


def get_encryption(subject, loop):
    """A function to calculate the encryption key given the public key and the loop size

    ------------
    subject:
    The subject of the calculation, the public key to be converted

    loop:
    The loop size for the given encryption

    ------------

        :parameter subject: integer
        :parameter loop: integer
        :return my_key: integer"""
    my_key = 1
    for i in range(loop):
        my_key *= subject
        my_key = my_key % 20201227
    return my_key


card_public, door_public = read_data()
card_public = int(card_public)
door_public = int(door_public)
card_loop = get_loop_size(card_public, 7)
door_loop = get_loop_size(door_public, 7)

print("Card loop size is", card_loop)
print("Door loop size is", door_loop)

if card_loop > door_loop:
    encryption = get_encryption(card_public, door_loop)
else:
    encryption = get_encryption(door_public, card_loop)

print("The encryption is", encryption)

