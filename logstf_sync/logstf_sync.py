import PyLogsTF
import save_to_disk

def run(last_file_path):
    last_match_saved = get_last_match_saved(last_file_path)
    latest_match = PyLogsTF.latest_match()
    save_new_matches(last_match_saved, latest_match, save_to_disk.save_match)
    set_last_match_saved(last_file_path, latest_match)

def save_one_match(match_id):
    try:
        save_to_disk.save_match(match_id, PyLogsTF.get(match_id))
    except:
        pass

def save_one_match_parallel_wrapper(match_id):
    if match_id % 100 == 0:
        print match_id
    save_one_match(match_id)

def parallel_save(lower, upper):
    import multiprocessing as mp
    pool = mp.Pool(processes=mp.cpu_count())
    match_ids = range(lower+1, upper+1)
    pool.map(save_one_match_parallel_wrapper, match_ids)

def save_all_matches():
    latest_match = PyLogsTF.latest_match()
    parallel_save(0, latest_match)
    set_last_match_saved(last_file_path, latest_match)

def get_last_match_saved(file_path):
    try:
        with open(file_path, 'r') as f:
            return int(f.read())
    except:
        return 0

def set_last_match_saved(file_path, last):
    with open(file_path, 'w') as f:
        f.write(str(last))

def save_new_matches(lower, upper, save_result):
    for i in range(lower+1, upper+1):
        save_one_match(i, save_result)