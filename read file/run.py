import subprocess
import os

for i in range(3):
    subprocess.call("{ time /workspaces/Rusty-Kernels-Code/read\ file/C/read_fileC ; } 2>> /workspaces/Rusty-Kernels-Code/read\ file/C/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)
    os.remove("/workspaces/Rusty-Kernels-Code/read file/destination.txt")

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/read file/C/Results/massif{i}.txt\" /workspaces/Rusty-Kernels-Code/read\ file/C/read_fileC", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)
    os.remove("/workspaces/Rusty-Kernels-Code/read file/destination.txt")
    
for i in range(3):
    subprocess.call("{ time /workspaces/Rusty-Kernels-Code/read\ file/C++/read_fileC++ ; } 2>> /workspaces/Rusty-Kernels-Code/read\ file/C++/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)
    os.remove("/workspaces/Rusty-Kernels-Code/read file/destination.txt")

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/read file/C++/Results/massif{i}.txt\" /workspaces/Rusty-Kernels-Code/read\ file/C++/read_fileC++", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)
    os.remove("/workspaces/Rusty-Kernels-Code/read file/destination.txt")
    
for i in range(3):
    subprocess.call("{ time /workspaces/Rusty-Kernels-Code/read\ file/Rust/target/debug/Rust ; } 2>> /workspaces/Rusty-Kernels-Code/read\ file/Rust/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)
    os.remove("/workspaces/Rusty-Kernels-Code/read file/destination.txt")

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/read file/Rust/Results/massif{i}.txt\" /workspaces/Rusty-Kernels-Code/read\ file/Rust/target/debug/Rust", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)
    os.remove("/workspaces/Rusty-Kernels-Code/read file/destination.txt")
