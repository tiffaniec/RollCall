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
import webapp2, os, jinja2

from google.appengine.api import users #Google login
from google.appengine.ext import ndb #Cloud storage

#Say where you are keeping your HTML templates for Jinja2
template_directory = os.path.join(os.path.dirname(__file__), 'templates')
#Create a Jinja environment object by passing it the template location
jinja_environment = jinja2.Environment(loader = jinja2.FileSystemLoader(template_directory))

class Student(ndb.Model): #Define a person class
    name = ndb.StringProperty() #Must specify the type the variable will be
    grad_yr = ndb.IntegerProperty() #: this does not give them a value
    schedule = ndb.StringProperty(repeated = True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user: #true if user is logged in
            nickname = user.nickname() #nickname is email address before @

            # url = users.create_logout_url('/') #url to redirect to once logged out
            #  #the href text that will show on index.html
            # # self.response.out.write(template.render(url = url, url_text = url_text, kind = type, name = user_name, items = items)

            q_usr_exist = Student.query(Student.name == nickname)
            if q_usr_exist.get() is None:
                std_current = Student(name = nickname, schedule =[])
                std_current.put()
                self.redirect("/pg2")

            else:
                self.redirect("/pg3")

        else:
            url = users.create_login_url('/') #url to redirect to once logged in
            template = jinja_environment.get_template('index.html')
            self.response.out.write(template.render(url = url))

class pg2Handler(webapp2.RequestHandler):

    def get(self):
        logout_url = users.create_logout_url('/')
        template = jinja_environment.get_template('pg2.html')
        self.response.out.write(template.render(url = logout_url))

class pg3Handler(webapp2.RequestHandler):
    def get_user(self):
        currentUser = users.get_current_user() #Check if logged in or not
        nickname = currentUser.nickname()
        print(nickname)
        query = Student.query(Student.name == nickname)
        return query.get()

    def post(self):

        user = self.get_user()
        grad_yr = self.request.get('input_grad_yr')


        user.schedule.append(self.request.get("_1c", "input_1t"))
        user.schedule.append(self.request.get("input_2c", "input_2t"))
        user.schedule.append(self.request.get("input_3c", "input_3t"))
        user.schedule.append(self.request.get("input_4c", "input_4t"))
        user.schedule.append(self.request.get("input_5c", "input_5t"))
        user.schedule.append(self.request.get("input_6c", "input_6t"))

        user.put()

    def get(self):
        template = jinja_environment.get_template('pg3.html')
        self.response.out.write(template.render())

class AboutUsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('aboutUS.html')
        self.response.out.write(template.render())

class ContactHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('contact.html')
        self.response.out.write(template.render())

class HowItWorksHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('howItWorks.html')
        self.response.out.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/pg2', pg2Handler),
    ('/pg3', pg3Handler),
    ('/AboutUs', AboutUsHandler),
    ('/Contact', ContactHandler),
    ('/howItWorks', HowItWorksHandler),
], debug=True)
