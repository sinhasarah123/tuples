import random
import string
lower=string.ascii_lowercase
upper=string.ascii_uppercase
digits=string.digits
all_char=lower+upper+digits
password_length=8
password=random.sample(all_char,password_length),random.sample(all_char,password_length)
print("your password is:","".join(password[0]))