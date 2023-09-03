import hvac
from hvac.exceptions import InvalidPath

def role_delete(func):
   
    def wrapper(*args, **kwargs):
        client = args[0].client
        method = args[0].method
        try:
            role_list = getattr(client.auth, method).list_roles(mount_point=method)['keys']
            for role in role_list:
                getattr(client.auth, method).delete_role(mount_point=method, role=role)
        except InvalidPath as e:
            print('List is of roles is empty')
        finally:                   
            func(*args, **kwargs)
    return wrapper