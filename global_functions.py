def breakToLines(txt):
    with open(txt, 'rt', encoding='utf-8') as file:
        return_list = [line for line in file.read().splitlines()]
    return return_list

def currentTime():
    import time
    seconds = time.time()
    local_time = time.ctime(seconds)
    return local_time