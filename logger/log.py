from datetime import datetime

logList = []


def getGreeting():
    time = int(datetime.now().strftime("%H"))
    if time >= 5 and time < 9:
        ret = "Good morning!"

    elif time >= 9 and time < 17:
        ret = "Good day!"

    elif time >= 17 and time < 23:
        ret = "Good evening!"

    elif time >= 23 or time < 5:
        ret = "Good night!"

    else:
        ret = "Time is: " + "'" + str(time) + "'"
            
    return ret


def log(message: str, level=0):
    dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    match level:
        case -1:
            tier = ""
        case 0:
            tier = "[INFO]"
        case 1:
            tier = "[WARNING]"
        case 2:
            tier = "[ERROR]"

        case _:
            tier = "[THIS_SHOULD_NOT_HAPPEN]"

    msg = tier + " " + dt + ": \t\t" + message + "\n"
    with open("log.txt", "a") as logfile:
        logfile.write(msg)
    
    logList.append(msg)
    print(msg, end='')

if __name__ == "log":    
    log(getGreeting(), -1)

