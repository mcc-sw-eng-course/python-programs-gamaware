**Design Principles and Design Patterns**

This reading talks about the different approaches on Design patterns and gives us a closer look at them in detail. Design of many software applications begins as a vital image in the minds of its designers. At this stage it is clean, elegant, and compelling. It has a simple beauty that makes the designers and implementers itch to see it working. Some of these applications manage to maintain this purity of design through

the initial development and into the first release. Everything begins stating the different symptoms that give insight on why some designs are not well designed, these are:

- **Rigidity** : Which is the tendency for software to be difficult to change, even in simple ways. Every change causes a cascade of subsequent changes in dependent modules.
- **Fragility** : Which is the tendency of the software to break in many places every time it is changed. Often the breakage occurs in areas that have no conceptual relationship with the area that was changed.
- **Immobility** : Which is the inability to reuse software from other projects or from parts of the same project. It often happens that one engineer will discover that he needs a module that is like one that another engineer wrote.
- **Viscosity** : Which comes in two forms: viscosity of the design, and viscosity of the environment. When faced with a change, engineers usually find more than one way to make the change. Some of the ways preserve the design, others do not. Viscosity of environment comes about when the development environment is slow and inefficient.

Another bad practice is the fact that the requirements constantly change, often these changes need to be made quickly, and may be made by engineers who are not familiar with the original design philosophy. So, though the change to the design works, it somehow violates the original design. Bit by bit, as the changes continue to pour in, these violations accumulate until malignancy sets in.

Another topic that the author explores is the _dependency management_, which states that to forestall the degradation of the dependency architecture, the dependencies between modules in an application must be managed. This management consists of the creation of dependency firewalls. Across such firewalls, dependencies do not propagate.

**The Open closed principle (OCP)**

In this section, it is stated that we should write our modules so that they can be extended, without requiring them to be modified. In other words, we want to be able to change what the modules do, without changing the source code, therefore there are several techniques for achieving the _OCP_ on a large scale.

- **Dynamic Polymorphism:**  Programs that are designed this way tend to be littered with similar if/else or switch statement. Every time anything needs to be done to the modem, a switch statement if/else chain will need to select the proper functions to use. When new modems are added, or modem policy changes, the code must be scanned for all these selection statements, and each must be appropriately modified.
- **Static Polymorphism:** Another technique for conforming to the OCP is using templates or generics.
- **Architectural Goals of the OCP:** By using these techniques to conform to the OCP, we can create modules that are extensible, without being changed. This means that, with a little forethought, we can add new features to existing code, without changing the existing code and by only adding new code.

**The Liskov Substitution Principle (LSP)**

This concept states that derived classes should be substitutable for their base classes. That is, a user of a base class should continue to function properly if a derivative of that base class is passed to it.

The examples above are just a few of the topics that are shown in the reading. Unfortunately, LSP violations are difficult to detect until it is too late. In the _Circle/Ellipse_ which is another case for instance, everything works fine until some client came along and discovered that the implicit contract had been violated.

**The Dependency Inversion Principle (DIP)**

If the OCP states the goal of OO architecture, the DIP states the primary mechanism. Dependency Inversion is the strategy of depending upon interfaces or abstract functions and classes, rather than upon concrete functions and classes. This principle is the enabling force behind component design, COM, CORBA, EJB, etc.

Procedural designs exhibit a kind of dependency structure. An object-oriented architecture shows a very different dependency structure, one in which most dependencies point towards abstractions. Moreover, the modules that contain detailed implementation are no longer depended upon, rather they depend themselves upon abstractions.

Depending upon Abstractions. The implication of this principle is quite simple. Every dependency in the design should target an interface, or an abstract class. No dependency should target a concrete class.

Mitigating Forces. One motivation behind the DIP is to prevent you from depending upon volatile modules. The DIP assumes that anything concrete is volatile. While this is frequently so, especially in early development, there are exceptions Object Creation. One of the most common places that designs depend upon concrete classes is when those designs create instances. You cannot create instances of abstract classes. Thus, to create an instance, you must depend upon a concrete class.

**The Interface Segregation Principle (ISP)**

The ISP is another one of the enabling technologies supporting component substrates such as COM. Without it, components and classes would be much less useful and portable.

**Principles of Package Architecture**

Classes are a necessary, but insufficient, means of organizing a design. The larger granularity of packages is needed to help bring order. But how do we choose which classes belong in which packages. Below are three principles known as the Package Cohesion Principles, that attempt to help the software architect.

**The Release Reuse Equivalency Principle (REP)**

A reusable element, be it a component, a class, or a cluster of classes, cannot be reused unless it is managed by a release system of some kind. Users will be unwilling to use the element if they are forced to upgrade every time the author changes it.

**The Common Closure Principle (CCP)**

A large development project is subdivided into a large network of interrelated packages. The work to manage, test, and release those packages is non-trivial. The more packages that change in any given release, the greater the work to rebuild, test, and deploy the release.

**The Common Reuse Principle (CRP)**

A dependency upon a package is a dependency upon everything within the package. When a package changes, and its release number is bumped, all clients of that package must verify that they work with the new package, even if nothing they used within the package changed.

**The Acyclic Dependencies Principle (ADP)**

Since packages are the granule of release, they also tend to focus manpower. Engineers will typically work inside a single package rather than working on dozens. This tendency is amplified by the package cohesion principles, since they tend to group together those classes that are related. Thus, engineers will find that their changes are directed into just a few packages. Once those changes are made, they can release those packages to the rest of the project.

**The Stable Dependencies Principle (SDP)**

Stability is related to the amount of work required to make a change. The penny is not stable because it requires very little work to topple it. On the other hand, a table is very stable because it takes a considerable amount of effort to turn it over.

**The Stable Abstractions Principle (SAP)**

The more packages that are hard to change, the less flexible our overall design will be. However, there is a loophole we can crawl through. The highly stable packages at the bottom of the dependency network may be very difficult to change, but according to the OCP they do not have to be difficult to extend!

**Patterns of Object-Oriented Architecture**

When following the principles described above to create object-oriented architectures, one finds that one repeats the same structures repeatedly. These repeating structures of design and architecture are known as _design patterns_. The essential definition of a design pattern is a well-worn and known good solution to a common problem. Design patterns are definitively not new. Rather they are old techniques that have shown their usefulness over a period of many years. Some common design patterns are described below. These are the patterns that you will come across while reading through the case studies later in the book.

At the end of the day the concept of object-oriented architecture shows us the structure of classes and packages that keeps the software application _flexible, robust, reusable, and developable_. The principles and patterns presented here support such architectures and have been proven over time to be powerful aids in software architecture. In a general matter the whole chapter has been an overview but there is much more to be said about the topic of OO architecture than can be said.

**What is a pattern?**

Patterns are effective means of communication between software developers. Pat terns, in a sense, help bring order into the chaos. Patterns represent best practice, proven solutions, and lessons learned, that aid in evolving software engineering into a mature engineering discipline. The aim is that every software developer should be able to use patterns when building software systems. Thus, to reach this aim, large pattern sets must be presented in a form of languages, catalogs, systems, or even handbooks.

A pattern describes a problem which occurs repeatedly in our environment, and then describes the core of the solution to that problem, in such a way that you can use this solution a million times over, without

ever doing it the same way twice.

In this paper, it is suggested, that there are some misconceptions regarding patterns:

- **patterns are only object-oriented:** Patterns are not only object-oriented Patterns in the software are often identified only with object-oriented software. Although most of the patterns are object-oriented, patterns can also be found in variety of software systems, independently of the methods used in developing those systems.
- **Patterns provide more than one solution:** Patterns describe solutions to the recurring problems, but do not provide an exact solution, rather capture more than one solution. This implies that a pattern is not an implementation, although it may provide hints about potential implementation issues.
- **Patterns are implementations.**
- **every solution is a pattern:** Every solution is not necessary a pattern Not every solution, algorithm, or heuristic can be viewed as a pattern. In order to be considered as a pattern, the solution must be verified as recurring solution to a recurring problem.

In general terms, every solution is not necessary a pattern Not every solution, algorithm, or heuristic can be viewed as a pattern. In order to be considered as a pattern, the solution must be verified as recurring solution to a recurring problem, however not every pattern can be considered to be a good pattern. There is a set of properties that a pattern must fulfill in order to be a good one. A pattern encapsulating:

- a solution (but not obvious).
- a proven concept.
- relationships, and.
- human component.

The author also considers the classifications of them which can be as follows:

- Generative and non-generative patterns or also called Gamma Patterns: which are descriptive and passive, since they describe recurring phenomenon&#39;s without necessary describing the way of reproducing these phenomenon&#39;s.
- Types of software patterns:
  - design patterns, which are patterns in software engineering.
  - analysis patterns, which are patterns that describe recurring and reusable analysis models.
  - organization patterns, which are patterns that describe software process design.
  - other domain-specific patterns.
  - conceptual patterns.
  - design patterns.
  - programming patterns.
- Types of design patterns:
  - architectural patterns.
  - design patterns, and
  - idioms.

There&#39;s also the consideration of the pattern templates such as:

- Alexandrian form.
- GoF format.
- And other templates.

And finally, three different types of pattern collections have been identified pattern language, pattern system, and pattern catalog. These three pattern collections possess varying degrees of structure and interaction. In this section the definition and basic characteristics of each of these pattern collections is given.

We can say that the characteristics of patterns apply not only to software but to other artifacts and can be used in a variety of implementations with basic concepts such as the previously explained templates, languages, system, and pattern catalogs.