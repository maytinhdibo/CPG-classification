import subprocess
import os

joern_path = "./joern/cli/"

#joern-parse
subprocess.run([joern_path + "joern-parse", "./input/a.c", "--out",  "./output/cpg.bin"],
                                      stdout=subprocess.PIPE, text=True, check=True)

#open-joern
joern_process = subprocess.Popen(joern_path + "joern", stdin=subprocess.PIPE)

import_cpg_cmd = f"importCpg(\"{os.path.abspath("./output/cpg.bin")}\")\r".encode()
script_path = os.path.abspath("./joern/script/graph-for-funcs.sc")
run_script_cmd = f"cpg.runScript(\"{script_path}\").toString() |> \"{os.path.abspath("./output/cpg.json")}\"\r".encode()

joern_process.stdin.write(import_cpg_cmd)
joern_process.stdin.write(run_script_cmd)
joern_process.stdin.write("delete\r".encode())
joern_process.communicate(timeout=60)

# print(import_cpg_cmd)