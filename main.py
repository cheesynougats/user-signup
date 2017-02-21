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

error_dict = {
"user_blank":"Please enter a user name",
"user_invalid":"Valid user names are 3 to 20 characters and can include letters and numbers only",
"pwd_blank":"Please enter a password",
"pwd_invalid":"Valid passwords include 3 to 20 characters",
"pwd_mismatch":"Passwords do not match",
"email_blank":"Please enter an email address",
"email_invalid":"Email address is invalid"
}
class Index(webapp2.RequestHandler):

    def GetErrorMsg(self, error):
        return error_dict[error]


    def get(self):

        error_user = ""
        if self.request.get('error_user'):
            error_user = self.GetErrorMsg(self.request.get('error_user'))
        error_password = ""
        if self.request.get('error_password'):
            error_password = self.GetErrorMsg(self.request.get('error_password'))
        error_match = ""
        if self.request.get('error_match'):
            error_match = self.GetErrorMsg(self.request.get('error_match'))
        error_email = ""
        if self.request.get('error_email'):
            error_email = self.GetErrorMsg(self.request.get('error_email'))

        new_user_form = """
        <form action="/add" method="post">
            <label>
                Name:
                <input type="text" name="user_name" value="{4}"/>
            </label>{0}
            <br />
            <label>
                Password:
                <input type="password" name="password" />
            </label>{1}
            <br />
            <label>
                Retype Password:
                <input type="password" name="password_match" />
            </label>{2}
            <br />
            <label>
                Email:
                <input type="text" name="user_email" value="{5}"/>
            </label>{3}
            <br />
            <input type="submit" value="Add Me!"/>
        </form>
        """.format(error_user, error_password, error_match, error_email, self.request.get('user_name'), self.request.get('user_email'))



        content = page_header + new_user_form + page_footer
        self.response.write(content)


class AddUser(webapp2.RequestHandler):

    def post(self):
        user_name = cgi.escape(self.request.get("user_name"), quote=True)
        error_user = self.GetUserErrors(user_name)
        password = cgi.escape(self.request.get("password"), quote=True)
        error_password = self.GetPwdErrors(password)
        password_match = cgi.escape(self.request.get("password_match"), quote=True)
        error_match = self.GetMatchErrors(password, password_match)
        user_email = cgi.escape(self.request.get("user_email"), quote=True)
        error_email = self.GetEmailErrors(user_email)
        if error_user or error_password or error_match or error_email:
            usererror_param = "error_user=" + error_user
            passworderror_param = "error_password=" + error_password
            matcherror_param = "error_match=" + error_match
            emailerror_param = "error_email=" + error_email
            username_param = "user_name=" + user_name
            email_param = "user_email=" + user_email
            redirect_address = "/?" + usererror_param + "&" + passworderror_param + "&" + matcherror_param + "&" + emailerror_param + "&" + username_param + "&" + email_param
            self.redirect(redirect_address)
        else:
            self.response.write("Welcome, " + user_name + "!")

    def GetUserErrors(self, user_name):
        if user_name == "":
            error = "user_blank"
            return error
        else:
            user_MatchObj = re.match(USER_REGEX, user_name )
            if not user_MatchObj:
                error = "user_invalid"
                return error
        return ""

    def GetPwdErrors(self, password):

        if password == "":
            error = "pwd_blank"
            return error
        else:
            password_MatchObj = re.match(PWD_REGEX, password)
            if not password_MatchObj:
                error = "pwd_invalid"
                return error
        return ""

    def GetMatchErrors(self, password, match):

        if password != match:
            error = "pwd_mismatch"
            return error
        return ""

    def GetEmailErrors(self, user_email):
        if user_email == "":
            return ""
        else:
            email_MatchObj = re.match(EMAIL_REGEX, user_email )
            if not email_MatchObj:
                error = "email_invalid"
                return error
        return ""





app = webapp2.WSGIApplication([
    ('/', Index),
    ('/add', AddUser)

], debug=True)
