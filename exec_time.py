import time

def execution_time(func):
    def wrapper():
        print('Setting start time...')
        start_time = time.time()
        func()
        print('Setting end time...')
        print('Time elapsed:', time.time() - start_time)
    return wrapper