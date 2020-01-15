import sys
from xml.etree import ElementTree as ET
import oca

EXCEPTIONS = {'terminate': [66789]}

ADDRESS = 'https://api.hpccloud.surfsara.nl/RPC2'

STATES = {
    0: "INIT",
    1: "PENDING",
    2: "HOLD",
    3: "ACTIVE",
    4: "STOPPED",
    5: "SUSPENDED",
    6: "DONE",
    7: "FAILED",
    8: "POWEROFF",
    9: "UNDEPLOYED",
    10: "CLONING",
    11: "CLONING_FAILURE",
}
LCM_STATES = {
    0: "LCM_INIT",
    1: "PROLOG",
    2: "BOOT",
    3: "RUNNING",
    4: "MIGRATE",
    5: "SAVE_STOP",
    6: "SAVE_SUSPEND",
    7: "SAVE_MIGRATE",
    8: "PROLOG_MIGRATE",
    9: "PROLOG_RESUME",
    10: "EPILOG_STOP",
    11: "EPILOG",
    12: "SHUTDOWN",
    13: "//CANCEL",
    14: "//FAILURE",
    15: "CLEANUP_RESUBMIT",
    16: "UNKNOWN",
    17: "HOTPLUG",
    18: "SHUTDOWN_POWEROFF",
    19: "BOOT_UNKNOWN",
    20: "BOOT_POWEROFF",
    21: "BOOT_SUSPENDED",
    22: "BOOT_STOPPED",
    23: "CLEANUP_DELETE",
    24: "HOTPLUG_SNAPSHOT",
    25: "HOTPLUG_NIC",
    26: "HOTPLUG_SAVEAS",
    27: "HOTPLUG_SAVEAS_POWEROFF",
    28: "HOTPLUG_SAVEAS_SUSPENDED",
    29: "SHUTDOWN_UNDEPLOY",
    30: "EPILOG_UNDEPLOY",
    31: "PROLOG_UNDEPLOY",
    32: "BOOT_UNDEPLOY",
    33: "HOTPLUG_PROLOG_POWEROFF",
    34: "HOTPLUG_EPILOG_POWEROFF",
    35: "BOOT_MIGRATE",
    36: "BOOT_FAILURE",
    37: "BOOT_MIGRATE_FAILURE",
    38: "PROLOG_MIGRATE_FAILURE",
    39: "PROLOG_FAILURE",
    40: "EPILOG_FAILURE",
    41: "EPILOG_STOP_FAILURE",
    42: "EPILOG_UNDEPLOY_FAILURE",
    43: "PROLOG_MIGRATE_POWEROFF",
    44: "PROLOG_MIGRATE_POWEROFF_FAILURE",
    45: "PROLOG_MIGRATE_SUSPEND",
    46: "PROLOG_MIGRATE_SUSPEND_FAILURE",
    47: "BOOT_UNDEPLOY_FAILURE",
    48: "BOOT_STOPPED_FAILURE",
    49: "PROLOG_RESUME_FAILURE",
    50: "PROLOG_UNDEPLOY_FAILURE",
    51: "DISK_SNAPSHOT_POWEROFF",
    52: "DISK_SNAPSHOT_REVERT_POWEROFF",
    53: "DISK_SNAPSHOT_DELETE_POWEROFF",
    54: "DISK_SNAPSHOT_SUSPENDED",
    55: "DISK_SNAPSHOT_REVERT_SUSPENDED",
    56: "DISK_SNAPSHOT_DELETE_SUSPENDED",
    57: "DISK_SNAPSHOT",
    58: "//DISK_SNAPSHOT_REVERT",
    59: "DISK_SNAPSHOT_DELETE",
    60: "PROLOG_MIGRATE_UNKNOWN",
    61: "PROLOG_MIGRATE_UNKNOWN_FAILURE",
    62: "DISK_RESIZE",
    63: "DISK_RESIZE_POWEROFF",
    64: "DISK_RESIZE_UNDEPLOYED",
}


client = oca.Client(None, address=ADDRESS)
result = client.call('vmpool.info', -1, -1, -1, -1)
root = ET.fromstring(result)
nodes = []
for node in root.findall('./VM/ID/..'):
    if node.find('ID').text == sys.argv[1]:
        print('name:', node.find('NAME').text,
              'ip:', node.find('TEMPLATE/CONTEXT/ETH0_IP').text,
              'state:', (STATES[int(node.find('STATE').text)], LCM_STATES[int(node.find('LCM_STATE').text)]))
        break
