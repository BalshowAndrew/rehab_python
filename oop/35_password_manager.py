""""Менеджек паролей"""

class PasswordManager:
    """Class PasswordManager"""
    def __init__(self):
        self._passwords = {}
    
    def add_password(self, service: str, password: str):
        self._passwords[service] = password

    def get_pasword(self, service: str):
        return self._passwords.get(service)


my_passwords = PasswordManager()

my_passwords.add_password('smart_home', '12345')
my_passwords.add_password('google_disk', '54321')

print(my_passwords.get_pasword('smart_home'))
print(my_passwords.get_pasword('google_disk'))
print(my_passwords.get_pasword('stupid_home'))

my_passwords.add_password('telecom', 'abracadabra')
print(my_passwords.get_pasword('telecom'))
