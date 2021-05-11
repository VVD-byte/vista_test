import hashlib
import random

from main import db
from sqlalchemy_serializer import SerializerMixin


class User(db.Model, SerializerMixin):
    __tablename__ = 'user'
    serialize_only = ('email', )

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)  # Уникальный эмайл
    password = db.Column(db.String(80), nullable=False)
    salt = db.Column(db.String(12), nullable=False)  # соль для пароля
    notebook = db.relationship('Notebook', lazy=True)  # Все книжки данного пользовател

    def __init__(self, email, password):
        super().__init__()
        self.email = email
        self.salt = self.generate_salt
        self.password = self.get_hash_sha256(password)

    def __repr__(self):
        return '<User %r>' % self.email

    def check_password(self, password: str) -> bool:
        if self.get_hash_sha256(password) == self.password:
            return True
        return False

    def get_hash_sha256(self, passwd: str) -> str:
        return hashlib.sha256((passwd + self.salt).encode('utf-8')).hexdigest()

    @property
    def generate_salt(self) -> str:
        return ''.join([random.choice(list('qwertyuiopasdfghjklzxcvbnm')) for i in range(12)])


class Notebook(db.Model, SerializerMixin):
    __tablename__ = 'notebook'
    serialize_only = ('name', 'note')

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Ссылка на владельца (таблица User)
    name = db.Column(db.String(100), nullable=False)  # Название книжки
    note = db.relationship('Note', lazy=True)  # Все записи этой книги

    def add_notebook(self, user):
        db.session.add(self)
        user.notebook.append(self)
        db.session.commit()

    def delete_notebook_for_user(self, user):
        user.notebook.delete(self)
        db.session.delete(self)
        db.session.commit()

    def __init__(self, user, name):
        super().__init__()
        self.user = user
        self.name = name

    def __repr__(self):
        return '<Notebook %r>' % self.name


class Note(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    notebook = db.Column(db.Integer, db.ForeignKey('notebook.id'), nullable=False)  # Ссылка на книжку(таблица Notebook)
    name = db.Column(db.String(100), nullable=False)  # название записи
    text = db.Column(db.Text, nullable=False)  # содержимое записи

    def __repr__(self):
        return '<Note %r>' % self.name
