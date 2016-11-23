#!/bin/bash
dirBase="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
datasend_zabbix="$dirBase/datasend_zabbix_azurevpn.conf"
azurevpninfo=`$dirBase/azurevpn-zabbix.py -o $2 -i $3 -s $4 -u $5 -r $6 -g $7`

echo "$azurevpninfo" > $datasend_zabbix
zabbix_sender -z $1 -i $datasend_zabbix
