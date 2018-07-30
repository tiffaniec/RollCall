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
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

         if user: #true if user is logged in
            nickname = user.nickname() #nickname is email address before @

            url = users.create_logout_url('/') #url to redirect to once logged out
            url_text = "logout" #the href text that will show on index.html

            template = jinja_environment.get_template('index.html')
            self.response.out.write(template.render(url = url, url_text = url_text, kind = type, name = user_name, items = items))

        else:
            url = users.create_login_url('/') #url to redirect to once logged in
            url_text = "login"


        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render())

class pg2Handler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('pg2.html')
        self.response.out.write(template.render())

class pg3Handler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('pag3dropdown.html')
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
    ('/pg2' pg2Handler),
    ('/pg3', pg3Handler),
    ('/AboutUs', AboutUsHandler),
    ('/Contact', ContactHandler),
    ('/howItWorks', HowItWorksHandler),
], debug=True)
