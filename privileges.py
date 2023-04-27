class Privileges:
    def __init__(self) -> None:
        self.privilages = ["can add post", "can delete post", "can ban user"]


    def show_privileges(self):
          print("The Admin has the following privileges:")
          for privilage in self.privilages:
               print(f'{privilage}')    