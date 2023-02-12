from flask import Blueprint,render_template,request,jsonify,redirect,url_for
from app import Form

views = Blueprint(__name__,"views")

@views.route('/')
def home():
        return render_template('index.html',name = 'DM')

@views.route('/profile')
def profile():
        args = request.args
        name = args.get('name')
        return render_template('index.html',name = name)

@views.route('/json')
def get_json():
        return jsonify({'name':'dm','cool':'yes'})

@views.route('/data')
def get_data():
        data = request.json
        return jsonify(data)

@views.route('/gotohome')
def gotohome():
        return redirect(url_for('views.home'))

@views.route('/form',method=['GET','POST'])
def form():
        singerName = None
        count = None
        duration = None
        outputFile = None
        form = Form()
        if form.valida
        return render_template('index.html')