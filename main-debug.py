import sys

from httprunner.cli import main

cmd = sys.argv.pop(1)

if cmd in ["hrp", "httprunner", "ate"]:
    main()

