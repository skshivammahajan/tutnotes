import time

import datetime


def time_func(function):
    """ This decorator calculates the amount of time a function takes to execute.

    When time_func is applied to a function it records how long the function takes to
    finish and add the elapsed time to the functions attributes.

    - **parameters**
    :param function: The function you want to add the elapsed time attribute to.

    :Example:
    @time_func
    def example(name, **kwargs):
      meta = type(name, (object,), kwargs)
      return meta

    example('foo')
    print example.elapsed
    0:00:00.000052

    """
    def new_func(*args, **kwargs):
        # Start the clock.
        start = datetime.datetime.now()
        # Execute the function and record the results.
        function_result = function(*args, **kwargs)
        # Calculate the elapsed time and add it to the function
        # attributes.
        new_func.elapsed = datetime.datetime.now() - start
        # Returned the function with the added elapsed attribute
        return function_result
    return new_func


def execution_time(method):
    def funct(*args, **kwargs):
        start_time = time.time()
        method(*args)
        end_time = time.time()
        total_execution_time = end_time - start_time
        print("TOTAL_EXECUTION_TIME = ", total_execution_time)
    return funct


@execution_time
def even_number():
    num = 11
    result = [i for i in range(1, num) if i % 2 == 0]
    print(result)


@execution_time
def even_number_arguments(num, num2, b=10):
    result = [i for i in range(1, num) if i % 2 == 0]
    print(result)


even_number()
even_number_arguments(21, 10, 11)


@time_func
def example(name, **kwargs):
    meta = type(name, (object,), kwargs)
    return meta


print(example('foo'))
