import logging
import jinja2
import webapp2
import os
import random
import json
from google.appengine.api import channel

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

logging.getLogger().setLevel(logging.DEBUG)

users = set()

def random_string():
  str = ''
  for _ in range(4):
    str += random.choice('0123456789')
  logging.info(str)
  return str

class MainPage(webapp2.RequestHandler):
  def get(self):
    user = self.request.get('user')
    if len(user) == 0:
      user = random_string()
    token = channel.create_channel(user)
    template_values = {'token': token, 'user': user}
    template = jinja_environment.get_template('index.html')
    self.response.out.write(template.render(template_values))

class DisconnectPage(webapp2.RequestHandler):
  def post(self):
    user = self.request.get('from')
    logging.info("Disconnect: " + user)
    try:
      users.remove(user)
    except KeyError:
      logging.info('User not logged in')

class ConnectPage(webapp2.RequestHandler):
  def post(self):
    user = self.request.get('from')
    logging.info("Connect: " + user)
    users.add(user)

class MessagePage(webapp2.RequestHandler):
  def post(self):
    msg = json.loads(self.request.body)
    for command in msg:
      to_user = msg[command]['to']
      from_user = msg[command]['from']
    logging.info(from_user + ' -> ' + to_user + ": " + command)
    if to_user in users:
      channel.send_message(to_user, self.request.body)
    else:
      logging.info('User not found')
      channel.send_message(from_user, '{"ERROR":"User not found ' + to_user + '"}')

app = webapp2.WSGIApplication([('/', MainPage), ('/message', MessagePage), ('/_ah/channel/connected/', ConnectPage), ('/_ah/channel/disconnected/', DisconnectPage)], debug=True)
