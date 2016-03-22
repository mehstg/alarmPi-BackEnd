#!env/bin/python
import flask, time
from dbConnector import dbConnector


app =flask.Flask(__name__)
db = dbConnector('alarmPi.db')

records = db.getAllRecords()

alarmlog = []
for record in records:
    print 'Generating output dictionary'
    dt = time.strftime("%d-%m-%Y", time.gmtime(record[1]))
    tm = time.strftime("%H:%M:%S", time.gmtime(record[1]))
    alarmlog.append({u'Date': dt,  u'Time': tm, u'StateChange': record[2]})



state = {u'IsArmed': False, u'Log': alarmlog, u'Title': u'Wansbeck Alarm Panel'}


@app.route('/api/v1.0/getState', methods=['GET'])
def get_state():
    return flask.jsonify(state)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
