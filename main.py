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
import webapp2, cgi, re

USER_REGEX = "^[a-zA-Z0-9_-]{3,20}$"
PWD_REGEX = "^.{3,20}$"
EMAIL_REGEX = "^[\S]+@[\S]+.[\S]+$"

page_header = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <title>User Signup</title>
</head>
<body>
    <h1>Enter your user information</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):

    def GetErrorMsg(error):


    def get(self):

        error_user = GetErrorMsg(self.request.get('error_user'))
        error_password = GetErrorMsg(self.request.get('error_password'))
        error_match = GetErrorMsg(self.request.get('error_match'))
        error_email = GetErrorMsg(self.request.get('error_email'))

        new_user_form = """
        <form action="/add" method="post">
            <label>
                Name:
                <input type="text" name="user_name" />
            </label>{0},
            <label>
                Password:
                <input type="password" name="password" />
            </label>{1}
            <label>
                Retype Password:
                <input type="password" name="password_check" />
            </label>{2}
            <label>
                Email:
                <input type="text" name="user_email" />
            </label>{3}
            <input type="submit" value="Add Me!"/>
        </form>
        """.format(error_user, error_password, error_match, error_email)



        content = page_header + new_user_form + page_footer
        self.response.write(content)


class AddUser(webapp2.RequestHandler):

    def post(self):
        user_name = cgi.escape(self.request.get("user_name"), quote=True)
        if user_name == "":
            error_user = "Please enter a user name"
        elif
        else:
            new_movie_element = "<strong>" + new_movie + "</strong>"
            sentence = new_movie_element + " has been added to your Watchlist!"

            content = page_header + "<p>" + sentence + "</p>" + page_footer
            self.response.write(content)



class CrossOffMovie(webapp2.RequestHandler):
    """ Handles requests coming in to '/cross-off'
        e.g. www.flicklist.com/cross-off
    """

    def post(self):
        # look inside the request to figure out what the user typed
        crossed_off_movie = self.request.get("crossed-off-movie")

        # build response content
        crossed_off_movie_element = "<strike>" + crossed_off_movie + "</strike>"
        confirmation = crossed_off_movie_element + " has been crossed off your Watchlist."

        content = page_header + "<p>" + confirmation + "</p>" + page_footer
        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', Index),
    ('/add', AddUser),
    ('/cross-off', CrossOffMovie)
], debug=True)
