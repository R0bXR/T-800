#!/usr/bin/python3

from marker import *

if __name__ == "__main__":
    args = get_args()

    if args.d:
        with daemon.DaemonContext():
            file_log_info("Start as a daemon")
            presence_marker(sys.argv[1], sys.argv[2])
            file_log_info("Goodbye from daemon")
            exit(SUCCESS)

    con_log_info("Start as an application")
    presence_marker(sys.argv[1], sys.argv[2])
    con_log_info("Goodbye from application")
    exit(SUCCESS)
