'''
LoginController :
    This controller handles authenticating users for the application and
    redirecting them to your home screen.
'''
from models.AuthModel import AuthModel
class AuthController:

    status = {
                'code':1,
                'message':'Successful Execution',
                'role': ''
              }

    def login(self,username,password):

        if len(username) == 0:
            self.status['code'] = 0
            self.status['message'] = 'Username cannot be empty'
            return  self.status

        if len(password) == 0:
            self.status['code'] = 0
            self.status['message'] = 'Password cannot be empty'
            return  self.status

        am = AuthModel()
        result = am.checkUser(username,password)

        if result:
            self.status['role'] = result[5]
            self.status['code']=1
            self.status['message'] = 'Login Successful'
            return self.status
        else:
            self.status['code'] = 0
            self.status['message'] = 'Username or Password is incorrect'
            return self.status

    def register(self,name,phone,email,username,password):

        if len(name) == 0:
            self.status['code']  = 0
            self.status['message'] = 'Name cannot be empty'
            return self.status

        if len(phone) < 10:
            self.status['code']  = 0
            self.status['message'] = 'Phone number cannot be less than 10 digits'
            return self.status

        if len(email) == 0:
            self.status['code']  = 0
            self.status['message'] = 'Email cannot be empty'
            return self.status

        if len(username) == 0:
            self.status['code']  = 0
            self.status['message'] = 'Username cannot be empty'
            return self.status

        if len(password) == 0:
            self.status['code']  = 0
            self.status['message'] = 'Password cannot be empty'
            return self.status

        am = AuthModel()
        result = am.saveUser(name,phone,email,username,password)

        if result:
            self.status['code'] = 1
            self.status['message'] = 'Successfully created used. You can login now'
            return self.status
        else:
            self.status['code'] = 0
            self.status['message'] = 'Some database error kindly retry'
            return self.status