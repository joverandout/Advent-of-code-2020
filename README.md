# advent-of-code-2020

My solutions to advent of code (https://adventofcode.com/2020)

Languages used for solutions:
* Days 1-9: Python
* Days 10-12: Haskell
* Days 13-14: Python
* Days 15-16: Haskell
* Days 17-25: Python
 
All the haskell solutions need to be run in a `stack` environment, such as the one seen in day 10. For other days that use haskell I haven't uploaded all the stack files as they're quite cluttered. To download `stack` please visit https://docs.haskellstack.org/en/stable/README/ To run use `stack run` but ensure all imported dependencies such as `intMaps` have been added to the `.cabal` file.  Once you've imported all necessary dependencies it is possible to test the individual functions:
```
stack repl
=> [function name] [function perameters]
RESULT
```
To run any written tests (although most days I haven't written any) run the following command:
```
stack test
```
To run the program and get the output to both parts concurrently without of the need of parameters use:
```
stack run
```

Python scripts are pretty straightforward and run as you would expect I suggest using `python3` as follows: `python3 filename.py`/ For example...
```
$ python3 day[xx].py
```
On windows however run:
```
python.exe day[xx].py
```
Or
```
py day[xx].py
```
Depending on the version of your python installation. You can check this with the commands depending on your operating system. Consolt your help command if you have any issues.


