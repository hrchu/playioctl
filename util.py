# -*- coding: utf-8 -*-
import subprocess
import time


def run(cmd):
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    # print(result.returncode, result.stdout, result.stderr)


def prepare():
    # run(['mtx', '-f', '/dev/sg14', 'load', '1', '0'])
    run(['mt', '-f', '/dev/nst0', 'eod'])
    time.sleep(1)


def demo(device=None, implement=None):
    print("Demo tape rewind/status operation powered by " + str(implement))
    prepare()
    print("AS-IS: ")
    print(implement.status(device))
    implement.rewind(device)
    time.sleep(1)
    print("TO-BE: ")
    print(implement.status(device))
