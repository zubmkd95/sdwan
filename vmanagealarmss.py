#!/usr/bin/env python3

from requests.exceptions import RequestException
from tabulate import tabulate

from vmanage import VMANAGE_HOST, USERNAME, PASSWORD, authenticate


def get_alarms(session):
    """Get the list of alarms from vManage."""
    url = f"{VMANAGE_HOST}/dataservice/alarms"

    try:
        response = session.get(url, verify=False)
        if response.status_code == 200:
            return response.json()["data"]

        print(f"Failed to get alarms. Status code: {response.status_code}")
        return None

    except RequestException as e:
        print(f"Error getting alarms: {str(e)}")
        return None


def main():
    print("\nConnecting to vManage...")
    session = authenticate(VMANAGE_HOST, USERNAME, PASSWORD)
    print("Successfully authenticated to vManage")

    print("\nRetrieving alarms...")
    alarms = get_alarms(session)

    if alarms is None:
        return

    if alarms:
        print("\nAlarms:")
        print(tabulate(alarms, headers="keys", tablefmt="grid"))
        print(f"\nTotal alarms found: {len(alarms)}")
    else:
        print("No alarms found.")


if __name__ == "__main__":
    main()