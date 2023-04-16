import concurrent.futures
import subprocess
import signal
import sys

scripts = ['blockchain/TsCoin.py', 'blockchain/tsCoin_5001.py', 'blockchain/tsCoin_5002.py', 'blockchain/tsCoin_5003.py']
futures = []

# Define a flag to stop the program gracefully
stop_flag = False

# Define a function to handle keyboard interrupts
def signal_handler(sig, frame):
    global stop_flag
    print('Keyboard interrupt detected. Stopping program gracefully...')
    stop_flag = True

# Register the signal handler for keyboard interrupts
signal.signal(signal.SIGINT, signal_handler)

# Function to run a script
def run_script(script):
    subprocess.run(['python', script])

# Use the concurrent.futures module to execute the functions in parallel
with concurrent.futures.ThreadPoolExecutor(max_workers=len(scripts)) as executor:
    for script in scripts:
        if stop_flag:
            break
        future = executor.submit(run_script, script)
        futures.append(future)

    for future in concurrent.futures.as_completed(futures):
        try:
            result = future.result()
        except Exception as e:
            print(f'Error occurred: {e}')
