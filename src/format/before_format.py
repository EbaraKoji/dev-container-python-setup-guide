# press `command + S` to format and `command + option + U` to unify quotes!

# imports should be sorted(standard => third party => local)
import os
from datetime import date
import mypy  # noqa F401
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
from app.schemas import User  # type: ignore

# should be <80 characters in one line
user = User(username='Ebara', email='ebara@example.com', password='supersecret', birthday=date(1994, 7, 25), email_verified=False,)

# should be 2 blank lines before function
def show_birthday(user: User):
    if user.birthday is None:
        # indented should be 4 characters
        print("birthday is not yet set.")  # should use single quote
    else:
        # should be double quote
        print(f"birthday: {user.birthday.strftime('%Y/%m/%d')}")




# should be <2 blank lines
show_birthday(user)  # at least two spaces before inline comment
# XXX: As string is not formatted automatically even if too long, should be formatted by hand
print('---------------------------------------------------------------------------')
# newline at end of file
