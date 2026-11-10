password=input(f"Введите пароль:")
if len(password)<=16:
    print(f"Слишком короткий пароль")
elif password.isalnum():
    print(f"Слабый пароль")
else:
    print(f"Надежный пароль")