import os
import kopf
import yaml
from client import client

from auth_methods.aws_auth import AwsAuth
from auth_methods.oidc_auth import OidcAuth

@kopf.on.create('awslogins')
def create_aws(spec, name, namespace, logger, **kwargs):
    print(client.is_authenticated())
    auth = AwsAuth(client)
    auth.enableAuth()
    auth.createRoles(spec.get('roles'))

@kopf.on.delete('awslogins')
def disable_aws(spec, name, namespace, logger, **kwargs):
    auth = AwsAuth(client)
    auth.disableAuth()

@kopf.on.update('awslogins')
def update_aws(spec, name, namespace, logger, **kwargs):
    print(client.is_authenticated())
    auth = AwsAuth(client)
    auth.updateRoles(spec.get('roles'))

@kopf.on.create('oidclogins')
def create_oidc(spec, name, namespace, logger, **kwargs):
    print(client.is_authenticated())
    auth = OidcAuth(client)
    print(spec)
    auth.enableAuth(spec['oidc_conf']['oidc_discovery_url'], spec['oidc_conf']['oidc_discovery_ca_pem'])