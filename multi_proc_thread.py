from multiprocessing import Pool
import time
import thread
import Queue

result_queue = Queue.Queue(maxsize=5)


def process_thread(result_queue, z):
    for i in range(10):
        print("I am thread {}".format(z))
        time.sleep(1)

    return_map = {"rcode": z}
    result_queue.put(return_map)


def multi_thread(y):
    print("I am process {}".format(y))
    result_list = []
    parallel_list = [y * i for i in range(10, 110, 10)]
    for pnode in parallel_list:
        thread.start_new_thread(process_thread, (result_queue, pnode))

    while True:
        if result_queue.full():
            break

    while not result_queue.empty():
        result_list.append(result_queue.get())


def process_request(x):
    for i in range(10):
        print(x, " * ", i, " = ", x * i)
        time.sleep(1)


def multi_process():
    p = Pool(4)
    multiple_results = list()
    for node_data in range(10):
        # process_request(node_data)
        print("Starting process {}".format(node_data))
        # import pdb;pdb.set_trace()
        multiple_results.append(p.apply_async(multi_thread, (node_data,)))

    for res in multiple_results:
        res.get()

    p.close()
    p.join()


if __name__ == "__main__":
    multi_process()
    # multi_thread(1)
