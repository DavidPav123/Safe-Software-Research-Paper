import subprocess

for i in range(3):
    subprocess.call("{ time /workspaces/Rusty-Kernels-Code/fasta/C/fastaC 25000 ; } 2>> /workspaces/Rusty-Kernels-Code/fasta/C/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/fasta/C/Results/massif{i}.txt\" /workspaces/Rusty-Kernels-Code/fasta/C/fastaC 25000", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call("{ time /workspaces/Rusty-Kernels-Code/fasta/C++/fastaC++ 25000 ; } 2>> /workspaces/Rusty-Kernels-Code/fasta/C++/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/fasta/C++/Results/massif{i}.txt\" /workspaces/Rusty-Kernels-Code/fasta/C++/fastaC++ 25000", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call("{ time /workspaces/Rusty-Kernels-Code/fasta/Rust/target/release/Rust 25000 ; } 2>> /workspaces/Rusty-Kernels-Code/fasta/Rust/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/fasta/Rust/Results/massif{i}.txt\" /workspaces/Rusty-Kernels-Code/fasta/Rust/target/release/Rust 25000", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)