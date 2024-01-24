import bcrypt

# Function to hash a password
def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

# Function to verify a password
def verify_password(password, hashed_password):
    password_encoded = password.encode('utf-8')
    hashed_password_encoded = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_encoded, hashed_password_encoded)