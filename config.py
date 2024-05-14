from src.model.admins import a

BOT_TOKEN = '5921193873:AAFtVwAzegmN6G9USoetSEVV7NoSW-BFJRM'
admins = a.get()
ADMIN = []
for i in admins:
  ADMIN.append(int(i[1]))


print(ADMIN)
# ADMIN = []