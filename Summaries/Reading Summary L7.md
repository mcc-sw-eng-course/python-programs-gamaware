**UML Distilled**

The chapters that were reviewed, talk about the different and probably the most important approaches on how to work with UML, it begins exploring the Class Diagrams, then the Sequence Diagrams and also the Advanced concepts of such class diagrams. The reading ends with the chapter on State Machine Diagrams. In general terms, these readings are useful when we developers try to design certain behavior on our products and the specifics on those diagrams are as follow:

**Class Diagrams**

Class diagram describes the types of objects in the System and the various kinds of static relationships that exist among them. These diagrams also show the properties and operations of a Class and the constraints that apply to the way objects are connected. The UML uses the term feature as a general term that covers properties and operations of a Class.

Properties represent structural features of a Class. As a first approximation, we can think of properties as corresponding to fields in a Class. The reality is rather involved, as we shall see, but that&#39;s a reasonable place to start.

According to the author, the attribute notation describes a property as a line of text within the class box itself.

An association is a solid line between two classes, directed from the source. The name of the property goes at the target end of the association, together with its multiplicity. The target end of the association links to the class that is the type of the property.

Also, the multiplicity of a property is an indication of how many objects may fill the property:

In attributes, you come across various terms that refer to the multiplicity.

- Optional implies a lower bound of 0.
- Mandatory implies a lower bound of 1 or possibly more.
- Single-valued implies an upper bound of 1.
- Multivalued implies an upper bound of more than 1: usually &#39;~.

And another common kind of association is a bidirectional association which is a pair of properties that are linked together as inverses. In general terms the bidirectional nature of the association is made obvious by

the navigability arrows at both ends of any association; the UML allows you to use this form either to indicate a bidirectional association or when you aren&#39;t showing navigability. The general preference is to use the double-headed arrows when you want to make it clear that you have a bidirectional association.

In other case operations are the actions that a class knows to carry out. Operations most obviously correspond to the methods of a class. Normally, you don&#39;t show those operations that simply manipulate properties, because they can usually be inferred. With conceptual models, you shouldn&#39;t use operations to specify the Interface of a class. Instead, use them to indicate the principal responsibilities of that class, perhaps using a couple of words summarizing a CRC responsibility.

As a matter of fact, UML defines a query as an operation that gets a value from a class without changing the system state-in other words, without side effects.

The author also talks about some of the typical examples of generalization which involves the personal and corporate customers of a business. They have differences but also many similarities. The similarities can be placed in a general Customer class (the Supertype), with Personal Customer and Corporate Customer as subtypes.

Even though the indication of the components of classes are stated in this chapter, in future chapters he talks about the advanced concepts but as such, one of the basic ones are the Notes are comments in the diagrams. Notes can stand at their own, or they can be linked with a dashed line to the elements they are commenting They can appear in any kind of diagram, dependency exists between two elements if changes to the definition of one element (the supplier) may cause changes to the other (the client). With classes, dependencies exist for various reasons: One class sends a message to another; one class has another as part of its data; one class mentions another as a parameter to an operation. If a class changes its interface, any message sent to that class may no longer be valid.

In the end, the _UML allows you to depict dependencies between all sorts of elements_. You use dependencies whenever you want to show how changes in one element might alter other elements and Class diagrams are the backbone of the UML.

The biggest danger with class diagrams is that you can focus exclusively on structure and ignore behavior. Therefore, when drawing class diagrams to understand software, always do them in conjunction with some form of behavioral technique. If you&#39;re going well, you&#39;11 find yourself swapping between the techniques. Frequently.

**Sequence Diagrams**

Interaction diagrams describe how groups of objects collaborate in some behavior. The UML defines several forms of interaction diagram, of which the most common is the sequence diagram. _Sequence diagrams show the interaction_ by showing each participant with a lifeline that runs vertically down the page and the ordering of messages by reading down the page. The sequence diagram indicates the differences in how the participants interact therefore this is the great strength of such diagrams. They aren&#39;t good at showing details of algorithms, like loops and conditional behavior, but they make the calls between participants crystal clear and give a really good picture about which participants are doing which processing.

A common issue with sequence diagrams is how to show looping and conditional behavior. The first thing to point out is that this isn&#39;t what sequence diagrams are good at. If you want to show control structures like this, you are better off with an activity diagram or indeed with code itself

According to the author there are _synchronous and asynchronous_ Calls:

In UML 2, filled arrowheads show a synchronous message, while stick arrowheads show an asynchronous message.

- If a caller sends a synchronous message, it must wait until the message is

done, such as invoking a subroutine.

- If a caller sends an asynchronous message, it can continue processing and doesn&#39;t have to wait for a response.

Asynchronous calls in multithreaded applications and in message-oriented middleware are a bit common. But it is also worth noting that asynchrony gives better responsiveness and reduces the temporal coupling but is harder to debug

In the end we should use sequence diagrams when we want to look at the behavior of several objects within a single use case. _Sequence diagrams are good at showing collaborations among the objects; they are not so good at precise definition of the behavior_

**Class Diagrams: Advanced Concepts**

Chapter 4 of the book talks about more advanced concepts of the class diagram technique, however, and it is mentioned that it has dozens of other notations. But the author mentions that we shouldn&#39;t use them all the time, but just when they&#39;re appropriate, these notations are:

- Keyword: The UML often tries to reduce the number of symbols and use keywords instead.
- Responsibilities: The best way to show them is as comment strings in their own compartment in the class.
- Static Operations and Attributes: The UML refers to an operation or an attribute that applies to a class rather than to an instance as static. This is equivalent to static members in C-based languages. Static features are underlined a class diagram-
- Aggregation and Composition: Aggregation is the part-of relationship. It&#39;s like saying that a car has an engine and wheels as its parts.
- Derived Properties: Derived properties can be calculated based on other values
- Interfaces and Abstract Classes: An abstract class is a class that cannot be directly instantiated. Instead, you instantiate an instance of a subclass.
- Read-Only and Frozen: A property is frozen if it cannot change during the lifetime of an object.
- Reference Objects and Value Objects: Reference objects are such things as Customer. Here, identity is very important because you usually want only one software object to designate a Customer in the real world.
- Qualified Associations: A qualified association is the UML equivalent of a programming concept variously known as associative arrays, maps, hashes, and dictionaries.
- Classification and Generalization: e UML uses the generalization Symbol to show generalization. If you need to show classification, use a dependency with the «instantiate» keyword.
- Multiple and Dynamic Classification: In single classification, an object belongs to a single type, which may inherit from supertypes. In multiple classification, an object may be described by several types that are not necessarily connected by inheritance.
- Association Class: Association classes allow you to add attributes, operations, and other features

to associations.

- Template (Parameterized) Class: This concept is most obviously useful for working with collections in a

strongly typed language.

- Enumerations: Enumerations are used to show a fixed set of values that don&#39;t have any properties other than their symbolic value.
- Active Class: An active class has instances, each of which executes and controls its own thread of control
- Visibility: Visibility is a subject that is simple in principle but has complex subtleties.
- Messages: message Information Spans multiple use Gases, so they aren&#39;t numbered

to Show sequences, unlike communication diagrams.

**State Machine Diagrams**

State machine diagrams are a familiar technique to describe the behavior of a System. Various forms of State diagrams have been around since the 1960s and the earliest object-oriented techniques adopted them to show behavior. In object-oriented approaches, you draw a State machine diagram for a single class to show the lifetime behavior of a single object. The diagram shows that the controller can be in three states: _Wait, Lock, and Open_. The diagram also gives the rules by which the controller changes from State to State. These rules are in the form of transitions: the lines that connect the states.

When developers talk about objects, they often refer to the state of the objects to mean the combination of all the data in the fields of the objects. However, the state in a state machine diagram is a more abstract notion of

states essentially, different states imply a different way of reacting to events.

- Internal Activities: States can react to events without transition, using internal activities: putting the event, guard, and activity inside the state box itself.
- Activity States: In the states I&#39;ve described so far, the object is quiet and waiting for the next event before it does something. However, you can have states in which the object is doing some ongoing work.
- Superstrates: Often, you&#39;ll find that several states share common transitions and internal activities. In these cases, you can make them substrates and move the shared behavior into a super state. Without the super state, you would have to draw a cancel transition for all three states within the enter connection details state.
- Concurrent States: States can be broken into several orthogonal state diagrams that run concurrently.

In the last part of the reading it is shown how _Implementing Stare Diagrams_ works:

A Stare diagram can be implemented in three main ways: _nested switch, the State pattern, and state tables_



_When to Use Stare Diagrams_:

State diagrams are good at describing the behavior of an object across several use cases. State diagrams are not very good at describing behavior that involves several objects collaborating. As such, it is useful to combine state diagrams with other techniques. For instance, interaction diagrams are good at describing the behavior of several objects in a single use case, and activity diagrams are good at showing the general sequence of activities for several objects and use cases.

In the end, it depends on how we want to make use of the UML notations and the needs we have to implement one or another type of the different diagrams previously described.