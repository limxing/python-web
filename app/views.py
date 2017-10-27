from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm
import tushare as ts
from app import db, models

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Miguel'}  # fake user
	return render_template("index.html",
						   title='Home',
						   user=user)
@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		users = models.User.query.all()
		return render_template("index.html",
						title='Home',
						user=users[0])

		# flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
		# df = ts.get_tick_data(form.openid.data, date='2017-10-25')
		# df = ts.get_realtime_quotes(form.openid.data)
		# df = ts.get_today_ticks(form.openid.data)
		# df = ts.get_latest_news(top=50, show_content=True)  # 显示最新5条新闻，并打印出新闻内容
		# df.head(10)
		# return df.to_json(orient='table')
		# return redirect('/index')
	return render_template('login.html',
						   title='Sign In',
						   form=form,
						   providers=app.config['OPENID_PROVIDERS'])