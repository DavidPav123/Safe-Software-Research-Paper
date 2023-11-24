import subprocess

for i in range(5):
    subprocess.call("time (/workspaces/Rusty-Kernels-Code/fasta/C/fastaC 25000000 > /dev/null) 2>> /workspaces/Rusty-Kernels-Code/fasta/C/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/fasta/C/Results/massif{i}.txt\" --pages-as-heap=yes /workspaces/Rusty-Kernels-Code/fasta/C/fastaC 250000 > /dev/null", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call("time (/workspaces/Rusty-Kernels-Code/fasta/C++/fastaC++ 25000000 > /dev/null) 2>> /workspaces/Rusty-Kernels-Code/fasta/C++/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/fasta/C++/Results/massif{i}.txt\" --pages-as-heap=yes /workspaces/Rusty-Kernels-Code/fasta/C++/fastaC++ 250000 > /dev/null", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call("time (/workspaces/Rusty-Kernels-Code/fasta/Rust/target/release/Rust 25000000 > /dev/null) 2>> /workspaces/Rusty-Kernels-Code/fasta/Rust/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/fasta/Rust/Results/massif{i}.txt\" --pages-as-heap=yes /workspaces/Rusty-Kernels-Code/fasta/Rust/target/release/Rust 250000 > /dev/null", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)