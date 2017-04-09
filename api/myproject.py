import sqlite3
from flask import Flask, g, jsonify, request, redirect, url_for

app = Flask(__name__, static_folder="doc")
app.config.from_object(__name__)

DATABASE = 'api/test.db'

# BOF Model (by Flask)
with app.app_context():
    def get_db():
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect(DATABASE)
            db.row_factory = make_dicts
        return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv
# EOF Flask Model

# BOF Routes / Controller


@app.route('/client/')
def index():
    return redirect(url_for('static', filename='client/index.html'))


@app.route('/doc/')
# URL for documentation made with apidocjs
def doc():
    return redirect(url_for('static', filename='index.html'))


@app.route('/data/', methods=['GET', 'POST'])
@app.route('/data/<int:id>/')
def api(id=None):
    """
    @api {get} data/:id Read data
    @apiName GetData
    @apiGroup Data
    @apiVersion 0.0.1
    @apiDescription Return last data in JSON, or a specific one with optionnal ID.

    @apiParam {int} id Data unique ID (optionnal)

    @apiSuccess {int} id ID of the entry in the database
    @apiSuccess {date} date_enr  Creation date of the entry, format : YYYY-MM-DD
    @apiSuccess {time} heure_enr  Creation hour of the entry, format : HH:MM:SS (UTC+2)
    @apiSuccess {decimal} temp  Temperature, unit : °C
    @apiSuccess {decimal} hum  Humidity, unit : %

    @apiSuccessExample Success-Response:
        HTTP/1.1 200 OK
        {
            "date_enr": "2017-04-06",
            "heure_enr": "21:17:24",
            "hum": 35,
            "id": 42,
            "temp": 25
        }
    """
    if request.method == 'GET':
        if(id is not None):
            getid = query_db("SELECT * FROM data WHERE id = ?", [id], one=True)
            return jsonify(getid)
        else:
            getlastrecord = query_db("SELECT * FROM data \
                ORDER BY id DESC LIMIT 1")
            return jsonify(getlastrecord)

    """
    @api {post} data/ Record data
    @apiName PostData
    @apiGroup Data
    @apiVersion 0.0.1
    @apiDescription Data sent from NodeMCU to a Raspberry Pi web server.
    """
    if request.method == 'POST':
        content = request.get_json(silent=True)
#       content = {"temp": 41.56, "hum": 48.4}
        temp = content["temp"]
        hum = content["hum"]
        db = get_db()
        db.execute("INSERT INTO data ( date_enr, heure_enr, temp, hum ) VALUES \
            ( date('now', 'localtime'), time('now', 'localtime'), ?, ? )", [
            temp, hum])
        db.commit()
        return "Temp. : " + str(temp) + " | Hum. : " + str(hum)


@app.route('/data/all')
def api_getall():
    """
    @api {get} data/all Read all data
    @apiName GetAll
    @apiGroup Data
    @apiVersion 0.0.1
    @apiDescription Return entries from the database.

    @apiExample {curl} Example usage:
        curl -i http://localhost:5000/data/all
    """
    getall = query_db("SELECT * FROM data")
    return jsonify(getall)


@app.route('/data/first/<int:num>/')
def api_getfirst(num):
    """
    @api {get} data/first/:num Read first data
    @apiName GetFirst
    @apiGroup Data
    @apiVersion 0.0.1
    @apiDescription Return n first data in JSON format.

    @apiParam {int} num Number of entries wanted
    """
    getfirst = query_db("SELECT * FROM data ORDER BY id LIMIT ?", [num])
    return jsonify(getfirst)


@app.route('/data/last/<int:num>/')
def api_getlast(num):
    """
    @api {get} data/last/:num Read last data
    @apiName GetLast
    @apiGroup Data
    @apiVersion 0.0.1
    @apiDescription Return n last data in JSON format.

    @apiParam {int} num Number of entries wanted

    @apiExample {curl} Example usage - Return the 10 last data :
        curl -i http://localhost:5000/data/last/10
    """
    getlast = query_db("SELECT * FROM data ORDER BY id DESC LIMIT ?", [num])
    return jsonify(getlast)


@app.route('/data/<start_date>/<end_date>/')
def api_getdates(start_date, end_date):
    """
    @api {get} data/:start_date/:end_date Read data (days)
    @apiName GetDates
    @apiGroup Data
    @apiVersion 0.0.1
    @apiDescription Return data from date 1 to date 2 in JSON format.

    @apiParam {date} start_date Format YYYY-MM-DD
    @apiParam {date} end_date Format YYYY-MM-DD

    @apiExample {curl} Example usage - Return data from 2017-04-06 to 2017-04-09 :
        curl -i http://localhost:5000/data/2017-04-06/2017-04-09
    """
    getdates = query_db("SELECT * FROM data WHERE date_enr BETWEEN ? AND ?",
                        [start_date, end_date])
    return jsonify(getdates)


@app.route('/data/hours/<start_hour>/<end_hour>/')
def api_gethours(start_hour, end_hour):
    """
    @api {get} data/:start_hour/:end_hour Read data (hours)
    @apiName GetHours
    @apiGroup Data
    @apiVersion 0.0.1
    @apiDescription Return data from hour 1 to hour 2 in JSON format.

    @apiParam {time} start_hour Format HH:MM:SS
    @apiParam {time} end_hour Format HH:MM:SS

    @apiExample {curl} Example usage - Return every morning data :
        curl -i http://localhost:5000/data/08:00:00/12:00:00
    """
    gethours = query_db("SELECT * FROM data WHERE heure_enr BETWEEN ? AND ?",
                        [start_hour, end_hour])
    return jsonify(gethours)


@app.route('/data/temp/')
def api_gettemp():
    """
    @api {get} data/temp Read temperatures
    @apiName GetTemp
    @apiGroup Data
    @apiVersion 0.0.1
    @apiDescription Return every temperature with its timestamp.
    """
    temp = query_db("SELECT date_enr || ' ' || heure_enr AS timestamp, temp \
                    FROM data")
    return jsonify(temp)


@app.route('/data/hum/')
def api_gethum():
    """
    @api {get} data/hum Read humidity
    @apiName GetHum
    @apiGroup Data
    @apiVersion 0.0.1
    @apiDescription Return every humidity with its timestamp.
    """
    hum = query_db("SELECT date_enr || ' ' || heure_enr AS timestamp, hum \
                    FROM data")
    return jsonify(hum)


@app.route('/data/temp-hum/')
def api_gettemphum():
    """
    @api {get} data/temp-hum Read temperature and humidity
    @apiName GetTempHum
    @apiGroup Data
    @apiVersion 0.0.1
    @apiDescription Return every temperature and humidity with their timestamp.

    @apiSuccess {decimal} hum  Humidity, unit : %
    @apiSuccess {decimal} temp  Temperature, unit : °C
    @apiSuccess {datetime} timestamp  Timestamp from the database record

    @apiSuccessExample Success-Response:
        HTTP/1.1 200 OK
        {
            "hum": 35,
            "temp": 25,
            "timestamp": "2017-04-06 21:17:24"
        }
    """
    temphum = query_db("SELECT date_enr || ' ' || heure_enr AS timestamp, \
                        temp, hum FROM data")
    return jsonify(temphum)
# EOF Routes


# BOF Serveur
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
# EOF Serveur
