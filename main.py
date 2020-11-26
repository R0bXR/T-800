#!/usr/bin/python3

from marker import *

if __name__ == "__main__":
    args = get_args()

    if args.d:
        if "Linux" in platform.system():
            import daemon
            with daemon.DaemonContext():
                file_log_info("Start as a daemon")
                presence_marker(args.login, args.password)
                file_log_info("Goodbye from daemon")
                exit(SUCCESS)
        elif "Windows" in platform.system():
            con_log_warn("Feature not implemented. Running as app")

    con_log_info("Start as an application")
    presence_marker(args.login, args.password)
    con_log_info("Goodbye from application")
    exit(SUCCESS)
