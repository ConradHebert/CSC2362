alphabet = "abcdefghijklmnopqrstuvwxyz"
special = " ,.-;:_?!'=/()"

def decrypt(message):
    """Brute forcing all possible shifts"""
    messages = []
    for key in range(1, 26):
        decrypted = ""
        for character in message:
            if character in special:
                decrypted += character
                continue
            if character in alphabet:
                decrypted += chr((ord(character) - 97 + key) % 26 + 97)
            messages.append(decrypted)

    """finding which of the brute forced outcomes has the highest frequency of e, which is the probable plaintext"""
    frequency = [(c, c.count('e')) for c in messages]
    frequency.sort(key=lambda x: x[1], reverse=True)
    return frequency[0][0]

message = input("Enter the encrypted message: ").lower()
decrypted_message = decrypt(message)
print(f'\nProbable plaintext based on letter frequency is: \n{decrypted_message}')


"""This code works based on the most frequent letter being e in the plaintext. If e is not the most frequent letter, it likely
 will not produce the decoded text. e is the most frequent as the sample size increases, so this only really works on 
 very large inputs."""