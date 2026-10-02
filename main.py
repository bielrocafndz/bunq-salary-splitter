import signal
import sys
import time

# region functions
# ------------------------------------------------------------------------------
# Error handlers
# ------------------------------------------------------------------------------
def signal_handler(sig, frame):
    print("Exiting the program.")
    sys.exit(0)

# ------------------------------------------------------------------------------
#  Main functions
# ------------------------------------------------------------------------------ 
def main():
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        print("True")
        time.sleep(1)
#endregion

# ------------------------------------------------------------------------------
#  Main program
# ------------------------------------------------------------------------------ 
if __name__ == "__main__":
    main()