#!/usr/bin/python

from snmp_helper import snmp_get_oid,snmp_extract

def snmp_poll(a_device, oid):
    snmp_data = snmp_get_oid(a_device, oid=oid)
    return snmp_extract(snmp_data)

def main():
    router_list = [('x.x.x.x', 'community', 161), ('x.x.x.x', 'community', 161)]
    OIDLIST = [('1.3.6.1.2.1.1.5.0'), ('1.3.6.1.2.1.1.1.0')]
    for router in router_list:
        for oid in OIDLIST:
            print snmp_poll(router, oid) + "\n---------"

if __name__ == "__main__":
    main()
