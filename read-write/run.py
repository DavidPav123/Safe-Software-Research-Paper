import subprocess

for i in range(5):
    subprocess.call("time (/workspaces/Rusty-Kernels-Code/read-write/C/read-writeC) 2>> /workspaces/Rusty-Kernels-Code/read-write/C/Results/One-Billion/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/read-write/C/Results/One-Billion/massif{i}.txt\" --pages-as-heap=yes /workspaces/Rusty-Kernels-Code/read-write/C/read-writeC", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)
    
for i in range(5):
    subprocess.call("time (/workspaces/Rusty-Kernels-Code/read-write/C++/read-writeC++) 2>> /workspaces/Rusty-Kernels-Code/read-write/C++/Results/One-Billion/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/read-write/C++/Results/One-Billion/massif{i}.txt\" --pages-as-heap=yes /workspaces/Rusty-Kernels-Code/read-write/C++/read-writeC++", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)
    
for i in range(5):
    subprocess.call("time (/workspaces/Rusty-Kernels-Code/read-write/Rust/target/release/Rust) 2>> /workspaces/Rusty-Kernels-Code/read-write/Rust/Results/One-Billion/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/read-write/Rust/Results/One-Billion/massif{i}.txt\" --pages-as-heap=yes /workspaces/Rusty-Kernels-Code/read-write/Rust/target/release/Rust", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)
