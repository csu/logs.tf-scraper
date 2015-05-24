# import PyLogsTF
# PyLogsTF.get(828613)
# PyLogsTF.latest_match()

import logstf_sync
# print logstf_sync.get_last_match_saved('last.txt')
# logstf_sync.set_last_match_saved('last.txt', 100)
# logstf_sync.save_to_disk.save_to_file('results', 'test.txt', 'hello world')
# logstf_sync.run('last')
logstf_sync.save_all_matches('last')