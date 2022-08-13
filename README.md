# Python Ecosystem Array Performance Tests

### Intro
There are a few popular array types in the Python ecosystem.

This repo means to answer questions such as-
- how do various array implementatikons perform over various tasks?
- what is their memory consumption?
- which operations are optimal, which are slow?

## Array frameworks that may be tested (in order of interest)
- CPython list
- pandas array
- Cython array.array
- CPython + Cython ([cf](https://www.cardinalpeak.com/blog/faster-python-with-cython-and-pypy-part-2)
- numpy ndarray
- pandas dataframe

## Methodology

1. We will be coding up various stand-alone functions and scripts, and trialing them in various environments, with as close to a "clean room" approach to ensuring all tests are treated equally.
2. We will execute tests using the latest Python stable release ([3.10.6 as of 2 Aug 2022](https://www.python.org/downloads/release/python-3106/)), and pinning to it for the duration of initial development.
3. We may investigate whether there is any advantage to executing these performance tests under an "expected behavior" test framework such as [pytest](https://github.com/pytest-dev/pytest).
   - One attempt was conducted with pytest. It adds a layer of indirection for parameterizing tests, which is inefficient and ultimately added no benefit.
   - Therefore no testing framework will be used, perhaps just argparse for directing the size and iterations of tests

## Principles

1. Running multiple iterations of tests will be part of the external performance test-running framework, and never part  of any test
2. Collection sizing will be specified as a parameter to all tests, so that performance of operations on arrays of  various sizes might be explored
3. Tests will follow the "all things being equal rule" of ensuring operations and the contained datatypes are as near possible to equivalent
4. Tests of "same ops" will then vary by array types, but this may also cause the stored datatype to be different across array frameworks, and this must be noted when comparing memory and CPU time
5. Test types may vary widely.
6. Test source data may vary as needed; generating synthetic arrays, reading arrays from external sources, initializing arrays to a single value -all things are possible
7. Hybrid operations are permissible, but must be as identical as possible across array frameworks
8. It is a-okay to import tests from articles, blogs, gists and other test suites -all part of the process of learning what makes a particular piece of code slow or fast
9. We will organize results so that the strengths and weaknesses of each framework and operation may be easily determined.
