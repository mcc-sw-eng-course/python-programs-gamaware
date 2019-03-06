**Best Practices of Peer Code Reviews**

The first reading, which is a whitepaper that describes 11 best practices for efficient, lightweight peer

code review that have been proven to be effective by scientific study and by Smart Bear&#39;s extensive field experience.

These best practices ensure that developers get the most of out of the time spent in code reviews, and like the author says, both from a process and a social perspective, It is definitely a requirement to perform the code reviews in order to be able to start seeing the benefits in the short and long term. In the end, the author states that with the right tools and best-practices, almost all the teams of software developers can peer-review all of its code and find costly bugs before the software even reaches QA.

The practices the author explores are:

1. **Review fewer than 200-400 lines of code at a time**

Developers should review fewer than 200-400 _lines of code (LOC)_ at a time. Beyond that, the ability to find defects diminishes. At this rate, with the review spread over no more than 60-90 minutes, you should get a 70-90% yield; in other words, if 10 defects existed, you&#39;d find 7-9 of them.

1. **Aim for an inspection rate of less than 300-500 LOC/hour.**

Faster is not better. The cisco research shows that to achieve optimal results at an inspection rate of less than 300-500 LOC per hour. Left to their own devices, reviewers&#39; inspection rates will vary widely, even with similar authors, reviewers, files, and review size, in any case, in order, to find the optimal inspection rate, the research team compared defect density with how fast the reviewer went through the code. Again, the general result is not surprising: if you don&#39;t spend enough time on the review, you won&#39;t find many defects.

1. **Take enough time for a proper, slow review, but not more than 60-90 minutes.**

You should never review code for more than 90 minutes at a stretch, also, you should always spend at least five minutes reviewing code even if it&#39;s just one line. Often a single line can have consequences throughout the system.

1. **Authors should annotate source code before the review begins.**

Authors should annotate their source code before the review begins. Annotations guide the reviewer through the changes, showing which files to look at first and defending the reason and methods behind each code modification. These notes are not comments in the code, but rather comments given to other reviewers.

1. **Establish quantifiable goals for code review and capture metrics so you can improve your processes.**

It&#39;s best to start with external metrics, such as &quot;reduce support calls by 20%,&quot; or &quot;halve the percentage of defects injected by development.&quot; This information gives you a clear picture of how your code is doing from the outside perspective, and it should have a quantifiable measure not just a vague &quot;fix more bugs.&quot;

1. **Checklists substantially improve results for both authors and reviewers.**

Checklists are a highly recommended way to find the things you forget to do and are useful for both authors and reviewers. Omissions are the hardest defects to find after all, it&#39;s hard to review something that&#39;s not there. A checklist is the single best way to combat the problem, as it reminds the reviewer or author to take the time to look for something that might be missing.

1. **Verify that defects are actually fixed!**

Use good collaborative review software to track defects found in review. With the right tool, reviewers can log bugs and discuss them with the author. Authors then fix the problems and notify reviewers, and reviewers must verify that the issue is resolved. If you&#39;re going to go to the trouble of finding the bugs, make sure you&#39;ve fixed them all!

1. **Managers must foster a good code review culture in which finding defects is viewed positively.**

The point of software code review is to eliminate as many defects as possible regardless of who &quot;caused&quot; the error, therefore managers should also never use ever buggy code as a basis for negative performance review.

1. **Beware the &quot;Big Brother&quot; effect.**

Metrics should never be used to single out developers, particularly in front of their peers. This practice can seriously damage morale. Managers must continue to foster the idea that finding defects is good, not evil, and that defect density is not correlated with developer ability.

1. **The Ego Effect: Do at least some code review, even if you don&#39;t have time to review it all.**

The &quot;Ego Effect&quot; drives developers to write better code because they know that others will be looking at their code and their metrics. And no one wants to be known as the guy who makes all those junior-level mistakes. The Ego Effect drives developers to review their own work carefully before passing it on to others.

1. **Lightweight-style code reviews are efficient, practical, and effective at finding bugs.**

While several methods exist for lightweight code review, such as &quot;over the shoulder&quot; reviews and reviews by email, the most effective reviews are conducted using a collaborative software tool to facilitate the review. A good lightweight code review tool integrates source code viewing with &quot;chat room&quot; collaboration to free the developer from the tedium of associating comments with individual lines of code.

**Software Inspections**

There are several factors that lead to the undesirable project results in which projects continue to ship late, but one of the major contributors is the lack of _defect removal controls._

Clearly there is economic opportunity to improve both the quality and consequently the return on investment (ROI) for software projects as these costs to remove defects are part of the Cost of Quality, or more significantly the lack of quality, and can represent as much as 65% of total project costs.

**Why Inspections?**

_Inspections are needed to remove software defects at reduced cost_. Inspections enable us to remove defects early in the software life cycle, and it is always cheaper to remove defects earlier than later in the software life cycle. It&#39;s important to note that _Inspections are a way to remove defects at a lower cost, not a way to prevent defects from occurring._

The main objective with Inspections is to reduce the Cost of Quality like mentioned before, by finding and removing defects earlier and at a lower cost.

While some testing will always be necessary, we can reduce the costs of test by reducing the volume of defects propagated to test. We want to use test to verify and validate functional correctness, not for defect removal and associated rework costs. We want to use test to prove the correctness of the product without the high cost of defect removal normally seen in test. Additionally, we want to use test to avoid impacting the users with defective products. So, the problems that must addressed are:

- Defects are injected when software solutions are produced
- Removal of defects in test is costly
- Users are impacted by too many software defects in delivered products

Inspections have clear value independent of any model or standard for software development.

**So Why isn&#39;t Everyone Using Inspections**

The reasons for this vary. The author states that this is partially due to views that Inspections can only be done one way. Another reason for the resistance to Inspections is the view that they are not easy to do well. There are factors, including social and psychological, that we must consider. Management often views Inspections

as an added cost, when in fact Inspections will reduce costs during a project.

**Do Good Programmers Make Defects?**

Good programmers do indeed make defects, and if this is true for good programmers then it must follow for all others in the population of programmers. All programmers can and do want to learn from their injected defects. We will see later in the book how both Inspections and Defect Prevention are natural combined processes for programmers to use, when they are adapted for effective success.

One has to wonder where the worst people go. Most cultures will not easily accept the reality of a natural distribution of capability and talent. It seems to be almost a taboo subject. What we should want to do, and what the SW-CMM enables, is to achieve a higher maturity and improved capability in software processes for all people in an organization

There&#39;s also the distinction between _effectiveness and efficiency_. They are different, and both have business; i.e., economic, value to organizations practicing Inspections.

- **Effectiveness**

Data on the customer-found defects may require a longer period of time to acquire and may never be complete. In some cases, the best we may be able to do is to extrapolate from a shorter period of customer use and assume a ratio for the entire set of defects that remain latent in the product. It can never be precise, but it can be a reasonable calculation. We do not yet have the ability to decisively determine the real number of defects shipped with a product.

- **Efficiency**

Efficiency of Inspections is represented by various cost relationships:

-
  - $ spent / defect found in Inspections
  - $ for Inspections / total project costs; this is a subset of Cost of Quality (COQ) measures
  - $ ratio of cost of finding defects in Inspection to cost of defects found in test and by the customers.
  - hours spent / defect found in Inspections.

The use of the terms effectiveness and efficiency of Inspections including the relationship between them is not consistently applied in the software community. Some of this misinterpretation derives from Fagan&#39;s article where he refers to effectiveness as efficiency. This was because a focus at the time was on costs.

**Will Inspections Ever Become Obsolete?**

The author states that a clear possibility exists for Low-level design and code, but not for all work products. The highest cost for Inspections is in Low-level design, and code, so a reduction in these areas is a good contribution to reducing COQ. I suspect that for requirements and key design documents we will need Inspections for quite some time. For other artifacts such as plans, test cases, documents, I think we will see a reduction in a need for Inspections as we improve the disciplines of the activities for creating these work products through training, processes, and tools.

- There is no reason why programmers should be put into positions of generating 100&#39;s of defects to be found by Inspections.
- And Inspections should not be a requirement to achieve quality and they are not required for all work products.

At the end of the day Inspections can reduce the Cost of Quality (COQ), which today has a benchmark of about 22% in software organizations. That&#39;s a far cry from the 65% still seen in many organizations. Much of this COQ reduction can be attributed to the use of Inspections, so why would any organization not exploit Software Inspections?

In conclusion, both readings talk about the importance of performing code reviews and inspections because they save cost and time. It is also shown with metrics and by scientific studies, how they&#39;re useful, and even though they do not help reduce 100% of the bugs, they definitely help do our work in a better way and to deliver quality products.