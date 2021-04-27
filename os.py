#created by saurabh

cmd="welcome to SAURABH THUNDER-OS"
print(cmd)
x=print("="*50)
started=False
print(f'''
    Version 1.0
    Enter the command and check the results
    This is a Beta version
        
{"="*50}''')
while cmd.lower() != "quit":
    cmd=input(">").lower()
    if cmd == "help":
        print('''"Start" to start the car
"Stop" to stop the car
"Quit" to exit''')
    elif cmd == "start":
        if started:
            print("car is already on")
        else:
            started = True
            print("Started engine ========>>>>>>>")
    elif cmd == "stop":
        if not started:
            print("car is already stopped")
        else:
            started = False
            print("Engine Stopped wooooooooosh")
    elif cmd == "quit":
        print('''GoodBye!!!
have a Great Day :)''')
        break
    elif cmd=="":
        continue
    else:
        print('''I cannot understand that use "help" key''')

