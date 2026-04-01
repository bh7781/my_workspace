import time
import tracemalloc
from typing import Callable, Any


class PerformanceAnalyzer:
    @staticmethod
    def measure(func: Callable) -> Callable:
        """
        Decorator to measure execution time and memory usage of a function.
        """

        def wrapper(*args, **kwargs) -> Any:
            # Start time tracking
            start_time = time.perf_counter()

            # Start memory tracking
            tracemalloc.start()

            result = func(*args, **kwargs)

            # Stop time tracking
            end_time = time.perf_counter()

            # Stop memory tracking
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            # Print results
            print(f"\nPerformance Report for: {func.__name__}")
            print(f"Execution Time: {(end_time - start_time) * 1000:.4f} ms")
            print(f"Current Memory Usage: {current / 1024:.4f} KB")
            print(f"Peak Memory Usage: {peak / 1024:.4f} KB\n")

            return result

        return wrapper
