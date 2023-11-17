import subprocess

for i in range(3):
    subprocess.call("{ time /workspaces/Rusty-Kernels-Code/reverse-complement/C/revcompC < /workspaces/Rusty-Kernels-Code/reverse-complement/input.txt ; } 2>> /workspaces/Rusty-Kernels-Code/reverse-complement/C/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/reverse-complement/C/Results/massif{i}.txt\" /workspaces/Rusty-Kernels-Code/reverse-complement/C/revcompC < /workspaces/Rusty-Kernels-Code/reverse-complement/input.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call("{ time /workspaces/Rusty-Kernels-Code/reverse-complement/C++/revcompC++ < /workspaces/Rusty-Kernels-Code/reverse-complement/input.txt ; } 2>> /workspaces/Rusty-Kernels-Code/reverse-complement/C++/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/reverse-complement/C++/Results/massif{i}.txt\" /workspaces/Rusty-Kernels-Code/reverse-complement/C++/revcompC++ < /workspaces/Rusty-Kernels-Code/reverse-complement/input.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call("{ time /workspaces/Rusty-Kernels-Code/reverse-complement/Rust/target/release/Rust < /workspaces/Rusty-Kernels-Code/reverse-complement/input.txt ; } 2>> /workspaces/Rusty-Kernels-Code/reverse-complement/Rust/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/reverse-complement/Rust/Results/massif{i}.txt\" /workspaces/Rusty-Kernels-Code/reverse-complement/Rust/target/release/Rust < /workspaces/Rusty-Kernels-Code/reverse-complement/input.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)




