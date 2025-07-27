import random
import string
import requests

def generate_username(length):
    letters = string.ascii_lowercase + string.digits + "._"
    return ''.join(random.choices(letters, k=length))

def is_available(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    return response.status_code == 404

# إعدادات
length = int(input("طول اليوزر (مثلاً 4): "))
amount = int(input("كم عدد اليوزرات اللي تبي تجربها؟: "))

print("\nاليوزرات المتاحة 👇:\n")

found = 0
tried = 0
while found < amount:
    user = generate_username(length)
    tried += 1
    if is_available(user):
        print(user)
        found += 1
