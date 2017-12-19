PageChecker
-

The scripts use only built-in libraries of Python 2.7, so as long as you have Python 2.7 installed, there's no need to install any other libraries. 

>To test solutions with unit tests for the three problems:

`python p1.py`

`python p2.py`

`python p3.py`

>To test project assigement in the `pagechecker` folder:

`python test.py`

>To run the pagechecker:

`python pagechecker.py`

>To terminate the process:

`ctrl + c`

The original problems and project
-

>Problem 1*

Transform these lists (left side is INPUT, right side is OUTPUT):

[1,2,3,1,5] → [15,11,13,12,11]

[‘a’,’b’,’c’,’d’,’e’] → [‘e’,’d’,’c’,’b’,’a’]

[‘a’,’b’,’c’,’d’,’e’] → [‘a’,’c’,’e’]

[‘a’,’b’,’c’,’d’,’e’] → [‘b’,’d’]

[11,6,10] → [11,10,6,[27]]


>Problem 2*

We have a function complex_function to compute certain data, printing out the result after the computation. This is great, but we want to add some functionality. We want to push to a log:

- the time used by the function to run

- the name of the function

- the input values of the function.

Note: We cannot modify the body of the original complex_function function!!

>Problem 3*

Define a custom MyDict class that allows you the following operations:

- set/read values using the dot notation (e.g. mydict.name). In case the mapped value is not present, returns None

- A + B addition operation.

 - MyDict + dict = MyDict;

 - MyDict + MyDict = MyDict;

 - the result of this operation is a MyDict object, having all the members of both dictionaries. In case of common keys between the dictionaries, their values need to be added/appended together (according to their type - consider types to be only int and string).
 
>Project Assignment

We want to check a list of urls at regular intervals, to make sure these are reachable and that we can get their content. Create a program that you can feed with a list of URLs and check intervals. For instance:

[(‘http://cnn.com’,10),

(‘http://google.ca’,20),

(‘http://cnn.com’,15),

(‘http://httpbin.org/delay/20’,15)]

where in each tuple, the first element is the url and the second element the number of seconds between checks.

Provide a solution that performs such task and, as output, provides timestamp, url and length of the body.

Eg:

13/11/17 11:18:20 - http://cnn.com - 231274 Bytes

13/11/17 11:18:27 - http://google.ca - 55609 Bytes

13/11/17 11:18:30 - http://cnn.com - 231274 Bytes

13/11/17 11:18:47 - http://google.ca - 55609 Bytes

…

In your implementation, be mindful that we need to respect the defined schedule as much as possible. This means you have to think of a solution that isn't affected by the time a single URL takes, nor by the fact that some URLs fail. Consider the best design pattern for this. Try to tackle as many corner cases as you can think (for instance, what happens in case the url is not reachable? How to reduce the delay in the capture of such links? …anything you can think of!)

Also, provide some test cases for your implementation (choose the most meaningful - no need to cover everything!).
