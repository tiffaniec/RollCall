#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2, jinja2, os

from google.appengine.ext import ndb

template_directory = os.path.join(os.path.dirname(__file__), 'templates')#telling where templates agr
jinja_environment = jinja2.Environment(loader = jinja2.FileSystemLoader(template_directory))

class User(ndb.Model):
    name = ndb.StringProperty()
    age= ndb.IntegerProperty()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        new_user = User(name = "Bob", age=12)
        key = new_user.put()#in cloud
        returnedUser = key.get()



        template = jinja_environment.get_template('index.html')
        anotherNumber = 8
        exampleList = ['Begin', 1,2,3, 'End']
        self.response.out.write(template.render(number = anotherNumber,
        list = exampleList))

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('about.html')
        self.response.write(template.render())

class OutputHandler(webapp2.RequestHandler):
    def post(self):
        data = self.request.get('userInput')

        template = jinja_environment.get_template('output.html')
        self.response.out.write(template.render(data = data))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/about', AboutHandler),
    ('/output', OutputHandler)
], debug=True)
