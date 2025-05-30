Contributing to Mypy
====================

Welcome!  Mypy is a community project that aims to work for a wide
swath of Python users and Python codebases.  If you're trying Mypy on
your Python code, your experience and what you can contribute is
important to the project's success.


Getting started, building, and testing
--------------------------------------

If you haven't already, take a look at the project's README file and
the [Mypy documentation](http://mypy.readthedocs.org/en/latest/), and
try adding type annotations to your file and type-checking it with Mypy.


Discussion
----------

If you've run into behavior in Mypy you don't understand, or you're
having trouble working out a good way to apply it to your code, or
you've found a bug or would like a feature it doesn't have, we want to
hear from you!

Our main forum for discussion is the project's [GitHub issue
tracker](https://github.com/python/mypy/issues).  This is the right
place to start a discussion of any of the above or most any other
topic concerning the project.

We have an IRC channel, `#python-mypy` on irc.freenode.net.  This is
lightly used, but some Mypy core developers are almost always present;
feel free to find us there and we're happy to chat.  Substantive
technical discussion will be directed to the issue tracker.

#### Code of Conduct

Everyone participating in the Mypy community, and in particular in our
issue tracker, pull requests, and IRC channel, is expected to treat
other people with respect and more generally to follow the guidelines
articulated in the [Python Community Code of
Conduct](https://www.python.org/psf/codeofconduct/).


Submitting Changes
------------------

Even more excellent than a good bug report is a fix for a bug, or the
implementation of a much-needed new feature.  We'd love to have your
contributions.

We use the usual GitHub pull-request flow, which may be familiar to
you if you've contributed to other projects on GitHub.  For the mechanics
of it, see [our git and GitHub workflow help page](http://www.mypy-lang.org/wiki/UsingGitAndGitHub),
or [GitHub's own documentation](https://help.github.com/articles/using-pull-requests/).

Anyone interested in Mypy may review your code.  One of the Mypy core
developers will merge your pull request when they think it's ready.
For every pull request, we aim to promptly either merge it or say why
it's not yet ready; if you go a few days without a reply, please feel
free to ping the thread with a new comment.

At present the core developers are (alphabetically):
* David Fisher (@ddfisher)
* Jukka Lehtosalo (@JukkaL)
* Greg Price (@gnprice)
* Guido van Rossum (@gvanrossum)


Preparing Changes
-----------------

Before you begin: if your change will be a significant amount of work
to write, we highly recommend starting by opening an issue laying out
what you want to do.  (This is good advice for all kinds of
open-source projects in general.)  That lets a conversation happen
early in case other contributors disagree with what you'd like to do
or have ideas that will help you do it.

The best pull requests are focused, clearly describe what they're for
and why they're correct, and contain tests for whatever changes they
make to the code's behavior.  As a bonus these are easiest for someone
to review, which helps your pull request get merged quickly!  Standard
advice about good pull requests for open-source projects applies; we
have [our own writeup](http://www.mypy-lang.org/wiki/GoodPullRequest)
of this advice.

See also our [coding conventions](http://www.mypy-lang.org/wiki/CodeConventions) --
which consist mainly of a reference to
[PEP 8](https://www.python.org/dev/peps/pep-0008/) -- for the code you
put in the pull request.

You may also find other pages in the
[Mypy developer guide](http://www.mypy-lang.org/wiki/DeveloperGuides)
helpful in developing your change.


Issue-tracker conventions
-------------------------

We aim to reply to all new issues promptly.  We'll assign a
"milestone" to help us track which issues we intend to get to when,
and may apply "labels" to carry some other information.  Here's what
our milestones and labels mean.

### Milestones

We use GitHub "milestones" (see [our
milestones](https://github.com/python/mypy/milestones)) to roughly
order what we want to do soon and less soon.

This means they represent a combination of priority and scale of work.
Bugs that aren't a huge deal but do matter to users and don't seem
like a lot of work to fix generally go in a near milestone; things
that will take longer may go further out.

Specifically:

* **Numbered milestones** correspond to releases.  These assignments
  are changeable and issues may be moved earlier or later.
  Assignments to further-out milestones are especially likely to
  change.
* Point releases, like 0.x.y when we're already at 0.x.z, generally
  have issues that are less work to tackle and whose user-facing
  impact is small or a bugfix.  Meatier or more radical issues
  generally go to a full "minor" release, like 0.x.0.
* **Future** has other things we don't currently plan to get to anytime
  soon -- akin to "backlog" in some systems.
* **Questions** is for things that aren't yet clearly a thing to
  actually change but rather a user asking a question -- we use the
  issue tracker as the preferred venue for such questions.  These
  might move to a different milestone if after discussion a bug or
  feature request emerges.
* Issues **without a milestone** haven't been triaged.  We aim to
  triage all new issues promptly, but there are some issues from 2015
  and earlier that we haven't yet reviewed for triage since adopting
  these conventions.

### Labels

* **needs discussion**: This issue needs agreement on some kind of
  design before it makes sense to implement it, and it either doesn't
  yet have a design or doesn't yet have agreement on one.
* **feature**, **bug**, **refactoring**: These classify the user-facing
  impact of the change.  Specifically "refactoring" means there should
  be no user-facing effect.
* **duplicate**, **wontfix**: These identify issues that we've closed
  for the respective reasons.
* **priority**, **question**, **postponed**: These labels predate the
  milestone conventions and are deprecated; they should be gone on all
  issues that have been triaged to a milestone.
