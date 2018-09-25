# -*- coding: utf-8 -*-
import subprocess
import time

import mt


def run(cmd):
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    print(result.returncode, result.stdout, result.stderr)


# run(['mtx', '-f', '/dev/sg14', 'load', '1', '0'])
run(['mt', '-f', '/dev/nst0', 'eod'])
time.sleep(1)
print("AS-IS: ")
print(mt.status('/dev/nst0'))
mt.rewind('/dev/nst0')
time.sleep(1)
print("TO-BE: ")
print(mt.status('/dev/nst0'))
