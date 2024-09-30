import subprocess

# Read the wordlist
with open('wordlist.txt', 'r') as file:
    passwords = [line.strip() for line in file]

def try_password(password):
    """Function to try a password and return the result."""
    process = subprocess.Popen(['./bruteforcer'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input=password)
    return stdout.strip()

def binary_search_password(passwords):
    """Binary search algorithm to find the correct password."""
    low = 0
    high = len(passwords) - 1

    while low <= high:
        mid = (low + high) // 2
        password = passwords[mid]
        result = try_password(password)
        print(f'Trying password: {password}, Result: {result}')

        if "WRONG :( Key too low" in result:
            low = mid + 1
        elif "WRONG :( Key too high" in result:
            high = mid - 1
        else:
            print(f'Correct password found: {password}')
            return password

    print('Password not found in the list.')
    return None

# Start the binary search for the correct password
correct_password = binary_search_password(passwords)
