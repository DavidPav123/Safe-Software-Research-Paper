import subprocess

for i in range(3):
    subprocess.call("time (/workspaces/Rusty-Kernels-Code/fannkuch-redux/C/fannkuchreduxC 12 > /dev/null) 2>> /workspaces/Rusty-Kernels-Code/fannkuch-redux/C/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/fannkuch-redux/C/Results/massif{i}.txt\" --stacks=yes /workspaces/Rusty-Kernels-Code/fannkuch-redux/C/fannkuchreduxC 12", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)
    
for i in range(3):
    subprocess.call("time (/workspaces/Rusty-Kernels-Code/fannkuch-redux/C++/fannkuchreduxC++ 12 > /dev/null) 2>> /workspaces/Rusty-Kernels-Code/fannkuch-redux/C++/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/fannkuch-redux/C++/Results/massif{i}.txt\" --stacks=yes /workspaces/Rusty-Kernels-Code/fannkuch-redux/C++/fannkuchreduxC++ 12", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)
    
for i in range(3):
    subprocess.call("time (/workspaces/Rusty-Kernels-Code/fannkuch-redux/Rust/target/release/fannkuch-redux 12 > /dev/null) 2>> /workspaces/Rusty-Kernels-Code/fannkuch-redux/Rust/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/fannkuch-redux/Rust/Results/massif{i}.txt\" --stacks=yes /workspaces/Rusty-Kernels-Code/fannkuch-redux/Rust/target/release/fannkuch-redux 12", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)
    