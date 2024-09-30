import base64
import sys
# Original string
original_string = sys.argv[1]

# Convert string to bytes
original_bytes = original_string.encode('utf-8')

# Base64 encoding
base64_encoded = base64.b64encode(original_bytes).decode('utf-8')

# Base32 encoding
base32_encoded = base64.b32encode(original_bytes).decode('utf-8')

# Hex encoding
hex_encoded = original_bytes.hex()

# Text itself (no encoding)
text_itself = original_string

# Print the results
print(base64_encoded)
print(base32_encoded)
print(hex_encoded)
print(text_itself)
