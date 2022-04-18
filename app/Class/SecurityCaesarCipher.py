KEY = 3


# the latest and the safest algorithm for password security
class SecurityCaesarCipher:
    @staticmethod
    def encrypt(plain_password: str):
        encrypted_password = ""
        for i in range(len(plain_password)):
            if ord(plain_password[i]) > 122 - KEY:
                encrypted_password += chr(ord(plain_password[i]) + KEY - 26)
            else:
                encrypted_password += chr(ord(plain_password[i]) + KEY)
        return encrypted_password

    @staticmethod
    def decrypt(password):
        decrypted_password = ""
        key_m = KEY % 26

        for char in password:
            if ord(char) - key_m < 97:
                decrypted_password += chr(ord(char) - key_m + 26)
            else:
                decrypted_password += chr(ord(char) - key_m)

        return decrypted_password
