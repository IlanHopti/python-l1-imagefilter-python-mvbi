from _datetime import datetime

log_file = "pythonImageFilter.log"


def log(msg):
    """
    log message to file
    :param msg: The message to log
    """
    now = datetime.now()
    timestamp = now.strftime('%Y/%m/%d %H,%M,%S')
    formatted = f'{timestamp} - {msg}'
    print(formatted)
    with open(log_file, "a") as f:
        f.write(formatted + "\n")


def dump_log():
    """
    Dump the log file to the console
    """
    try:
        with open(log_file, 'r') as f: # open the log file
            print(f.read())
    except FileNotFoundError as e: # if file not found print error
        print(f"fichier cannot open {log_file}. error={e}")
        log(f"fichier cannot open {log_file}. error={e}")
