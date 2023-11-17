import subprocess

for i in range(3):
    subprocess.call("{ time /workspaces/Rusty-Kernels-Code/spectral-norm/C/spectralnormC 5500 ; } 2>> /workspaces/Rusty-Kernels-Code/spectral-norm/C/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/spectral-norm/C/Results/massif{i}.txt\" /workspaces/Rusty-Kernels-Code/spectral-norm/C/spectralnormC 5500", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call("{ time /workspaces/Rusty-Kernels-Code/spectral-norm/C++/spectralnormC++ 5500 ; } 2>> /workspaces/Rusty-Kernels-Code/spectral-norm/C++/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/spectral-norm/C++/Results/massif{i}.txt\" /workspaces/Rusty-Kernels-Code/spectral-norm/C++/spectralnormC++ 5500", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call("{ time /workspaces/Rusty-Kernels-Code/spectral-norm/Rust/target/release/Rust 5500 ; } 2>> /workspaces/Rusty-Kernels-Code/spectral-norm/Rust/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/spectral-norm/Rust/Results/massif{i}.txt\" /workspaces/Rusty-Kernels-Code/spectral-norm/Rust/target/release/Rust 5500", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)



