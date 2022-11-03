from multiprocessing import Pool
from multiprocessing import Process
from threading import Thread
from functions import partial
import searchController as sc

def multi_search(keyword, file_list):
    """
    # thread로 동작
    try:
        th1 = Thread(target=sc.get_file_text, args=(keyword, file_name)
        th2 = Thread(target=work, args=(2, END//2, END, result))
        thd_list = []
        for file_name in file_list :
            proc_list.append(Process(target=sc.get_file_text, args =(keyword, file_name)))
            t = Thread(target=sc.get_file_text, args=(keyword, file_name))
            t.start()
            thd_list.append(t)
        for t in thd_list:
            t.join()
    except KeyboardInterrupt:
        print("KeyboardInterrupt sys.exit")
        sys.exit(0)
        print("KeyboardInterrupt os.exit")
        os._exit(os.EX_OK)
        print("KeyboardInterrupt quit")
        quit()
        print("KeyboardInterrupt exit")         
        exit()
    """

    # process 로 동작
    try:
        pool = Pool(processes=len(file_list))
        func = partial(sc.get_file_text, keyword)
        var = pool.map(func, file_list)
        pool.close()
        pool.join()
    except KeyboardInterrupt:
        print("KeyboardInterrupt sys.exit")
        sys.exit(0)
        print("KeyboardInterrupt os.exit")
        os._exit(os.EX_OK)
        print("KeyboardInterrupt quit")
        quit()
        print("KeyboardInterrupt exit")         
        exit()