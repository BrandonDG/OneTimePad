#!/usr/bin/python3.5

import os

# XOR the message with the key and return the results as a byte object
def xor_message(message, key):
    return bytes(p ^ k for p, k in zip(*map(bytes, [message, key])))

# Main
def main():
    print("This is main")
    plaintext = ""
    while (True):
        where_is_cipher = input("Is the plaintext given via stdin or file? ")
        if where_is_cipher == "file":
            print("File selected")
            plain = input("File name please: ")
            plaintext += open(plain, 'rU').read()
            break
        elif where_is_cipher == "stdin":
            print("stdin selected")
            plain = input("Ciphertext please: ")
            plaintext = plain
            break
        else:
            print("Need to select a valid option ('file' or 'stdin')")

    plaintext = plaintext.strip('\n')

    # Generate a random key of bytes that is of equal length of the plaintext
    key = os.urandom(len(plaintext))
    # Print the key and plaintext
    print("------")
    print("Plaintext: \n%s" % plaintext)
    print(" ")
    print("Key: \n%s" % key)
    print("------")
    # Generate ciphertext by xor'ing both the message and key
    ciphertext = xor_message(plaintext.encode("utf-8"), key)
    print("Binary Ciphertext: \n%s" % ciphertext)
    print("------")
    print("Verify: \n%s" % xor_message(ciphertext, key))

    # Write ciphertext to file
    outputfile = open("ciphertext", "wb")
    outputfile.write(ciphertext)
    outputfile.close()

    # Display file ciphertext
    print("------")
    print("Character Ciphertext: \n\n")
    print(os.system("cat ciphertext"))

# Main
if __name__ == "__main__":
    main()
