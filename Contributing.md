How to contribute
=================

Welcome
-------

Thank you for your interest to contribute to this project!
We appretiate everyone who wants to help!

In this document we collected some information we think you will find useful to get started.

If you have any questions, please feel free to [ask][maintainer]!


Be a nice person
-----------------

We want everyone to feel welcome and be happy at our project. 
That's why we follow the **[Code of Conduct][code_of_conduct]**. 
Please follow it in all your interactions with the project, 
including comments, questions, issues, requests and so on.

How to contribute
-----------------

To keep the code organized, we uses the **[Git Flow branching model][gitflow]**. 
If you never heard Git Flow before, please get familiar with the 
[concept of git flow][gitflow-model].

All development is done using BehaviourDriven Development and TestDriven Development,
when possible.

We use python's unittests to write Unit tests and the behave-module to develop
behaviour tests.

Before you contribute, please contact us and tell us what you want to change!

How to do a pull request
------------------------

1. Open an issue and let us know what you want to change or improve.
   We are excited to discuss your idea with you!
2. [Fork the code][fork] and clone it, then checkout the development branch.
   
   ```git checkout develop```
   
3. Make sure, any existings tests in the test directory are working!
4. Add a new feature branch

   ```git flow feature start MYFEATURE```
   
   or 
   
   ```git checkout -b feature/MYFEATURE develop```
  
5. Write User stories and develop Behaviour Tests and Unit tests 
   to demonstrate what problem whould be solved.
6. Make it work and test it using the tests you wrote in step 3
7. Make a pull request





A word on commit messages: Please keep your commit messages useful by following
some very simple rules about commit messages!

When contributing to this repository, please first discuss the change you wish to make 
via issue with the owners of this repository before making a change.

I'm no programmer. What can I do?
---------------------------------

You don't *have* to be an programmer to contribute. There are many ways to help:

**Help us to optimize future development**

This is very simple! Just download our [tool to provide hardware- and software information][tool]
about your computer. Run the tool and you are done! This will help us focus on hard- and software
which is actual in use instead of get lost in improvments for platforms that do not
exist (any more).

**Help us write or improve documentation for users, so they can learn how to use the software**

Bad documentation frightens users! But it is hard to write good documentation.
We all make mistakes: Typos, explanations that are hard to understand, Formatting errors, 
missing documents or broken links...

You can help us improving our documentation or writing new documentation by joining our
[documentation wiki][documentation].

**Find and report bugs and test software**

If you find a bug, [please let us know][report-bug]!

If you didn't find a bug yet, download a [pre-release][pre-release] to test our new 
features and code. You probably will find something soon. 

**Help to improve the user interface**

Please provide screenshots of our software! This is very helpful for user interface enhancments!
If you are familiar with graphics software or UI Designers, you may want to suggest new
or enhanced user interface concepts!

**Translate the software in your mother tongue**

The more languages, the better!

Please [contact us][translate] if you are interested, especially for the following languages:

> *Arabic, Chinese, English (British), French, German (Switzerland), 
German (Austria), Hindi, Japanese, Korean, Russian*



[tool]: https://github.com/michagrandel/
[documentation]: https://github.com/michagrandel/BackupApi/wiki
[maintainer]: https://github.com/michagrandel/BackupApi/blob/master/Maintainer.md
[code_of_conduct]: https://github.com/michagrandel/BackupApi/blob/master/CodeOfConduct.md
[pre-release]: https://github.com/michagrandel/BackupApi/releases
[report-bug]: https://github.com/michagrandel/BackupApi/issues/new
[translate]: https://github.com/michagrandel/BackupApi/wiki/Translate