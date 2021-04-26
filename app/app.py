from typing import List, Dict
import simplejson as json
from flask import Flask, request, Response, redirect
from flask import render_template
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'fordData'
mysql.init_app(app)


@app.route('/', methods=['GET'])
def index():
    user = {'username': 'Ford Project'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblFordImport')
    result = cursor.fetchall()
    return render_template('index.html', title='Home', user=user, ford=result)


@app.route('/view/<int:ford_id>', methods=['GET'])
def record_view(ford_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblFordImport WHERE id=%s', ford_id)
    result = cursor.fetchall()
    return render_template('view.html', title='View Form', ford=result[0])


@app.route('/edit/<int:ford_id>', methods=['GET'])
def form_edit_get(ford_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblFordImport WHERE id=%s', ford_id)
    result = cursor.fetchall()
    return render_template('edit.html', title='Edit Form', ford=result[0])


@app.route('/edit/<int:ford_id>', methods=['POST'])
def form_update_post(ford_id):
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('year'), request.form.get('mileage'), request.form.get('price'), ford_id)
    sql_update_query = """UPDATE tblFordImport t SET t.year = %s, t.mileage = %s, t.price = %s = %s WHERE t.id = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/ford/new', methods=['GET'])
def form_insert_get():
    return render_template('new.html', title='New Ford Form')


@app.route('/ford/new', methods=['POST'])
def form_insert_post():
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('year'), request.form.get('mileage'), request.form.get('price'))
    sql_insert_query = """INSERT INTO tblFordImport (year,mileage, price) VALUES (%s, %s,%s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/delete/<int:ford_id>', methods=['POST'])
def form_delete_post(ford_id):
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM tblFordImport WHERE id = %s """
    cursor.execute(sql_delete_query, ford_id)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/api/v1/ford', methods=['GET'])
def api_browse() -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblFordImport')
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/ford/<int:ford_id>', methods=['GET'])
def api_retrieve(ford_id) -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblFordImport WHERE id=%s', ford_id)
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/ford/', methods=['POST'])
def api_add() -> str:
    resp = Response(status=201, mimetype='application/json')
    return resp


@app.route('/api/v1/ford/<int:ford_id>', methods=['PUT'])
def api_edit(ford_id) -> str:
    resp = Response(status=201, mimetype='application/json')
    return resp


@app.route('/api/ford/<int:ford_id>', methods=['DELETE'])
def api_delete(ford_id) -> str:
    resp = Response(status=210, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
