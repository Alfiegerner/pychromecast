"""
Example that shows how to list chromecasts matching on name or uuid.
"""
import argparse
import logging
import sys
import time
from uuid import UUID

import pychromecast
import zeroconf

parser = argparse.ArgumentParser(description="Example on how to receive updates on discovered chromecasts.")
parser.add_argument("--show-debug", help="Enable debug log", action="store_true")
parser.add_argument("--show-zeroconf-debug", help="Enable zeroconf debug log", action="store_true")
parser.add_argument(
    "--cast", help='Name of wanted cast device")', default=None
)
parser.add_argument(
    "--uuid", help='UUID of wanted cast device', default=None
)
args = parser.parse_args()

if args.show_debug:
    logging.basicConfig(level=logging.DEBUG)
if args.show_zeroconf_debug:
    print("Zeroconf version: " + zeroconf.__version__)
    logging.getLogger("zeroconf").setLevel(logging.DEBUG)

if args.cast is None and args.uuid is None :
    print("Need to supply `cast` or `uuid`")
    sys.exit(1)

friendly_names = []
if args.cast:
    friendly_names.append(args.cast)

uuids = []
if args.uuid:
    uuids.append(UUID(args.uuid))

devices, browser = pychromecast.discovery.discover_listed_chromecasts(friendly_names=friendly_names, uuids=uuids)
#devices, browser = pychromecast.get_listed_chromecasts(friendly_names=friendly_names, uuids=uuids)
# Shut down discovery
pychromecast.stop_discovery(browser)

print(f"Discovered {len(devices)} device(s):")
for device in devices:
    print(f"  {device}")
    
