#!env/bin/python
from flask import Flask, jsonify
from dbConnector import dbConnector

app = Flask(__name__)
db = dbConnector('alarmPi.db')

records = db.getAllRecords()





state = {u'IsArmed': False, u'Log': [{u'Date': u'20/01/2015', u'StateChange': u'Disarmed', u'Time': u'01:50'}, {u'Date': u'20/01/2015', u'StateChange': u'Armed', u'Time': u'07:50'}], u'Title': u'WansbeckAlarm'}

@app.route('/api/v1.0/getState', methods=['GET'])
def get_state():
    return jsonify(state)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
