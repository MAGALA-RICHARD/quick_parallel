import unittest
from unittest.mock import patch, MagicMock
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from tqdm import tqdm
from process import quick_parallel, sample_func, sample_func_w_args


class TestQuickParallel(unittest.TestCase):

    def test_quick_parallel_threads(self):
        """Test quick_parallel using threads."""
        # Define a sample function

        iterable = [1, 2, 3, 4, 5]

        # Mock dependencies
        with patch('process.select_type', return_value=ThreadPoolExecutor(max_workers=2)), \
                patch('process.tqdm', side_effect=tqdm) as mock_tqdm:
            # Execute quick_parallel
            results = list(quick_parallel(sample_func, iterable, use_thread=True, n_workers=2))

            # Validate results
            self.assertEqual(bool(results), True)
            mock_tqdm.assert_called_once_with(
                total=5, position=0, leave=True,
                bar_format="Processing multiple jobs via 'sample_func' please wait!{l_bar}{bar}| jobs completed: {n_fmt}/{total_fmt}| Elapsed time: {elapsed}"
            )

    def test_quick_parallel_processes(self):
        """Test quick_parallel using processes."""


        iterable = [1, 2, 3]

        # Mock dependencies
        with patch('process.select_type', return_value=ProcessPoolExecutor(max_workers=2)), \
                patch('process.tqdm', side_effect=tqdm) as mock_tqdm:
            # Execute quick_parallel
            results = list(quick_parallel(sample_func, iterable, use_thread=False, n_workers=2))

            # Validate results
            self.assertEqual(bool(results), True)
            mock_tqdm.assert_called_once_with(
                total=3, position=0, leave=True,
                bar_format="Processing multiple jobs via 'sample_func' please wait!{l_bar}{bar}| jobs completed: {n_fmt}/{total_fmt}| Elapsed time: {elapsed}"
            )

    def test_quick_parallel_with_args(self):
        """Test quick_parallel with additional arguments."""

        # Define a sample function with additional arguments

        iterable = [2, 3, 4]

        # Mock dependencies
        with patch('process.select_type', return_value=ThreadPoolExecutor(max_workers=2)), \
                patch('process.tqdm', side_effect=tqdm) as mock_tqdm:
            # Execute quick_parallel with an extra argument
            results = list(quick_parallel(sample_func_w_args, iterable, 3, use_thread=True, n_workers=2))

            # Validate results
            self.assertEqual(bool(results), True)


if __name__ == "__main__":
    unittest.main()
