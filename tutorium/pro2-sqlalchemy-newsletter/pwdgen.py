# Benutzerpasswort hashen
import bcrypt

passwd = input("Bitte Password eingeben: ")
passwd_hash = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt())
print(passwd_hash)

