##关于面试

####1. 跳槽目的:
* GF got a job in SF, so decided to move to a larger city
* Like your company and interested about what your company is doing.

####2. 工作类型:
* 70% dealing with back-end, including 15% of database work. Mostly Python.
* 30% dealing with front-end, working with Coffeescript or Javascript, html & less.

####3. 工作内容:
* In Hosting System Support Team, mostly develop and support internal tools. I work with other 3 developers making full stack development.

* I work with other 3 developers. We are using Python and Oracle to build a Sales application that connects with Salesforce and we are achieveing that by gathering requirements from sales team directly and build these enhancements right into the application.

* Build new quoting tool for our Salse Team.
  * SpineJS in Coffeescript handles the front-end. MVC framework on the front-end.
  * Tornado in Python handles the back-end, with Oracle Database. REST API on back-end.  
    Use Memecached to reduce the database fetch for 1. data is pretty big 2. data is used very frequently.
* Develop and deploy scripts in Python and SQL to do data analysis and maintain database.  
  Sometimes provide reports from our database to other department. Or use script to fix data integrity problem.
* Day-to-day support issues for internal systems.  
  Become fire fighter, internal user report there's issue for systems that we support, then dive into the systems and find traceback and try to fix.
* Working closely with our Sales Team to constantly improve and update internal systems for them.

####4. Mercury特点
* Provide our sales team a faster, more stable, more flexible platform and give them better user experience.
1. Navisite is the king of customization. Our customer can buy whatever they want in whatever way as long as we have profit on the order. This is the goal for us. To build a tool that won't limit our sales people's creativity.
2. A lot of procedures are data-driven, e.g. some approval rules are just a row of data in our database, we can react very fast if there's any need for us to change the rule, without touching the code base.
3. We work closely with our Sales team and we listen to their feedback and make quick improvements based on their feedback.


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
* Pretty easy to bind model update to backend
* Spine stores and renders everything client-side, communicating with the server asynchronously.
* Coffee

####Reason for Spine
Fits well with our user's workflow.
* Most of the time, user are inputing data and choosing options. Like selecting parts, play with price. Data are changed frequently. We don't want our users wait everytime when they input anything, so doing async is the best solution, where SpineJS is good at.
* User opens up the app, load principle models ahead, and later on do async calls to the back-end. User can't even feel that this app is talking with it's back-end because there's non-block IO.

####Redesign Project
1. Use more popular front-end, like Angular - SpineJS's documentation is neat but not enough, we have been suffered from I found a problem, don't know how to solve, so I asked my teammate who is more focused on the front-end, and helped me with that. After that, I asked him, how did you know that? He said because I had a same problem and I dived into the source code
2. We had to worry too much about security. But since this is internal tool, we think this is not a big problem to us. But we still have to face the problem
3. Too much rely on client side may cause problem. You don't know what the user's browser is, you don't what's user's box's performance. Local storage size and other's system attribute will cause all kinds of headache if you do it too much.
4. We had small team and we didn't use TDD at the beginning.
5. For backend, there are a lot of things that we can improve, like reduce the piping to the front-end, make some of the data fetch loaded later.
6. But not anything we need to redesign. Tornado is pretty good, python web development is pretty good. Maybe get more async funcs on back-end but I cannot come up with a great use case for async.

#####Backbone.js / Ember.js / Angular.js

####MVC
* Model stores the data object. Spine can easily bind model change event with api-call the update on the back-end
* View is the template to be rendered to users.
* Controller controls all the logic. Render Views and modify Model.

####Coffeescript vs Javascript


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
4. Client side rendering will cause more problem
   * Cannot trust user's input, need to validate everything from the front-end.
   * Need to be careful about the render process since it's async. For example, user submit a quote for approval, after clicked submit button, if they close the window immediately, it won't actually submit. So need to move process a bit earlier.

#####6. About Team and Workflow
1. We don't have a QA, we are our own QAs. We don't have a PM but we like grokking the business from the ground up, helping to steer our strategy, and defining and prioritizing our business.
2. Use remedy and redmine as our bug tracker
3. We work in iterative agile way. We wanted to work like Scrum and actually currently my manager's role is almost same as Scrum Master, but since we are in a small team, we are not tight to the sprints.

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
* What are the most important skill set for the job?
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

###Behaviors Question
* Give me some examples that you've worked in the past that show you are a team player.
  * In some way to help to improve the chance to success
  * Work in late to fix a problem.
* Describe a situations that I you use your own judgment or own logic to solve the problem.
* Give me an example of time that you have to become very quick to come up with a solution of a problem.
* How you are motivated? - Give me an example that you are above or beyond call of your duty.
* Give me an example of situation that you positively influenced the actions other people.
* Leadership. What have you done in the situation where you had to get others to agree with your ideas.
* How would you describe a challenging group from which you have to gain cooperation from. You need to get to work together. How to lead them together.
  * Use action. If I work very hard, others see me working hard and will be inspired to work hard as well.

####普适的一个例子

Two month ago, we just released our project to production. Some of our user reporting that they are stucked at the loading bar. There were several users reporting the same problem so we think it's pretty serious and it was already 5:00PM.

So we had a quick conversation about the solution. I ssh to the production box and copied the error log and search for possible error entry. The other one make phone call and write emails to the users and gather more detailed information from them, like screen shot, browser version and OS, also like their name. The other one try to login as them and see if that's a permission related problem or if he can reproduce the problem. The other front-end guy try to figure out if there's possible problem happens during the user loading files.

After all, we found out this was a combination of several stuff.

1. In production database, the data set is larger than our staging database. I didn't serialize one of the data object so that data object failed to store in production memcache. Make the backend call very slow.
2. After serialized the data, still doesn't work because the data is still too big for user's local storage(Depends on the OS. For chrome it works fine on Linux but not for windows chrome. But IE works perfect since it has 10MB) (TWC blocked chrome's console so the user cannot see. We don't do much test on Windows). And also not working one mobile phone and Safari(Didn't test Mac OS stuff).
3. So we first blocked the user's local storage save and make large data object fetched when they need. Make the website back to work.
4. I look table to table/data by data and see if there's anything that we might not use(At the beginning, the front-end guy doesn't know what he might use or not, so I try to reduce as much as possible but there's still some kind of redundancies.)
5. Front-end guy located the data and we discussed the data that really needed. One of the relationship table is too big, so we break that to chunk and make another API call for it.
6. Front-end guy also used gzip to zip the data stored in user's local storage.
7. We did more test on windows browser and Mac OS and iOS devices make sure it works fine.

#####具体收获
1. Production和Staging一定要确定data的大小一样, 最好在做这种release之前refresh staging database to make them sync.
2. Team work, 5 of us we worked until 11 and no one left before we are sure the production is working fine.
3. Test on different platform.
4. When everybody work together, we can make the whole project success. If any of use left early that day, the problem wouldn't solved that quick.

最后再问I hope I've answered that question to your satisfaction?

######[Some Other Tricky Ones](https://www.facebook.com/notes/egyptian-recruiter/are-you-prepared-for-tricky-behavioral-interview-questions/359902444038414)
