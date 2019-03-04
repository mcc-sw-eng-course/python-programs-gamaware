**Use Coding Standards to Increase Efficiency and Productivity**

The purpose of the paper provides information on the importance of coding standards, and how using them effectively can help organizations achieve a variety of benefits, including reduced development costs, and increased efficiency and productivity.

In general terms, the paper talks about the following topics:

- What are coding standards?

Which states that coding standards are a comprehensive, language-specific rules that describe how software code should be written. Coding standards have been developed by industry experts in almost any programming language to help developers write code that is robust and resistant to the most common and damaging errors

- The benefits of coding standards can be seen as the standardization of processes and practices that can increase efficiency, improve productivity, and reduce costs.
  - They increase efficiency By using standards to detect problems earlier or prevent them entirely, your team can increase efficiency throughout the software development process.
  - They reduce costs and the risk of project failure By simply using coding standards and a formal code review process, your team can catch 60 percent of the defects in code (Basili/Boehm 01) and can do so early in the development process.
  - They reduce complexity By using coding standards to define how software code should be written, you can ensure that the code your team develops is free of unnecessary complexity, and that the development process does not lead to additional costs in the future. In addition, you reduce the risk of problems arising during the integration of components developed by different companies, groups, or team members.
  - They prevent hidden costs Whether you&#39;re developing software for internal use or for commercial sale, sub-standard quality can cause your organization to incur additional development costs as you fix errors, redesign the software, provide technical support, refund customer purchases, and lose brand value. While few of these consequences are considered during project planning cycles, they can lead to project delays or cancellations, budget overruns, and losses in market share and revenue.
  - They enable code reuse By enforcing coding standards on every project and every piece of code created, you can ensure that the code is high quality and easy to reuse and extend for other projects.
  - They enable staffing flexibility When all developers working on your code follow coding standards, code is easier to understand, modify, and maintain, whether the developers remain on the same projects over time or move on to other projects.
  - They enable automated error prevention Automated Error Prevention promotes five simple steps, which should be automated whenever possible:

-
  -
    1. Detect an error
    2. Isolate the cause of the error
    3. Locate the point in the process that created the error
    4. Implement practices to prevent the error from reoccurring
    5. Monitor for improvements

Coding standards are an excellent example of an AEP practice because they enable you to implement requirements that prevent the most common and damaging errors in software code.

You can adapt to new standards defined by industry groups or your own team members, adding rules individually or upgrading your automated system to incorporate additional rule groups. This enables you to quickly and easily adapt to new technology needs and continue to prevent errors.

The paper states that the implementation of coding standards enable companies to deliver higher quality software in a manner that is cost-effective and efficient and according to the author using coding standards, costs can be decreased, and productivity improves; however, most importantly, you can automate the prevention of errors throughout the software lifecycle. This not only leads to direct savings in time and cost, but also leads to overall productivity gains that will impact revenue and profitability.

**Making Wrong Code Look Wrong**

This article explains how the implementation of code should be as explicit as can be possible, in such way that if we&#39;re writing code, we should specify when it is supposed to be wrong and it uses as an example the concept of &quot;cleanliness&quot; in a bakery and the way they see things there once they get used to the proper way of doing things and how this is related to coding.

It mentions that when you start out as a beginning programmer or you try to read code in a new language it all looks equally inscrutable. Until you understand the programming language itself you can&#39;t even see obvious syntactic errors.

It talks about general XSS vulnerabilities on web applications and two possible solutions, but at the end it shows the real solution which is to use variables with explicit prefixes that state which ones are safe or unsafe strings. The general rule that it is mentioned in the business of making **wrong code look wrong** depends on getting the right things close together in one place on the screen. The author mentions that when he&#39;s looking at a string, in order to get the code right, he needs to know, everywhere he sees that string, whether it&#39;s safe or unsafe. He doesn&#39;t want that information to be in another file or on another page that I would have to scroll to. He states that we should be able to see it right there and that means a variable naming convention.

There are a lot of other examples where you can improve code by moving things next to each other. Most coding conventions include rules like:

- Keep functions short.
- Declare your variables as close as possible to the place where you will use them.
- Don&#39;t use macros to create your own personal programming language.
- Don&#39;t use goto.
- Don&#39;t put closing braces more than one screen away from the matching opening brace.

In the second part of the article, the author talks about the Hungarian notation that was invented by Microsoft programmer Charles Simonyi. It is mention that one of the major projects Simonyi worked on at Microsoft was Word; in fact he led the project to create the world&#39;s first WYSIWYG word processor, something called Bravo at Xerox Parc.

According to the author, the systems Hungarian was promulgated far and wide; it is the standard throughout the Windows programming documentation; it was spread extensively by books like Charles Petzold&#39;s Programming Windows, the bible for learning Windows programming, and it rapidly became the dominant form of Hungarian, even inside Microsoft, where very few programmers outside the Word and Excel teams understood just what a mistake they had made.

Eventually, programmers who never understood Hungarian in the first place noticed that the misunderstood subset they were using was Pretty Dang Annoying and Well-Nigh Useless, and they revolted against it. Now, there are still some nice qualities in Systems Hungarian, which help you see bugs. At the very least, if you use Systems Hungarian, you&#39;ll know the type of a variable at the spot where you&#39;re using it. But it&#39;s not nearly as valuable as Apps Hungarian.

But there&#39;s still a tremendous amount of value to Apps Hungarian, in that it increases collocation in code, which makes the code easier to read, write, debug, and maintain, and, most importantly, **it makes wrong code look wrong.**

In conclusion, both readings talk about the quality of our software development process and how we should implement coding standards to begin with and also make sure to make wrong code look wrong, so we can identify errors in a more efficient way and with this, save time, money and headaches.