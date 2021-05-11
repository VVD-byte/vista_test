from database.scheme import db, User, Notebook, Note

db.create_all()

# admin = User(username='admin', email='@example.com', password='test')
# db.session.add(admin)
# db.session.commit()
# user = User.query.filter_by(email='@example.com')
# print(user)
# print(user.first().id)
