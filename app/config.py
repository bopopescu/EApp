# Import Section
from app import app
import random
import string
# end import section


# app configurations
app.config['SECRET_KEY'] = "".join([random.choice(string.printable) for _ in range(50)])
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Gloyane@160298@localhost/eadata'