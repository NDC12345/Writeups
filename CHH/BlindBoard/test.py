def is_secure_password(password):
    if len(password) < 8:
        return False

    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special = False

    for char in password:
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_digit = True
        elif char in {'@', '#', '$', '&'}:
            has_special = True

    if has_lowercase and has_uppercase and has_digit and has_special:
        if not (password[0].isupper() and password[-1].isupper()):
            return True
        if not (password[0].isdigit() and password[-1].isdigit()):
            return True
    return False

# Đọc số lượng test
T = int(input())

# Kiểm tra từng test
for _ in range(T):
    password = input()
    if is_secure_password(password):
        print("YES")
    else:
        print("NO")
