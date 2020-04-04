from werkzeug import generate_password_hash, check_password_hash

##用户身份类
class Permission:
    ROLE_USER = 10
    ROLE_FORUMADMIN = 20
    ROLE_ADMIN = 30

##用于创建用户账号
class User:
    def __init__(self, name, email, password, role = Permission.ROLE_USER):
        self.name = name
        self.email = email
        self.password_hash = self.save_password(password)
        self.role = role

    def save_password(self, password):
        return generate_password_hash

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)

    ##判断用户是否为管理员
    @property
    def is_admin(self):
        return self.role == Permission.ROLE_ADMIN

    ##改变用户权限
    def change_role(self,role):
        self.role = role
            
def main():
    
    user1 = User('James', 'james@haha.com', '123456')

    user2 = User('Admin', 'admin@haha.com', '123456', Permission.ROLE_ADMIN )

    for user in (user1, user2):
        if user.is_admin:
            print('{}是管理员'.format(user.name))
        else:
            print('{}不是管理员'.format(user.name))
            user.change_role(Permission.ROLE_ADMIN)
            print('修改角色后,{}变成管理员'.format(user.name))

if __name__ == '__main__':
    main()
    



    
