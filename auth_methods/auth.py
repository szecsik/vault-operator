class Authentication():
    def __init__(self, method, client):
        self.method = method
        self.client = client

    def enableAuth(self):
        return

    def disableAuth(self):
        print("Disabling "+self.method)
        self.client.sys.disable_auth_method(self.method)

    def role_delete(self,func, method, client):
        def wrapper():
            role_list = getattr(client.auth, method).list_roles(mount_point=method)['keys']
            for role in role_list:
                getattr(client.auth, method).delete_role(mount_point=method, role=role)
            func()    
        return wrapper    
