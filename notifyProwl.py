#!env/bin/python
import logging, requests

class notifyProwl():
    def __init__(self,apikey):
    	self.apikey = apikey
    
    availableStates = ['arm', 'disarm', 'triggered', 'reset']


    def notify(self, state):
	if state in self.availableStates:
		if state  == 'triggered':
			self._pushMessage('2','Wansbeck Alarm','Alarm Status','Alarm Triggered')
			logging.debug("Alarm triggered notification")
		elif state == 'arm':
			self._pushMessage('-2','Wansbeck Alarm','Alarm Status','Alarm Armed')
			logging.debug("Alarm armed notification")
		elif state == 'disarm':
			self._pushMessage('-2','Wansbeck Alarm','Alarm Status','Alarm Disarmed')
			logging.debug("Alarm disarmed notification")
		elif state == 'reset':
			self._pushMessage('0','Wansbeck Alarm','Alarm Status','Alarm Reset')
			logging.debug("Alarm reset notification")

    # Private method to actually send message
    def _pushMessage(self,priority,application,event,description):
	logging.debug("Building Prowl message")
	payload = {'apikey': self.apikey, 'priority': priority, 'application': application, 'event': event, 'description': description}
	url = 'https://api.prowlapp.com/publicapi/add'
	try:
	    logging.debug("Posting Prowl message")
            r = requests.post(url, data=payload)
	except:
	    logging.error("Prowl message failed to post")
	    return False
