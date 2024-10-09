import signal

def handler(signum, frame):
  print(f"Catched signal {signum} - {signal.Signals(signum).name}")

  if signum == signla.SIGTERM:
    print(f"Raise KeyboardInterrupt as received {signal.Signals(signum).name}")

    raise KeyboardInterrupt('Received SIGTERM')

def init():
  signal.signal(signal.SIGTERM, handler)
