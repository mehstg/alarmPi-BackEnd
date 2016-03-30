#!env/bin/python
import flask, time, logging, sys, pytz
import dbConnector, notifyProwl

# Properties file in gitignore - Needs creating if it does not exist
import properties

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

app =flask.Flask(__name__)
db = dbConnector.dbConnector('alarmPi.db')
notification = notifyProwl.notifyProwl(properties.prowlAPIKey)

def getState():
    records = db.getAllEvents()
    currentstates = db.getState()

    alarmlog = []
    for record in records:
    	dt = time.strftime("%d-%m-%Y", time.gmtime(record[1]))
    	tm = time.strftime("%H:%M:%S", pytz.utc.localize(time.gmtime(record[1]), is_dst=None).astimezone(timezone))
    	alarmlog.append({u'Date': dt,  u'Time': tm, u'StateChange': record[2]})

    for s in currentstates:
    	currentstate = s

    if str(currentstate[1]) == 'arm':
	IsArmed = True
    else:
	IsArmed = False

    return {u'IsArmed': IsArmed, u'Log': alarmlog, u'Title': u'Wansbeck Alarm Panel'}



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
    return flask.jsonify(getState())

@app.route('/api/v1.0/setState', methods=['POST'])
def set_state():
    if not flask.request.json or not 'state' in flask.request.json:
    	flask.abort(400)

    if updateState(flask.request.json['state']):
	notification.notify(flask.request.json['state'])
	return 'State updated OK'
    else:
	flask.abort(503)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
