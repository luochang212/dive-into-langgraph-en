# -*- coding: utf-8 -*-

"""
Get device information
"""

import time
import datetime
import getpass
import platform


def _safe_get(func):
    try:
        return func()
    except Exception:
        return "Unknown"


dev_info = {
    "Current Time (now)": _safe_get(lambda: datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
    "Timezone (timezone)": _safe_get(lambda: time.tzname[0]),
    "Operating System (platform)": _safe_get(platform.system),
    "Username (username)": _safe_get(getpass.getuser),
    "UTC Time (utc_now)": _safe_get(lambda: datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")),
    "System Version (platform_release)": _safe_get(platform.release),
    "System Detailed Version (platform_version)": _safe_get(platform.version),
    "Architecture (architecture)": _safe_get(lambda: " ".join(list(platform.architecture()))),
    "Machine Type (machine)": _safe_get(platform.machine),
    "Processor (processor)": _safe_get(platform.processor),
}


def get_info(key):
    return dev_info[key]


if __name__ == "__main__":
    res = get_info("Current Time (now)")
    print(res)
