**Pragmatic Unit Testing**

This book and the different chapters talk about how unit testing is an essential, if often part of project and personal success. Unit testing is a relatively inexpensive, easy way to produce better code, faster&quot; Unit testing&quot; is the practice of using small bits of code to exercise the code you&#39;ve written.

Many programmers feel that testing is just a nuisance: an unwanted bother that merely distracts from the real business at hand cutting code. Unit testing is done by programmers, for programmers. It&#39;s here for our benefit alone, to make our lives easier.

The first chapter talks about the importance of unit testing and the author presents us with a real-world scenario where two developers with the same capabilities are writing a program with the same deadline, the only difference is that one of them does unit testing and the other one doesn&#39;t and in the end, having a successful outcome for the developer who took his time, wrote his code and tested it at the same time.

The chapter does a lot of emphasis, letting us know that a unit test is a piece of code written by a developer that exercises a very small, specific area of functionality in the code being tested. Usually a unit test exercises some particular method in a particular context. For example, you might add a large value to a sorted list, then confirm that this value appears at the end of the list. Or you might delete a pattern of characters from a string and then confirm that they are gone. Unit tests are performed to prove that a piece of code does what the developer thinks it should do.

It will make your designs better and drastically reduce the amount of time you spend debugging. We like to write code, and time wasted on debugging is time spent not writing code.

Long story short, unit testing is the _single most effective technique to better coding._

Beyond ensuring that the code does what you want, you need to ensure that the code does what you want all of the time, even when the winds are high, the parameters are suspect, the disk is full, and the network is sluggish. As part of the introduction the author mentions some of the main excuses developers usually say to avoid doing unit testing, here are some examples:

- It takes too much time to write the tests: By writing individual tests with the code itself as you go along, there&#39;s no crunch at the end, and you experience fewer overall bugs as you are generally always working with tested code.  By taking a little extra time all the time, you minimize the risk of needing a huge amount of time at the end.
- It takes too long to run the tests: Most unit tests should execute in the blink of an eye, so you should be

able to run hundreds, even thousands of them in a matter of a few seconds.

- My legacy code is impossible to test: Coding in a culture of fear because you are paralyzed by legacy code is not productive; it&#39;s bad for the project, bad for the programmers, and ultimately bad for business. Introducing unit testing helps break that paralysis.
- It&#39;s not my job to test my code: It&#39;s not polite to expect others to clean up our own messes, and in extreme cases submitting large volumes of buggy code can become a &quot;career limiting&quot; move.
- I don&#39;t really know how the code is supposed to behave so I can&#39;t test it: If you don&#39;t know what the code is supposed to do, then how will you know that it does it?
- But it compiles! : it&#39;s easy to get lulled into thinking that a successful compile is somehow a mark of approval, that you&#39;ve passed some threshold of goodness.
- I&#39;m being paid to write code, not to write tests: presumably you are being paid to write working code, and unit tests are merely a tool toward that end, in the same fashion as an editor, an IDE, or the compiler.
- I feel guilty about putting testers and QA staff out of work.
- My company won&#39;t let me run unit tests on the live system

- Yeah, we unit test already

Chapter 4 and chapter 5 cover the Right-BICEP and CORRECT way to come up with tests. These chapters talk about the specifics on what to test when performing the such called unit testing and in the end they ask the key question_: If the code ran correctly, how would I know?_

If you cannot answer this question satisfactorily, then writing the code or the test may be a complete waste of time If the requirements are truly not yet known, or complete, you can always invent some as a stake in the

ground. They may not be correct from the user&#39;s point of view, but you now know what you think the code should do, and so you can answer the question.

Some of the type of testes mentioned in chapters of the book are:

- Using Data Files: For sets of tests with large amounts of test data, you might want to consider putting the test values and/or results in a separate data file that the unit test reads in except when this is going to consume a lot of I/O and it is not necessarily required.

- Boundary Conditions: Identifying boundary conditions is one of the most valuable parts of unit testing, because this is where most bugs generally live at the edges. These nether-regions of untested code are where almost all exploitable security vulnerabilities come from.

An easy way to think of possible boundary conditions is to remember the acronym _CORRECT_

- **C** onformance: Does the value conform to an expected format?
- **O** rdering: Is the set of values ordered or unordered as appropriate?
- **R** ange: Is the value within reasonable minimum and maximum values?
- **R** eference: Does the code reference anything external that isn&#39;t under direct control of the code?
- **E** xistence: Does the value exist (e.g., is non-null, non-zero, present in a set, etc.)?
- **C** ardinality: Are there exactly enough values?
- **Ti** me (absolute and relative): Is everything happening in order? At the right time? In time?

- Check Inverse Relationships: Some methods can be checked by applying their logical inverse. For instance, you might check a method that calculates a square root by squaring the result and testing that it is tolerably close to the original number.
- Cross-check Using Other Means: Usually there is more than one way to calculate some quantity; we might pick one algorithm over the others because it performs better or has other desirable characteristics. That&#39;s the one we&#39;ll use in production, but we can use one of the other versions to cross-check our results in the test system.

Another way of looking at this issue is to use different pieces of data from the class itself to make sure they all &quot;add up,&quot; or reconcile. That counts as a cross-check as well.

- Force Error Conditions: In the real world, errors happen. Disks fill up, network lines drop, e-mail goes into a black hole, and programs crash. You should be able to test that your code handles all these real-world problems by forcing errors to occur.
- Here are a few environmental things we&#39;ve thought of.

- Running out of memory
- Running out of disk space
- Issues with wall-clock time
- Network availability and errors
- Insufficient File or Path permissions
- System load
- Limited color palette
- Very high or very low video resolution

- Performance Characteristics: you might consider some rough tests just to make sure that the performance curve remains stable this gives us some assurance that we&#39;re still meeting performance targets. But because this one test takes 6–7 seconds to run, we may not want to run it every time. As long as we run it in our automated build at least every couple of days, we&#39;ll quickly be alerted to any problems we may introduce, while there is still time to fix them.

Finally, chapter 5 talks about CORRECT Boundary Conditions and performs a better insight of the acronym discussed earlier, it shows some exercises to perform and practice the type of unit testing with specific lines of code.

**Testing your code**

This article talks about the importance of unit testing and how the different tools that are available in the different versions of python are within our reach, so we can code with more confidence and in an easier way.

Some of the general rules the article mentions for testing code are:

- A testing unit should focus on one tiny bit of functionality and prove it correct.
- Each test unit must be fully independent. Each test must be able to run alone, and also within the test suite, regardless of the order that they are called.
- Try hard to make tests that run fast. If one single test needs more than a few milliseconds to run, development will be slowed down, or the tests will not be run as often as is desirable.
- Learn your tools and learn how to run a single test or a test case.
- Always run the full test suite before a coding session and run it again after.
- It is a good idea to implement a hook that runs all tests before pushing code to a shared repository.
- If you are in the middle of a development session and have to interrupt your work, it is a good idea to write a broken unit test about what you want to develop next.
- The first step when you are debugging your code is to write a new test pinpointing the bug.
- Use long and descriptive names for testing functions.
- When something goes wrong or has to be changed, and if your code has a good set of tests, you or other maintainers will rely largely on the testing suite to fix the problem or modify a given behavior.
- Another use of the testing code is as an introduction to new developers. When someone will have to work on the code base, running and reading the related testing code is often the best thing that they can do to start.

In general, this article mentions and describes some of the tools and libraries that we can use to implement the previous rules. These are some of the tools the author suggests:

- Unittest: is the batteries-included test module in the Python standard library. Its API will be familiar to anyone who has used any of the JUnit/nUnit/CppUnit series of tools.
- Doctest: Which searches for pieces of text that look like interactive Python sessions in docstrings, and then executes those sessions to verify that they work exactly as shown.
- test: is a no-boilerplate alternative to Python&#39;s standard unittest module.
- Hypothesis: is a library which lets you write tests that are parametrized by a source of examples. It then generates simple and comprehensible examples that make your tests fail, letting you find more bugs with less work.
- Tox: is a tool for automating test environment management and testing against multiple interpreter configurations.
- Unittest2: is a backport of Python 2.7&#39;s unittest module which has an improved API and better assertions over the one available in previous versions of Python.
- Mock: s a library for testing in Python. As of Python 3.3, it is available in the standard library.

In conclusion, both readings talk the importance of unit testing and shows some valuable examples and real word scenarios with very specific chunks of code. In the end it is up to us on whether we decide to take this good practice into our tasks daily and do our life easier. Unit testing is the first line of fire when we&#39;re talking about delivering quality work.