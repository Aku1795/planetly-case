import json
import os

from flask import request, Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base

#ap
app = Flask(__name__)


#DB connection
user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST'] 
database = os.environ['POSTGRES_DB']
port = os.environ['POSTGRES_PORT']

DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI


db = SQLAlchemy(app)

#DB models
Base = automap_base()
Base.prepare(db.engine, reflect =True)
#TemperaturesByCity = 




#Routes
@app.route('/')
def index():
    return 'Hello world  fkoffkspe'



if __name__ == '__main__':
    app.run(debug= True, host='0.0.0.0')