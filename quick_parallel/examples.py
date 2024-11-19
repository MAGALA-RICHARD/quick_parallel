from process import quick_parallel


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
    # Example: simple worker without arguments
    gen_d = range(5)  # Replace with your actual generator or iterable

    # Running in a parallel process, using 2 workers and disabling threading
    lm = quick_parallel(worker, gen_d, use_thread=False, n_workers=2,
                        progress_message="Running in simple workf: ")

    # Collect and print the results
    res = [i for i in lm]
    print(res)

    # Example: worker with an extra positional argument

    arg = 9  # Example positional argument (power)
    ext_arg = quick_parallel(worker_with_arguments, gen_d, arg, use_thread=False, n_workers=2,
                             progress_message="Running worker_with_arguments function: ")
    print(list(ext_arg))
    # change the argument, then check if the numbers change
    arg = 10  # Example positional argument (power)
    ext_arg = quick_parallel(worker_with_arguments, gen_d, arg, use_thread=False, n_workers=2,
                             progress_message="Running worker_with_arguments function: ")
    print(list(ext_arg))
