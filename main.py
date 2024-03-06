from flask import Flask, make_response, jsonify
from data import db_session, news_api



app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'




if __name__ == '__main__':
    main()