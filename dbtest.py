from sqlachemy import db, User

#
# db.create_all()
# admin = User('admin', 'admin@example.com')
# guest = User('guest', 'guest@example.com')
#
# db.session.add(admin)
# db.session.add(guest)
#
# db.session.commit()

users = User.query.all()
for i in users:
    print(i.__dict__)
admin = User.query.filter_by(username='admin').first()
print(admin.__dict__)
