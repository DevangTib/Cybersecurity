import subprocess
import string

def try_password(password):
    """Function to try a password and return the result."""
    process = subprocess.Popen(['./notwordle'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input=password)
    return stdout.strip()

alphanumeric_characters = string.ascii_letters + string.digits + '_'

def search_char(index, current_password):
    for char in alphanumeric_characters:
        password = current_password + char
        result = try_password(password)
        try:
            x = result.split()[-5]
            if x == 'it\'s':
                print(result)
                return password
            x = int(x)
        except ValueError:
            print(f"Error: Unable to convert '{result.split()[0]}' to an integer")
            print(password)
            print(result)
            continue
        if x == index + 1:
            return password
    return current_password

current_password = ""
for i in range(30):
    current_password = search_char(i, current_password)
    print(f"Password after {i+1} characters: {current_password}")

print(f"Final password: {current_password}")
