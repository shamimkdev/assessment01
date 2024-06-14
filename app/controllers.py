from multiprocessing import Pool
from datetime import datetime
from .utils import log_info, log_error

def add_lists(lists):
    try:
        with Pool() as pool:
            result = pool.map(sum, lists)
        return result
    except Exception as e:
        log_error(f"Error in add_lists: {str(e)}")
        raise
