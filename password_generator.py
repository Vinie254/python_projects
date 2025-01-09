import secrets
import string
random_characters = []
for i in range(12):
    random_character = secrets.choice(string.ascii_letters + string.digits + string.punctuation)
    random_characters.append(random_character)
    character_list = list(random_character)
    secrets.SystemRandom().shuffle(character_list)

result_string = "".join(random_characters)
print(f"Your new password is: {result_string}")