import subprocess

for i in range(3):
    subprocess.call("{ time /workspaces/Rusty-Kernels-Code/mandelbrot/C/mandelbrotC 16000 ; } 2>> /workspaces/Rusty-Kernels-Code/mandelbrot/C/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/mandelbrot/C/Results/massif{i}.txt\" /workspaces/Rusty-Kernels-Code/mandelbrot/C/mandelbrotC 16000", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call("{ time /workspaces/Rusty-Kernels-Code/mandelbrot/C++/mandelbrotC++ 16000 ; } 2>> /workspaces/Rusty-Kernels-Code/mandelbrot/C++/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/mandelbrot/C++/Results/massif{i}.txt\" /workspaces/Rusty-Kernels-Code/mandelbrot/C++/mandelbrotC++ 16000", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call("{ time /workspaces/Rusty-Kernels-Code/mandelbrot/Rust/target/release/Rust 16000 ; } 2>> /workspaces/Rusty-Kernels-Code/mandelbrot/Rust/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/mandelbrot/Rust/Results/massif{i}.txt\" /workspaces/Rusty-Kernels-Code/mandelbrot/Rust/target/release/Rust 16000", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)