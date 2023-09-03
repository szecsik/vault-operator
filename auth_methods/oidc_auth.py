from auth_methods.auth import Authentication

class OidcAuth(Authentication):
    
    def __init__(self, client):
        self.method = "oidc"
        self.client = client

    def enableAuth(self, url, pem=None):
        print("Enabling OIDC Auth")
        self.client.sys.enable_auth_method(self.method)
        print("Configuration")
        self.client.auth.oidc.configure(
        oidc_discovery_url=url,
        oidc_discovery_ca_pem=pem,
         )