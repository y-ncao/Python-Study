##关于面试

####1. 跳槽目的:
* GF got a job in SF, so decided to move to a larger city
* Like your company and interested about what your company is doing.

####2. 工作类型:
* 70% dealing with back-end, including 15% of database work. Mostly Python.
* 30% dealing with front-end, working with Coffeescript or Javascript, html & less.

####3. 工作内容:
* In Hosting System Support Team, mostly develop and support internal tools. Working full stack.
* Build new quoting tool "Mercury" for our Salse Team. SpineJS in Coffeescript handles the front-end, Tornado in Python handles the back-end, with Oracle Database.
* Develop and deploy scripts in Python and SQL to analyze data and maintain database.
* Day-to-day support issues for internal systems.
* Working closely with our Sales Team to constantly improve and update internal systems for them.

##Detail about Mercury

####1. Tornado, Python's adv, why python
* RESTful by dispatch file
* Tornado handler receive API call
* Memcached  
  Can talk about serilization here
* Session & Permission & dispatch file
* Queue engine
* Email engine
* Oracle Database
* Nginx

####2. SpineJS's adv, why SpineJS. v1.3.2
* MVC - talk about this
* grunt

####3. Unit Test, TDD, why not
* sinon
* sinon-qunit  


* Team leader's decision. Personally, I'm not against doing Unit Test
* Some people go too far from writing test cases
* Changed to a function will need refactor all test cases
* You think the test case would cover all the mistakes, but not always
* Have limitation, like database(what about back-end pull data from database) and front-end, ui layout

####4. Libraries:

#####Back-End
* MPS  
  sqlio, validation, logger, format, config, dateutil. Wrapper lib for pthon. handy functions.  
  sqlio is similar for SQLAlchemy.
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

-----

####Memcached
* Default size is 64MB
* Default object size if 1MB
* Very fast
* service memecached restart
* config file /etc/memcached.conf

####RESTful vs SOAP

####Nginx vs Apache2
* __Nginx__ is a http request and load balancing server.  
  Nginx is faster.
* __Apache2__ used to be not good at scale. Had some memory problem.  
  ```sudo nginx -t``` 查看config file 有无错误  
  记住千万不能有两个default server

####Python Back-end Framework Comparison
#####Django (Powerful)
* Perfect documentation
* Full-stack framework - cache, session, feed, [orm](http://stackoverflow.com/questions/53428/what-are-some-good-python-orm-solutions), geo, auth
* MVC on the back end, have the template system
* System functions laid on each other. If you don't like the Django's ORM, hard to use your own.
* Not good at customization.

#####Tornado (Flexible) (Good for Scale)
* We have many libraries in our company. MPS.
* __Non-blocking__ network I/O
* Only provides what a basic web server needs. Like url dispatch

####Reason for Tornado
Tornado is flexible and light weight. Since we are putting all the MVC part to our front-end, we don't need that powerful framework like Django.

#####Flask & Bottle (Nimble) (Not non-blocking so not good for scale)
* Flask + Jinja + SQLAlchemy  
  Framework + Template + ORM

#####[Twisted](http://stackoverflow.com/questions/5458631/whats-so-cool-about-twisted)
* Include a lot of protocols implementation.
* Event-driven networking engine

#####[Blocking and Non-blocking I/O](http://stackoverflow.com/questions/8362794/networked-systems-whats-the-difference-between-a-blocking-and-a-non-blocki)
######Blocking - Synchronous vs Non-blocking - Asynchronous
A "blocking" call "blocks" the program that calls it until it completes. Your program has to wait for it to do (whatever) before the next statement runs.

A "non-blocking" or asynchronous method usually, instead, either deposits its results in a "mailbox" or "queue" of some kind, or (more commonly) will call back a function that you provide when it completes. 

####Javascript Front-end Framework Comparison
#####References
* [CodeBrief](http://codebrief.com/2012/01/the-top-10-javascript-mvc-frameworks-reviewed/)
* [InfoQ](http://www.infoq.com/research/top-javascript-mvc-frameworks/)

#####Spine.js
* MVC
* Asynchronous interfaces
* Simplicity

Spine stores and renders everything client-side, communicating with the server asynchronously.


#####Backbone.js / Ember.js / Angular.js

####MVC
* Model stores the data object. Spine can easily bind model change event with api-call the update on the back-end
* View is the template to be rendered to users.
* Controller controls all the logic. Render Views and modify Model.

####Coffeescript vs Javascript


####Reason for Spine
Fits well with our user's workflow.  
* Most of the time, user are inputing data and choosing options. Like selecting parts, play with price. Data are changed frequently. We don't want our users wait everytime when they input anything, so doing async is the best solution, where SpineJS is good at.
* User opens up the app, load principle models ahead, and later on do async calls to the back-end. User can't even feel that this app is talking with it's back-end because there's non-block IO.

####Grunt
* Javascript task runner, or automation. Helps you to do automated compile, build and test.
* 最重要的两个file: package.json & Gruntfile.js/cofffee

###Bower
* Package Manger. Helps you to manage and update package. Used with Grunt. Like if you have a package update, and tested by team member, grunt-bower will help you to install that package.
* 重要的file: bower.json

###Other Key Words:
* LESS
* Bootstrap
* Salesforce

-----


#####4. My Jobs:
#####Back-End
* Permissions
* Sessions
* Part Catalog with ten thousands of rows of data, stored in Memcached
* Nginx - gzip

#####Front-End
* Add Part Info
* Part Wiki
* Solutions

#####5. Challenges:
1. Started from scratch and everyone works full-stack.
2. The Memcache problem
3. Support for different browsers on different OS. Especially on mobile device. Had a problem about memory using on iOS device.

-----

###Questions:
* What do you think is the most challenging part of the work
* What makes the best candidate
* How do you different your product with ...
* Tell me more about your team
* How do you evaluate your company compare to your comnpetitors
* I've learnt a lot about this opportunity from xxxxx, as well as my research. I'd love to hear from you about what you are looking for the best candidate and what are some challenges in this work.
* ...

闲来没事可以问的问题：
#####Question to HR:
* How would you describe the company culture?
* What type of employees tend to excel at this company?
* Can you tell me more about the interview process?
* How would you describe the work enviroment here—collaborative or independent?

#####Hiring Manager: Your Future Boss
* What is the ideal candidate?
* What are some challenges one might face in this position?
* What are the most important skillset for the job?
* What are the backgrounds of people in the team?
* What's a typical career path at the company for someone in this role?
* If I am luck enough to get the job, what preparation would you suggest me do?
* Learning/training opportunities

#####The Executive or high level expert
* How do you think this industry will change in the next five years?
* What do you think is the competitive advantage of our company?
* What's the company's biggest challenge? How is it planning to meet that challenge?

#####The Coworker
* Could you please describe a typical day?
* How would you describe the work environment at the company?
* Share something about your background.

#####普适的问题：
* What do you particularly like about the company?
* What do you dislike about the company if there is any?
* Could you tell me something about the projects that you are working on? The size of the team. The language the team is adopting?


###References that I follow
* V2EX
* InfoQ
* The Hacker News
* TechCrunch
* Web Design Inspiration
