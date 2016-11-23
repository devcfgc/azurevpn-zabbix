#!/usr/bin/env python
import json
import optparse

from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

p = optparse.OptionParser()
p.add_option('-o', '--oauth', action='store', type='string', dest='oauth', default=None, help='oauth url')
p.add_option('-i', '--clientid', action='store', type='string', dest='clientid', default=None, help='client_id')
p.add_option('-s', '--clientsecret', action='store', type='string', dest='clientsecret', default=None, help='client_secret')
p.add_option('-u', '--subscriptionid', action='store', type='string', dest='subscriptionid', default=None, help='subscription_id')
p.add_option('-r', '--resourcegroup', action='store', type='string', dest='resourcegroup', default=None, help='resource group name')
p.add_option('-g', '--gateway', action='store', type='string', dest='gateway', default=None, help='gateway name')

options, args = p.parse_args()

OAUTH_URL = options.oauth
CLIENT_ID = options.clientid
CLIENT_SECRET = options.clientsecret
SUBSCRIPTION_ID = options.subscriptionid
RESOURCE_GROUP_NAME = options.resourcegroup
VPN_GATEWAY_NAME = options.gateway

VPN_GATEWAY_API = 'https://management.azure.com/subscriptions/' \
                  + SUBSCRIPTION_ID + '/resourceGroups/' \
                  + RESOURCE_GROUP_NAME + '/providers/Microsoft.Network/virtualNetworkGateways/' \
                  + VPN_GATEWAY_NAME + '/connections?api-version=2016-09-01'

client = BackendApplicationClient(client_id=CLIENT_ID)
oauth = OAuth2Session(client=client)
token = oauth.fetch_token(
        token_url=OAUTH_URL,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        resource="https://management.azure.com/")

# Get list of connections from VPN Gateway
r = oauth.get(VPN_GATEWAY_API)
response = json.loads(r.content)
nconnections = len(response['value'])

# Get details of each connection
for tmp_connection in response['value']:
    c = oauth.get('https://management.azure.com' + tmp_connection['id'] + '?api-version=2016-09-01')
    connection = json.loads(c.content)
    name = connection['name']
    if connection['properties']['connectionStatus'] != "Connected":
        ingressBytesTransferred = -1
        egressBytesTransferred = -1
    else:
        ingressBytesTransferred = connection['properties']['ingressBytesTransferred']
        egressBytesTransferred = connection['properties']['egressBytesTransferred']

    print "%s rx_bytes %s" % (name, ingressBytesTransferred)
    print "%s tx_bytes %s" % (name, egressBytesTransferred)
