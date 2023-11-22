import subprocess
import os

for i in range(3):
    subprocess.call("time (/workspaces/Rusty-Kernels-Code/read-write/C/read-writeC) 2>> /workspaces/Rusty-Kernels-Code/read-write/C/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/read-write/C/Results/massif{i}.txt\" --stacks=yes /workspaces/Rusty-Kernels-Code/read-write/C/read-writeC", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)
    
for i in range(3):
    subprocess.call("time (/workspaces/Rusty-Kernels-Code/read-write/C++/read-writeC++) 2>> /workspaces/Rusty-Kernels-Code/read-write/C++/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/read-write/C++/Results/massif{i}.txt\" --stacks=yes /workspaces/Rusty-Kernels-Code/read-write/C++/read-writeC++", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)
    
for i in range(3):
    subprocess.call("time (/workspaces/Rusty-Kernels-Code/read-write/Rust/target/release/Rust) 2>> /workspaces/Rusty-Kernels-Code/read-write/Rust/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/read-write/Rust/Results/massif{i}.txt\" --stacks=yes /workspaces/Rusty-Kernels-Code/read-write/Rust/target/release/Rust", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)
