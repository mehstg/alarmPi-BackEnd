#!env/bin/python
import flask, time
from dbConnector import dbConnector


app =flask.Flask(__name__)
db = dbConnector('alarmPi.db')

records = db.getAllEvents()
currentstates = db.getState()

alarmlog = []
for record in records:
    dt = time.strftime("%d-%m-%Y", time.gmtime(record[1]))
    tm = time.strftime("%H:%M:%S", time.gmtime(record[1]))
    alarmlog.append({u'Date': dt,  u'Time': tm, u'StateChange': record[2]})

for s in currentstates:
    currentstate = s

if str(currentstate[1]) == 'arm':
	IsArmed = True
else:
	IsArmed = False

state = {u'IsArmed': IsArmed, u'Log': alarmlog, u'Title': u'Wansbeck Alarm Panel'}

def updateState(update):
    if db.setEvent(str(update)):
    	if db.setState(str(update)):
	    return True
	else:
	    return False
    else:
	return False


@app.route('/api/v1.0/getState', methods=['GET'])
def get_state():
    return flask.jsonify(state)

@app.route('/api/v1.0/setState', methods=['POST'])
def set_state():
    update = app.request.args.get("update")
    if updateState(update):
	return 'State updated OK'
    else:
	abort(503)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
