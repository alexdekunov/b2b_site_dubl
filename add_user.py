from db import db_session
from models import User

# вводим данные пользователя
user = User(name="Petr", salary=25000, email='pehh7htr@dsd.ru')
# что бы добавить надо создать сессию
db_session.add(user)
db_session.commit()

