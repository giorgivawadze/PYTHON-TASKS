import main
from privileges import Privileges

class Admin(main.User):
    def __init__(self, first_name, last_name, age, height, login_attempts=0) -> None:
        super().__init__(first_name, last_name, age, height, login_attempts)

