'''
DetectorController :
    This controller handles detection of people in
    the camera frame.
'''
from models.DetectorModel import DetectorModel

class DetectorController:

    status = {
                'code':1,
                'message':'Successful Execution'
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

        login_model = LoginModel()
        result = login_model.checkUser(username,password)
        if result:
            self.status['code']=1
            self.status['message'] = 'Login Successful'
            return self.status
        else:
            self.status['code'] = 0
            self.status['message'] = 'Username or Password is incorrect'
            return self.status