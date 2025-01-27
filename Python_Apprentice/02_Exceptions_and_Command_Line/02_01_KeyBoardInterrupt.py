import time

try:
    time.sleep(111)
except KeyboardInterrupt:
    print("KeyBoardInterrupt has occurred!")