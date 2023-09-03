from auth_methods.auth import Authentication
from  auth_methods.auth_decorator import role_delete

class AwsAuth(Authentication):
    
    def __init__(self, client):
        self.method = "aws"
        self.client = client

    def enableAuth(self):
        print("Enabling AWS Auth")
        self.client.sys.enable_auth_method(self.method)

    def createRole(self,name,auth_type,bound_iam_principal_arn,policies,max_ttl):
        self.client.auth.aws.create_role(mount_point='aws', role=name, bound_iam_principal_arn=bound_iam_principal_arn, policies=policies, max_ttl=max_ttl)

    def createRoles(self, roles):
        for role in roles:
            self.createRole(role['name'],role['auth_type'],role['bound_iam_principal_arn'],role['policies'],role['max_ttl'])

    @role_delete
    def updateRoles(self, roles):
     for r in roles:
        self.createRole(r['name'],r['auth_type'],r['bound_iam_principal_arn'],r['policies'],r['max_ttl'])