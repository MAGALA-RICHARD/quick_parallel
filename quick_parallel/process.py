from concurrent.futures import ProcessPoolExecutor, as_completed, ThreadPoolExecutor
from multiprocessing import cpu_count

from tqdm import tqdm

CPU_CORES = int(int(cpu_count()) * 0.5)


def select_type(use_thread, n_cores):
    return ThreadPoolExecutor(n_cores) if use_thread else ProcessPoolExecutor(n_cores)


def quick_parallel(func, iterable, *args, **kwargs):
    """
    Run a function in parallel using threads or processes.

    *Args:
        func (callable): The function to run in parallel.

        iterable (iterable): An iterable of items that will be processed by the function.

        *args: Additional arguments to pass to the `func` function.

    Yields:
        Any: The results of the `func` function for each item in the iterable.
    :pram Args: any extra positional argument accepted by the function. please note their corresponding positions
     Keyword Args for the fucntion can also be entered after the positional argument if any
   **kwargs
    use_thread (bool, optional): If True, use threads for parallel execution; if False, use processes. Default is False.
     implying it will use parallel processing

     n_workers (int, optional): The number of threads or processes to use for parallel execution. Default is 50% of cpu
       cores on the machine.

     verbose (bool): if progress should be printed on the screen, default is True
     progress_message (str) sentence to display progress such processing please wait defaults to processing multiple jobs via {nameof the function} please wait
    @returns
     a generator
     The progress bar will be displayed on the screen as soon you start unzipping the returned generator
    """

    use_thread, cpu_cores = kwargs.get('use_thread', False), kwargs.get('n_workers', CPU_CORES)
    progress_message = kwargs.get('progress_message', f"Processing multiple jobs via '{func.__name__}' please wait!")

    selection = select_type(use_thread=use_thread,
                            n_cores=cpu_cores)
    bar_format = f"{progress_message}{{l_bar}}{{bar}}| jobs completed: {{n_fmt}}/{{total_fmt}}| Elapsed time: {{elapsed}}"
    with selection as pool:
        futures = [pool.submit(func, i, *args) for i in iterable]

        # progress = tqdm(total=len(futures), position=0, leave=True,
        #                 bar_format=f'{progress_message} {|{bar}|}:' '{percentage:3.0f}% completed')
        progress = tqdm(
            total=len(futures),
            position=0,
            leave=True,
            bar_format=bar_format
            # '{l_bar}{bar}| {percentage:3.0f}% completed | Elapsed time: {elapsed} | {remaining} remaining',
        )

        # Iterate over the futures as they complete
        for future in as_completed(futures):
            yield future.result()
            progress.update(1)
        progress.close()


# _______________________________________________________________


def fibonacci_executor(n):
    # Initialize the first two Fibonacci numbers
    fib_sequence = [0, 1]

    # Generate the Fibonacci sequence up to the nth term
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    return fib_sequence


def worker(x):
    return x ** 3 * 2


def sample_func(x):
    return x * 2


def sample_func_w_args(x, p):
    return x ** p


if __name__ == '__main__':
    lp = [(-92.70166631, 42.26139442), (-92.69581474, 42.26436962), (-92.64634469, 42.33703225)]
    gen_d = (i for i in range(1000))
    wk = quick_parallel(worker, gen_d, use_thread=True, ncores=4)

    # with custom message
    lm = quick_parallel(fibonacci_executor, gen_d, use_thread=False, n_workers=2,
                        progress_message="running function: ")
    # simple example

    ap = [i for i in lm]
