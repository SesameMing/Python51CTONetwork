# Author:Alex Li
import contextlib


@contextlib.contextmanager
def worker_state(state_list, worker_thread):
	"""
	用于记录线程中正在等待的线程数
	"""
	state_list.append(worker_thread)
	try:
		yield
	finally:
		state_list.remove(worker_thread)

free_list = []
current_thread = "alex"
with worker_state(free_list, current_thread):
	print(123)
	print(456)

