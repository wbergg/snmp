from snmp_helper import snmp_get_oid,snmp_extract

def poll_name(a_device, oid):
    snmp_data = snmp_get_oid(a_device, oid=oid)
    return snmp_extract(snmp_data)

def poll_version(a_device, oid):
    snmp_data = snmp_get_oid(a_device, oid=oid)
    return snmp_extract(snmp_data)

def main():
    router1 = ('x.x.x.x', 'community', port)
    router2 = ('x.x.x.x', 'community', port)
    router_list = [router1, router2]
    SYSNAME = '1.3.6.1.2.1.1.5.0'
    SYSVERSION = '1.3.6.1.2.1.1.1.0'
    for f in router_list:
        print poll_name(f, SYSNAME) + "\n---------"
        print poll_version(f, SYSVERSION) +"\n---------"

main()
