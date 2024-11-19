quick_parallel
==============

This library is used to run custom functions using threads or process pool executor.

Requirements
************

- `tqdm` (this will be installed automatically if missing)
- Python 3.4 or higher

Installation
************

Install using pip:

.. code:: shell

    pip install quick_parallel

Main Methods
************

`quick_parallel`: A function that splits multiple processes by either running them in parallel processes or using threads.

Usage
*****

.. code:: python

    from quick_parallel.process import quick_parallel

    def worker(x):
        """
        Function to compute x^3 * 2.
        """
        return x ** 3 * 2

    def worker_with_arguments(x, p):
        """
        Function that raises a number `x` to the power of `p`.

        :param x: Base number
        :param p: Power to which `x` is raised
        :return: Result of x raised to the power of p
        """
        return x ** p

    if __name__ == "__main__":
        # Example: Simple worker without arguments
        gen_d = range(5)  # Replace with your actual generator or iterable

        # Running in a parallel process with 2 workers and disabling threading
        lm = quick_parallel(worker, gen_d, use_thread=False, n_workers=2,
                            progress_message="Running in simple worker:")

        # Collect and print the results
        res = [i for i in lm]
        print(res)
        # Output: [0, 2, 16, 54, 128]

        # Example: Worker with an extra positional argument
        arg = 9  # Example positional argument (power)
        ext_arg = quick_parallel(worker_with_arguments, gen_d, arg, use_thread=False, n_workers=2,
                                 progress_message="Running worker_with_arguments function:")
        print(list(ext_arg))
        # Output: [0, 1, 512, 19683, 262144]

        # Change the argument and check the updated results
        arg = 10  # Example positional argument (power)
        ext_arg = quick_parallel(worker_with_arguments, gen_d, arg, use_thread=False, n_workers=2,
                                 progress_message="Running worker_with_arguments function:")
        print(list(ext_arg))
        # Output: [0, 1, 1024, 59049, 1048576]

Notes
*****

- When using threads (`use_threads=True`), the function utilizes `ThreadPoolExecutor` for parallel processing.
- If `n_workers` is not specified, the function defaults to using 40% of available CPU cores.
- Progress information is displayed during execution.
- Always run the code under `if __name__ == '__main__':` to prevent multiprocessing issues.
- Define worker functions in a separate script and import them into the processing script for better modularity.
- Pass a generator as the iterator (instead of a list, tuple, or numpy array) to save memory.
- If the function returns large datasets (e.g., DataFrames), store the data in a file (e.g., SQL database) to save memory and avoid performance slowdowns.
