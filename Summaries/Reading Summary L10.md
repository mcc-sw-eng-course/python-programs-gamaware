**Pragmatic Paranoia**

Chapter four of the book &quot;The pragmatic programmer&quot; begins with a statement that might sound sad, but it is the reality, &quot;You can&#39;t write perfect software&quot; so we need to take advantage of this fact.

As the author mentions, we are constantly interfacing with other people&#39;s code that might not live up to our high standards and dealing with inputs that may or may not be valid. So, we are taught to code defensively. If there&#39;s any doubt, we validate all information we&#39;re given. We use assertions to detect bad data. We check for consistency, put constraints on database columns, and generally feel pretty good about ourselves.

But _Pragmatic Programmers_ take this a step further. They don&#39;t trust themselves, either. Knowing that no one writes perfect code, including themselves, Pragmatic Programmers code in defenses against their own mistakes. We describe the first defensive measure in _Design by Contract_: clients and suppliers must agree on rights and responsibilities.

**Design by Contract**

The concept was initially developed by Bertrand Meyer for the language Eiffel which It is a simple yet powerful technique that focuses on documenting (and agreeing to) the rights and responsibilities of software modules to ensure program correctness, which turns out that it is one that does no more and no less than it claims to do. Documenting and verifying that claim is the heart of Design by Contract (_DBC_, for short).

Every function and method in a software system does something. Before it starts that something, the routine may have some expectation of the state of the world, and it may be able to make a statement about the state of the world when it concludes. Meyer describes these expectations and claims as follows:

- **Preconditions**. What must be true for the routine to be called; the routine&#39;s requirements. A routine should never get called when its preconditions would be violated. It is the caller&#39;s responsibility to pass good data.
- **Postconditions**. What the routine is guaranteed to do; the state of the world when the routine is done. The fact that the routine has a postcondition implies that it will conclude: infinite loops aren&#39;t allowed.
- **Class invariants**. A class ensures that this condition is always true from the perspective of a caller. During internal processing of a routine, the invariant may not hold, but by the time the routine exits, and control returns to the caller, the invariant must be true.

The greatest benefit of using DBC may be that it forces the issue of requirements and guarantees to the forefront. Simply enumerating at design time what the input domain range is, what the boundary conditions are, and what the routine promises to deliver or, more importantly, what it doesn&#39;t promise to deliver is a huge leap forward in writing better software. By not stating these things, you are back to programming by coincidence, which is where many projects start, finish, and fail.

- **Assertions**

While documenting these assumptions is a great start, you can get much greater benefit by having the compiler check your contract for you. You can partially emulate this in some languages by using assertions. This means that if you override a base class method that has a contract, the assertions that implement that contract will not be called correctly. You must remember to call the class invariant manually before you exit every method.
The basic problem is that the contract is not automatically enforced. Finally, the runtime system and libraries are not designed to support contracts, so these calls are not checked. This is a big loss, because it is often at the boundary between your code and the libraries it uses that the most problems are detected.

- **Language Support**

You get the greatest benefit in this case because all the code base must honor their contracts. It takes comments and generates a new source file with the assertion logic included. They can be messy to integrate into your project, and other libraries you use won&#39;t have contracts.

- **Loop Invariants**

Getting the boundary conditions right on a nontrivial loop can be problematic. Loops are subject to the banana problem, fencepost errors, and the ubiquitous &quot;off by one&quot; error. You can think of it as a kind of miniature contract.

- **Semantic Invariants**

You can use semantic invariants to express inviolate requirements, a kind of &quot;philosophical contract&quot;. We once wrote a debit card transaction switch. A major requirement was that the user of a debit card should never have the same trans-action applied to their account twice. Be sure not to confuse requirements that are fixed, inviolate laws with those that are merely policies that might change with a new management regime.

**Dynamic Contracts and Agents**

Until now, we have talked about contracts as fixed, immutable specifications. But in the landscape of autonomous agents, this doesn&#39;t need to be the case. By the definition of &quot;autonomous&quot; agents are free to reject requests that they do not want to honor

**Dead Programs Tell No Lies**

In the section, the author states that If something is starting to go wrong with one of our programs, sometimes it is a library routine that catches it first. Maybe a stray pointer has caused us to overwrite a file handle with something meaningless. The next call to read will catch it. It&#39;s easy to fall into the &quot;it can&#39;t happen&quot; mentality.
We&#39;re checking that the correct versions of shared libraries were loaded. You could convince yourself that the error can&#39;t happen and choose to ignore it but it is better to be aware of the possibility and do something about it, that is way we can take in consideration the following.

- **Crash, Don&#39;t Trash**

One of the benefits of detecting problems as soon as you can is that you can crash earlier. And many times, crashing your program is the best thing you can do.

- **Assertive Programming**

If you need to free resources, have an assertion failure generate an exception, longjmp to an exit point, or call an error handler. Just make sure the code you execute in those dying milliseconds doesn&#39;t rely on the information that triggered the assertion failure in the first place.

- **Leave Assertions Turned On**

For any complex program you are unlikely to test even a miniscule percentage of the permutations your code will be put through. The optimists are forgetting that your program runs in a dangerous world. During testing, rats probably won&#39;t gnaw through a communications cable, someone playing a game won&#39;t exhaust memory, and log files won&#39;t fill the hard drive.
These things might happen when your program runs in a production environment. Turning off assertions when you deliver a program to production is like crossing a high wire without a net because you once made it across in practice. There&#39;s dramatic value, but it&#39;s hard to get life insurance.

- **When to Use Exceptions**

In Dead Programs Tell No Lies, the author suggested that it is good practice to check for every possible error particularly the unexpected ones. However, in practice this can lead to some ugly code; the normal logic of your program can end up being totally obscured by error handling, particularly if you subscribe to the &quot;a routine must have a single return statement&quot; school of programming.

- **What Is Exceptional?**

One of the problems with exceptions is knowing when to use them. Assume that an uncaught exception will terminate your program and ask yourself, &quot;Will this code still run if I remove all the exception handlers?&quot; If the answer is &quot;no&quot; then maybe exceptions are being used in nonexceptional circumstances. Our answer is, _&quot;It depends._&quot; If the file should have been there, then an exception is warranted.

- **How to Balance Resources**

We all manage resources whenever we code: memory, transactions, threads, files, timers all kinds of things with limited availability. Most of the time, resource usage follows a predictable pattern: you allocate the resource, use it, and then deallocate it.

- **Objects and Exceptions**

If you are programming in an object-oriented language, you may find it useful to encapsulate resources in classes. When the object goes out of scope, or is reclaimed by the garbage collector, the object&#39;s destructor then deallocates the wrapped resource. This approach has benefits when you&#39;re working with languages such as C++, where exceptions can interfere with resource deallocation.

- **Balancing and Exceptions**

Languages that support exceptions can make resource deallocation tricky. If an exception is thrown, how do you guarantee that everything allocated prior to the exception is tidied up? The answer _depends_ to some extent on the language.

**Bend, or Break**

In this chapter, it is specified how to make reversible decisions, so your code can stay flexible and adaptable in the face of an uncertain world. A good way to stay flexible is to write less code. Changing code leaves you open to the possibility of introducing new bugs.
Metaprogramming explain how to move details out of the code completely, where they can be changed more safely and easily. In Temporal Coupling, we&#39;ll look at two aspects of time as they relate to coupling. Not if you want to stay flexible. A key concept in creating flexible code is the separation of a data model from a view, or presentation, of that model.

**Decoupling and the Law of Demeter**

Although individuals in each cell may know each other, they have no knowledge of those in other cells. If one cell is discovered, no amount of truth serum will reveal the names of others outside the cell. We feel that this is a good principle to apply to coding as well.

- **Minimize Coupling**

Suppose you are remodeling your house or building a house from scratch. A typical arrangement involves a &quot;general contractor&quot; You hire the contractor to get the work done, but the contractor may or may not. We&#39;d like to follow this same model in software. When we ask an object for a service, we&#39;d like the service to be performed on our behalf. You want to let your users select a recorder and plot its data, labeled with the correct time zone.

- **The Law of Demeter for Functions**

The Law of Demeter for functions attempts to minimize coupling between modules in any given program. It tries to prevent you from reaching into an object to gain access to a third object&#39;s methods.

**Metaprogramming**

Details mess up our pristine code especially if they change frequently. Every time we must go in and change the code to accommodate some change in business logic, or in the law, or in management&#39;s personal tastes of the day, we run the risk of breaking the system of introducing a new bug. So, we say &quot;out with the details!&quot; Get them out of the code. While we&#39;re at it, we can make our code highly configurable and &quot;soft&quot; that is, easily adaptable to changes.

- **Dynamic Configuration**

Not just things such as screen colors and prompt text, but deeply ingrained items such as the choice of algorithms, database products, middleware technology, and user-interface style. These items should be implemented as configuration options, not through integration or engineering. You should be able to access and manipulate this information just as you would any other data in the database. Typically, metadata is accessed and used at runtime, not at compile time.

- **Metadata-Driven Applications**

We want to configure and drive the application via metadata as much as possible. Our goal is to think declaratively and create highly dynamic and adaptable programs.

- **Business Logic**

So, you&#39;ve made the choice of database engine a configuration option and provided metadata to determine the user-interface style. Maybe you are writing a system with horrendous workflow requirements. Actions start and stop according to complex business rules. Consider encoding them in rule-based system, embedded within your application. That way, you&#39;ll configure it by writing rules, not cutting code. Less complex logic can be expressed using a minilanguage, removing the need to recompile and redeploy when the environment changes.

- **Cooperative Configuration**

We&#39;ve talked about users and developers configuring dynamic applications. Your larger applications probably already have issues with handling different versions of data and different releases of libraries and operating systems.Perhaps a more dynamic approach will help.

**Temporal Coupling**

Time is an often-ignored aspect of software architectures. Instead, we are talking about the role of time as a design element of the software itself. We don&#39;t usually approach programming with either of these aspects in mind. When people first sit down to design an architecture or write a program, things tend to be linear.
This approach is not very flexible, and not very realistic. We need to allow for concurrency 3 and to think about decoupling any time or order dependencies. In doing so, we can gain flexibility and reduce any time-based dependencies in many areas of development: _workflow analysis, architecture, design, and deployment_.

**It&#39;s Just a View**

Early on we are taught not to write a program as a single big chunk, but that we should _&quot;divide and conquer&quot;_ and separate a program into modules. We want each module to be like the man in the song and just hear what it wants to hear. An event is simply a special message that says, &quot;something interesting just happened&quot;. We can use events to signal changes in one object that some other object may be interested in.  In fact, there could be multiple receivers, each one focused on its own agenda. We need to exercise some care in using events, however. In an early version of Java, for example, one routine received all the events destined for an application.

And last but not least.

**Blackboards**

You may not usually associate elegance with police detectives, picturing instead some sort of doughnut and coffee cliché. Each detective may make contributions to this potential murder mystery by adding facts, statements from witnesses, any forensic evidence that might arise, and so on. This process continues, across all shifts, with many different people and agents, until the case is closed.

- None of the detectives needs to know of the existence of any other detective they watch the board for new information and add their findings.
- The detectives may be trained in different disciplines, may have different levels of education and expertise, and may not even work in the same precinct. They share a desire to solve the case, but that&#39;s all.
- Different detectives may come and go during the process and may work different shifts.
- There are no restrictions on what may be placed on the blackboard. It may be pictures, sentences, physical evidence, and so on.

In general terms these chapters talk about the best practices we can take in consideration when using design patterns and it provides examples with code in many different languages. I&#39;ve come to the conclusion, that using object-oriented design is probably one of the best approaches we can use when following these practices as it provides modularity to the code, but there are also many _&quot;ins and outs&quot;_ one should consider when doing so.