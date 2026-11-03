"""Validate a device inventory and print an offline connection plan."""

import argparse
import ipaddress
import json
from pathlib import Path


def connection_plan(inventory):
    if not isinstance(inventory, dict):
        raise ValueError("inventory must be an object")
    devices = inventory.get("devices")
    if not isinstance(devices, list) or not devices:
        raise ValueError("devices must be a nonempty list")
    names = set()
    plan = []
    for device in devices:
        if not isinstance(device, dict):
            raise ValueError("each device must be an object")
        name = device.get("name")
        if not isinstance(name, str) or not name.strip() or name in names:
            raise ValueError("device names must be nonempty and unique")
        names.add(name)
        address = device.get("address")
        if not isinstance(address, str):
            raise ValueError(f"{name}: address must be an IP address string")
        ipaddress.ip_address(address)
        platform = device.get("platform")
        if not isinstance(platform, str) or not platform.strip():
            raise ValueError(f"{name}: platform is required")
        port = device.get("port", 22)
        if type(port) is not int or not 1 <= port <= 65535:
            raise ValueError(f"{name}: port must be between 1 and 65535")
        plan.append(f"{name}: {address} port {port} ({platform})")
    return plan


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, required=True)
    args = parser.parse_args()
    try:
        plan = connection_plan(json.loads(args.inventory.read_text()))
    except (OSError, ValueError) as error:
        parser.exit(1, f"Inventory error: {error}\n")
    print("Offline connection plan (no device operations):")
    print("\n".join(plan))


if __name__ == "__main__":
    main()
