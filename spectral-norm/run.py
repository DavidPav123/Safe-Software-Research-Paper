import subprocess

for i in range(5):
    subprocess.call("time ((/workspaces/Rusty-Kernels-Code/spectral-norm/C/spectralnormC 5500) > /dev/null) 2>> /workspaces/Rusty-Kernels-Code/spectral-norm/C/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/spectral-norm/C/Results/massif{i}.txt\" --pages-as-heap=yes /workspaces/Rusty-Kernels-Code/spectral-norm/C/spectralnormC 5500 > /dev/null", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call("time ((/workspaces/Rusty-Kernels-Code/spectral-norm/C++/spectralnormC++ 5500) > /dev/null) 2>> /workspaces/Rusty-Kernels-Code/spectral-norm/C++/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/spectral-norm/C++/Results/massif{i}.txt\" --pages-as-heap=yes /workspaces/Rusty-Kernels-Code/spectral-norm/C++/spectralnormC++ 5500 > /dev/null", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call("time ((/workspaces/Rusty-Kernels-Code/spectral-norm/Rust/target/release/Rust 5500) > /dev/null) 2>> /workspaces/Rusty-Kernels-Code/spectral-norm/Rust/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/spectral-norm/Rust/Results/massif{i}.txt\" --pages-as-heap=yes /workspaces/Rusty-Kernels-Code/spectral-norm/Rust/target/release/Rust 5500 > /dev/null", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)



