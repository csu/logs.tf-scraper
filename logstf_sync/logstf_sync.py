import PyLogsTF
import save_to_disk

def run(last_file_path):
    last_match_saved = get_last_match_saved(last_file_path)
    latest_match = PyLogsTF.latest_match()
    save_new_matches(0, 3, save_to_disk.save_match)

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
        try:
            save_result(i, PyLogsTF.get(i))
        except:
            pass