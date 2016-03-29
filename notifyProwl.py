#!env/bin/python
import logging, requests

class notifyProwl():
    def __init__(self,apikey):
    	self.apikey = apikey


    def notifyArm(self):
	self._pushMessage('0','Wansbeck Alarm','Alarm Status','Alarm Armed')

    def notifyDisarm(self):
	self._pushMessage('0','Wansbeck Alarm','Alarm Status','Alarm Disarmed')

    def notifyTriggered(self):
	self._pushMessage('0','Wansbeck Alarm','Alarm Status','Alarm Triggered')

    def notifyReset(self):
        self._pushMessage('0','Wansbeck Alarm','Alarm Status','Alarm Reset')



    # Private method to actually send message
    def _pushMessage(self,priority,application,event,description):
	logging.debug("Building Prowl message")
	payload = {'apikey': self.apikey, 'priority': priority, 'application': application, 'event': event, 'description': description}
	url = 'https://api.prowlapp.com/publicapi/add'
	try:
	    logging.debug("Posting Prowl message")
            r = requests.post(url, data=payload)
	except:
	    return False
