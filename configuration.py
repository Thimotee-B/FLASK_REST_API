import connexion
import pathlib
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import MetaData

basedir = pathlib.Path(__file__).parent.resolve()
print(f"sqlite:///{basedir / 'referential.db'}")
application = connexion.App(__name__, specification_dir=basedir)

app = application.app
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{basedir / 'referential.db'}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

metadata = MetaData()
db = SQLAlchemy(app)
ma = Marshmallow(app)
