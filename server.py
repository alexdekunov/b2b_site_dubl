from flask import Flask, render_template, url_for
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://b2bsite.db'
# db = SQLAlchemy(app)


# class Article(db.Model):
#     id = db.Colum(db.Integer, primary_key=True)
#     title = db.Colum(db.String(100), nullable=False)
#     intro = db.Colum(db.String(300), nullable=False)
#     text = db.Colum(db.Text, nullable=False)
#     date = db.Colum(db.DateTime, default=datetime.utcnow)
#
#     def __repr__(self):
#         '''выдавать объект и его ID'''
#         return '<Article %r>' % self.id


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/bootstrap')
def bootstrap():
    return render_template("bootstrap.html")


if __name__ == "__main__":
    app.run(debug=True)  # дебаг даёт перезагрузку и тестирование сайте, пустой будет не выдавать ошибки
