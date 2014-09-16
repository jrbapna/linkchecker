# from __future__ import print_function
# from distutils.util import get_platform
import os, sys, json
# print("I will call this other program called hello.py")
# print(get_platform())


payload_file = None
payload = None
real_args = " ".join(map(str, sys.argv[1:]  ))


for i in range(len(sys.argv)):
    if sys.argv[i] == "-payload" and (i + 1) < len(sys.argv):
        payload_file = sys.argv[i + 1]
        with open(payload_file,'r') as f:
            payload = json.loads(f.read())
        break


os.system("cp -r build/scripts-2.7/* build/lib.linux-x86_64-2.7")
os.system("cp _LinkChecker_configdata.py build/lib.linux-x86_64-2.7")
os.system("python build/lib.linux-x86_64-2.7/linkchecker {}".format(real_args))