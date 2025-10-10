class Users:
      _amount_of_accounts = 0
      _account_types = ["admin", "member", "guest"]
      
      def __init__(self, username, password, role, isActive):
            roleCheck = len(self._account_types)
            for i in range(len(Users._account_types)):
                  if role == Users._account_types[i]:
                        self._role = role
                  else:
                        roleCheck -= 1
            if roleCheck == 0:
                  raise ValueError("No valid role submitted")
                  
            self._username = username
            self._password = password
            self._is_active = isActive if isActive == 1 else 0 
            
            Users._amount_of_accounts += 1
            
      def __str__(self):
            string = f"USERNAME: {self._username}, ROLE: {self._role},"
            if self._is_active == 0:
                  string += " INACTIVE ACCOUNT"
            else:
                  string += " ACTIVE ACCOUNT"
            return string
            
      def change_password(self, new_password):
            if new_password == self._password:
                  raise ValueError("Cannot set the new password to the old password")
            elif len(new_password) < 5:
                  raise ValueError("Password needs to be at least 5 characters long")
            else:
                  self._password = new_password
                  
      def disable_account(self):
            self._is_active = 0
            
      def enable_account(self):
            self._is_active = 1
            
      def is_active(self):
            return self._is_active
            
      def auth(self, username, password):
            if username is None or password is None:
                  raise ValueError("Need to submit both username and password")
            elif username != self._username or password != self._password:
                  raise ValueError("Either username or password is incorrect")
            elif self._is_active == 0:
                  raise ValueError("Account disabled, login not permitted")
            elif username == self._username and password == self._password and self._is_active != 0:
                  return True
      def amount_of_accounts():
            print(f"{Users._amount_of_accounts} accounts exist")
                  
      @property
      def username(self):
          return self._username
          
      @property
      def password(self):
            return self._password
            
      @property
      def is_active(self):
            return self._is_active
            
      @username.setter
      def username(self, new_username):
            if new_username:
                self._username = new_username
            else:
                  raise ValueError("No username submitted")
                  
      @password.setter
      def password(self, new_password):
            if new_password != self._password:
                  self._password = new_password
                  
      @is_active.setter
      def is_active(self, new_status):
            if self._is_active != new_status:
                  self._is_active = new_status
                  
                  
while True:
      pass