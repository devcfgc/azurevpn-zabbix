azurevpn-zabbix
---------------

A python script to monitor the health of an azure vpn from zabbix.
If the status is different from "Connected" we raise an alert on zabbix

usage:
```shell
> azurevpn-zabbix.py oauth_url client_id client_secret subscription_id resource_group gateway
```

```shell
Usage: azurevpn-zabbix.py [options]

This Zabbix plugin checks the health of an azure vpn.

Options:
  --help              show this help message and exit
  -o OAUTH_URL,       --oauth=OAUTH_URL                 Your azure ouath2 url
  -i CLIENT_ID,       --clientid=CLIENT_ID              Your azure client_id
  -s CLIENT_SECRET,   --clientsecret=CLIENT_SECRET      Your azure client_secret
  -u SUBSCRIPTION_ID, --subscriptionid=SUBSCRIPTION_ID  Your azure subscription_id
  -r RESOURCE_GROUP,  --resourcegroup=RESOURCE_GROUP    Your azure resource group
  -g GATEWAY,         --gateway=GATEWAY                 Your azure gateway name
```

###using with zabbix_sender
If you want to use this script with the zabbix_sender utility then there's a [shell script provided](zabbix-sender.sh) which will invoke azurevpn-zabbix.py and pipe the result to zabbix_sender.

Usually you would invoke this from a cron-job (or similar)

```
*/2 * * * * /path/to/azurevpn-zabbix/zabbix-sender.sh myzabbix.server.com [options] > /dev/null 2>&1
```
