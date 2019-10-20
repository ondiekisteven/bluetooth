import bluetooth

print("performing inquiry...")

nearby_devices = bluetooth.discover_devices(
        duration=20,  flush_cache=True, lookup_class=False)

print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    try:
        print("  %s - %s" % (addr, name))
        file = open("discovered.txt", "a")
        file.write("%s : %s " % (addr, name))
    except UnicodeEncodeError:
        print("  %s - %s" % (addr, name.encode('utf-8', 'replace')))
bluetooth.BLUETOOTH_PROFILE_DESCRIPTOR_LIST_ATTRID