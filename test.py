import time
import sys
import signal_handler

def main(opts):
    while True:
        print("Do some task...")
        time.sleep(2)
        pass

if __name__ == "__main__":
    print("Starting ...")
    signal_handler.init()

    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        print("Exit program as received signal")
        sys.exit(0)
    finally:
        print("Exit program with error")
        sys.exit(2)
