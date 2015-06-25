import os

def save_match(match_id, match_data, folder='data'):
    save_to_file(folder, '%s.json' % match_id, match_data)

def save_to_file(path, filename, data):
    file_path = os.path.join(path, filename)
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))
    with open(file_path, "w") as f:
        f.write(data.encode('utf-8'))