from instadm import InstaDM


with open(r'users.txt', 'r') as f:
    users = [line.strip() for line in f]

print(users)

# Auto login
insta = InstaDM(username='your username :)', password='password', headless=False)

for user in users:
    # Send message
    insta.sendMessage(user=user, message='text whatever u want to send')
