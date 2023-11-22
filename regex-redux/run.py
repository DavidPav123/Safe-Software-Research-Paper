import subprocess

for i in range(3):
    subprocess.call("time ((/workspaces/Rusty-Kernels-Code/regex-redux/C/regexreduxC < /workspaces/Rusty-Kernels-Code/regex-redux/input.txt) > /dev/null) 2>> /workspaces/Rusty-Kernels-Code/regex-redux/C/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/regex-redux/C/Results/massif{i}.txt\" /workspaces/Rusty-Kernels-Code/regex-redux/C/regexreduxC < /workspaces/Rusty-Kernels-Code/regex-redux/input.txt > /dev/null", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call("time ((/workspaces/Rusty-Kernels-Code/regex-redux/C++/regexreduxC++ < /workspaces/Rusty-Kernels-Code/regex-redux/input.txt) > /dev/null) 2>> /workspaces/Rusty-Kernels-Code/regex-redux/C++/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/regex-redux/C++/Results/massif{i}.txt\" /workspaces/Rusty-Kernels-Code/regex-redux/C++/regexreduxC++ < /workspaces/Rusty-Kernels-Code/regex-redux/input.txt > /dev/null", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call("time ((/workspaces/Rusty-Kernels-Code/regex-redux/Rust/target/release/Rust < /workspaces/Rusty-Kernels-Code/regex-redux/input.txt) > /dev/null) 2>> /workspaces/Rusty-Kernels-Code/regex-redux/Rust/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/regex-redux/Rust/Results/massif{i}.txt\" /workspaces/Rusty-Kernels-Code/regex-redux/Rust/target/release/Rust < /workspaces/Rusty-Kernels-Code/regex-redux/input.txt > /dev/null", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)



