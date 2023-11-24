import subprocess

for i in range(5):
    subprocess.call("time (/workspaces/Rusty-Kernels-Code/n-body/C/nbodyC 50000000 > /dev/null) 2>> /workspaces/Rusty-Kernels-Code/n-body/C/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/n-body/C/Results/massif{i}.txt\" --pages-as-heap=yes /workspaces/Rusty-Kernels-Code/n-body/C/nbodyC 50000000 > /dev/null", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call("time (/workspaces/Rusty-Kernels-Code/n-body/C++/nbodyC++ 50000000 > /dev/null) 2>> /workspaces/Rusty-Kernels-Code/n-body/C++/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/n-body/C++/Results/massif{i}.txt\" --pages-as-heap=yes /workspaces/Rusty-Kernels-Code/n-body/C++/nbodyC++ 50000000 > /dev/null", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call("time (/workspaces/Rusty-Kernels-Code/n-body/Rust/target/release/Rust 50000000 > /dev/null) 2>> /workspaces/Rusty-Kernels-Code/n-body/Rust/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/n-body/Rust/Results/massif{i}.txt\" --pages-as-heap=yes /workspaces/Rusty-Kernels-Code/n-body/Rust/target/release/Rust 50000000 > /dev/null", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)
