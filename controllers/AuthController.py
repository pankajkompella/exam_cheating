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