from main import app
from notebook_app.views import RegisterNewUser, WorkWithNotebook

app.add_url_rule('/register/', view_func=RegisterNewUser.as_view('register'))
app.add_url_rule('/notebook/', view_func=WorkWithNotebook.as_view('notebook'))
