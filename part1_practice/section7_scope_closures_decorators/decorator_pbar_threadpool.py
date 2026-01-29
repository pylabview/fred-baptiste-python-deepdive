# decorator_pbar_threadpool.py
import time
from concurrent.futures import ThreadPoolExecutor
from functools import wraps

from tqdm import tqdm


def looping_bar_while_running(
    *,
    desc="Working",
    unit="ticks",
    leave=True,
    ncols=None,
    tick_seconds=0.1,
    cycle_seconds=5.0,  # bar fills in this many seconds
    show_cycle_count=True,
    mininterval=0.1,
):
    """
    Show a looping tqdm progress bar while a function runs.

    - The bar fills over `cycle_seconds`.
    - If the function is still running, it resets and starts over.
    - Works with ANY function signature (no injected kwargs).

    This is not true % progress; it's a visual heartbeat.
    """
    if tick_seconds <= 0:
        raise ValueError("tick_seconds must be > 0")
    if cycle_seconds <= 0:
        raise ValueError("cycle_seconds must be > 0")
    if cycle_seconds < tick_seconds:
        raise ValueError("cycle_seconds must be >= tick_seconds")

    cycle_total = max(1, int(round(cycle_seconds / tick_seconds)))

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            with ThreadPoolExecutor(max_workers=1) as ex:
                future = ex.submit(fn, *args, **kwargs)

                cycles = 0
                with tqdm(
                    total=cycle_total,
                    desc=desc,
                    unit=unit,
                    leave=leave,
                    ncols=ncols,
                    mininterval=mininterval,
                    colour="green",
                ) as pbar:
                    while not future.done():
                        time.sleep(tick_seconds)
                        pbar.update(1)

                        # If bar filled and still running → reset and start over
                        if pbar.n >= cycle_total and not future.done():
                            cycles += 1
                            if show_cycle_count:
                                pbar.set_postfix_str(f"cycle={cycles}")
                            pbar.reset()

                return future.result()

        return wrapper

    return decorator
