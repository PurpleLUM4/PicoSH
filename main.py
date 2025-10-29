import os
import sys
import time

def picosh(command : str) -> None:
    if command.strip() == "":
        return
    
    if command == "ls":
        dirs = []
        files = []
        
        for file in os.listdir(command.split("ls")[1]):
            stat = os.stat(file)
            timestamp = stat[8]
            
            if (os.stat(file)[0] & 0x4000) == 0x4000:
                dirs.append([file, time.localtime(timestamp)])
            else:
                files.append([file, time.localtime(timestamp)])
                
        for dir in dirs:
            t = dir[1]
            print(f"Last modified {t[2]:02d}.{t[1]:02d}.{t[0]} {t[3]:02d}:{t[4]:02d}:{t[5]:02d} " + dir[0] + "/")
        
        for file in files:
            t = file[1]
            print(f"Last modified {t[2]:02d}.{t[1]:02d}.{t[0]} {t[3]:02d}:{t[4]:02d}:{t[5]:02d} " + file[0])
            
        print()
        return
    
    elif command.strip().startswith("cd "):
        cd_to = command.split("cd ")[1]
        
        try:
            os.chdir(cd_to)
        except OSError:
            try:
                os.chdir(cd_to.strip())
            except OSError:
                print("cd: " + cd_to + ": No such path.\n")
    
    elif command.strip().startswith(sys.implementation.name + " "):
        file = command.split(sys.implementation.name + " ")[1]
        try:
            fp = open(file, "r")
            
            try:
                exec(fp.read())
            except Exception as error:
                print(str(error) + "\n")
                
            fp.close()
        except OSError:
            print(sys.implementation.name + ": " + file + ": No such file.\n")
    
    elif command.strip().startswith("rm "):
        file = command.strip()[3:]
        
        try:
            os.remove(file)
        except OSError:
            print("rm: " + file + ": No such file.\n")
            
        

    elif command.strip().startswith("mv ") or command.strip().startswith("cp "):
        move_from = command.strip()[3:].split(" ")[0]
        move_to = commandstrip()[3:].split(" ")[1]
        
        with open(move_from, "r") as from_fp:
            data = from_fp.read()
            from_fp.close()
            
        with open(move_to, "w") as to_fp:
            to_fp.write(data)
            to_fp.close()
            
        if command.strip().startswith("mv "):
            os.remove(move_from)
        
    
    elif command.strip().startswith("python ") or command.strip().startswith("python2 ") or command.strip().startswith("python3 "):
        print("No such command '" + command + "', did you mean " + sys.implementation.name + "?")
    
    elif command.strip().startswith("cat "):
        file = command.split("cat ")[1]
        
        try:
            fp = open(file, "r")
            for line in fp.read().split("\n"):
                print(line)
            fp.close()
        except OSError:
            print("cat: " + file + ": No such file.\n")
        
            
    elif command.strip() == "exit" or command.strip() == "quit":
        return 1337

print(r"""
      ____  _           _____ __  __
     / __ \(_)________ / ___// / / /
    / /_/ / / ___/ __ \\__ \/ /_/ / 
   / ____/ / /__/ /_/ /__/ / __  /  
  /_/   /_/\___/\____/____/_/ /_/                                   
""")

try:
    fp = open(".PicoSH", "r")
    
    for cfg_line in fp.read().split("\n"):
        if cfg_line.startswith("export "):
            if cfg_line.startswith("export SHELL="):
                shell_prompt = cfg_line[14:][:-1]
        else:
            picosh(cfg_line)
        
    fp.close()
except OSError:
    fp = open(".PicoSH", "w")
    fp.write("export SHELL=\"PicoSH@[{PATH}]:~$ \"\n")
    fp.close()
    
    shell_prompt = "PicoSH@[{PATH}]:~$ "
    

while True:
    cmd = input(shell_prompt.replace("{PATH}", os.getcwd()))
    if ";" in cmd:
        cmds = cmd.split(";")
        
        exit = False
        for cmd in cmds:
            if picosh(cmd) == 1337:
                exit = True
            
        if exit:
            break
            
    else:
        if picosh(cmd) == 1337:
            break
