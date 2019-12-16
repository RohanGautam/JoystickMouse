import asyncio, time, threading

def doSomething(abc):
    print(f"operation beginning: {abc}")
    time.sleep(2)
    print("complex operation that takes time")


def controller():
    count =0
    while count<20:
        thread = threading.Thread(target=doSomething, args=("beans",)) # a tuple of arguments
        thread.start()
        print("we out here")
        count+=1
        

controller()