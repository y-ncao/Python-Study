##关于面试

#####1. 跳槽目的:
* GF got a job in SF, so decided to move to a larger city
* Like your company and interested about what your company is doing.

#####2. 工作类型:
* 70% dealing with back-end, including 15% of database work. Mostly Python.
* 30% dealing with front-end, working with Coffeescript or Javascript, html & less.

#####3. 工作内容:
* In Hosting System Support Team, mostly develop and support internal tools. Working full stack.
* Build new quoting tool "Mercury" for our Salse Team. SpineJS in Coffeescript handles the front-end, Tornado in Python handles the back-end, with Oracle Database.
* Develop and deploy scripts in Python and SQL to analyze data and maintain database.
* Day-to-day support issues for internal systems.
* Working closely with our Sales Team to constantly improve and update internal systems for them.

##Detail about Mercury

#####1. Tornado, Python's adv, why python
* RESTful by dispatch file
* Tornado handler receive API call
* Memcached

Can talk about serilization here

* Session & Permission & dispatch file
* Queue engine
* Email engine
* Oracle Database
* Nginx

#####2. SpineJS's adv, why SpineJS. v1.3.2
* MVC - talk about this
* grunt

#####3. Unit Test, TDD, why not
* sinon
* sinon-qunit

* Team leader's decision. Personally, I'm not against doing Unit Test.
* Some people go too far from writing test cases
* Changed to a function will need refactor all test cases
* You think the test case would cover all the mistakes, but not always
* Have limitation, like database(what about back-end pull data from database) and front-end, ui layout

#####4. Libraries:

#####Back-End
* MPS
  sqlio, validation, logger, format, config, dateutil. Wrapper lib for pthon. handy functions.
  sqlio is similar for SQLAlchemy
* ~~Pyxuss~~
* SalesForce
* Memcached

#####Some numbers to show this is not a easy project
* List of modals we have
* Queues
* Two Engines
* Data Size
* Rules
* Main table names
* Users, and no. of roles & permissions

#####A lot of comparing
* Python's pros and cons, and comparing to other programming languages.
* Front-end frame work
* Back-end frame work
* Memcached comparing to other DB

#####Front-End
* LESS
* jquery v 2.1
* Bootstrap v3.2.0
* font-awesome
* moment
* requireJS
* underscoreJS

#####4. My Jobs:
#####Back-End
* Permissions
* Sessions
* Part Catalog with ten thousands of rows of data, stored in Memcached
* Nginx - gzip

#####Front-End
* Add Part
* Part Wiki
* Solutions

#####5. Difficulties:
1. Started from zero and everyone works full-stack
2. The memcache problem
3. Support for different browsers on different OS. Especially on mobile device. Had a problem about memory using on iOS device.

###Questions:
* What do you think is the most challenging part of the work
* What makes the best candidate
* How do you different your product with ...
* Tell me more about your team
* How do you evaluate your company compare to your comnpetitors
* I've learnt a lot about this opportunity from xxxxx, as well as my research. I'd love to hear from you about what you are looking for the best candidate and what are some challenges in this work.
* ...

###References that I follow
* V2EX
* InfoQ
* The Hacker News
* TechCrunch
* Web Design Inspiration
