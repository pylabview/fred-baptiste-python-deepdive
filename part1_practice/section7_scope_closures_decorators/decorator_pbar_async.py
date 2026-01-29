# pbar_async.py
import asyncio
from functools import wraps

from tqdm import tqdm


def looping_bar_while_running(
    *,
    desc="Working",
    unit="ticks",
    leave=True,
    ncols=None,
    tick_seconds=0.1,
    cycle_seconds=5,
    show_cycle_count=True,
    mininterval=0.1,
):
    """
    Shows a looping tqdm progress bar while a function (fn) runs

    - The bar fills over 'cycle_seconds'
    - If the function still running, it resets and start over
    - Works with any function signature (no inject kwargs)

    Notes:
    - If fn is async: runs fully in asyncio (no threads)
    - If fn is sync/blocking: runs thru asyncio.to_thread() under the hood.

    """

    if tick_seconds <= 0:
        raise ValueError("tick_seconds must be > 0")
    if cycle_seconds <= 0:
        raise ValueError("cycle_seconds must be > 0")
    if cycle_seconds < tick_seconds:
        raise ValueError("cycle_seconds must be >= tick_seconds")

    cycle_total = max(1, int(round(cycle_seconds / tick_seconds)))

    async def _run_with_bar(task: "asyncio.Task"):
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
            while not task.done():
                await asyncio.sleep(tick_seconds)
                pbar.update(1)

                # if the bar is filled and still running -> reset and start over
                if pbar.n >= cycle_total and not task.done():
                    cycles += 1
                    if show_cycle_count:
                        pbar.set_postfix_str(f"cycles={cycles}")
                    pbar.reset()
        return await task

    def decorator(fn):
        is_coro = asyncio.iscoroutinefunction(fn)

        if is_coro:

            @wraps(fn)
            async def async_wrapper(*args, **kwargs):
                task = asyncio.create_task(fn(*args, **kwargs))
                try:
                    return await _run_with_bar(task)
                except asyncio.CancelledError:
                    task.cancel()
                    raise

            return async_wrapper

        @wraps(fn)
        def sync_wrapper(*args, **kwargs):
            async def runner():
                task = asyncio.create_task(asyncio.to_thread(fn, *args, **kwargs))
                try:
                    return await _run_with_bar(task)
                except asyncio.CancelledError:
                    task.cancel()
                    raise

            try:
                asyncio.get_running_loop()
            except RuntimeError:
                return asyncio.run(runner())
            raise RuntimeError("This fn is synchronous but it's called from a running event loop")

        return sync_wrapper

    return decorator
