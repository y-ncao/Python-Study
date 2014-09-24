#System Design

####By Tiny URL
1. Constrains and Use Cases
   1. Use Cases - What do we use the system for?
      1. Shortening: take a url => return a much shorter url
      2. Redirection: take a short ulr => redirect to the original url
      3. ~~Custom url~~
      4. ~~Analytics~~
      5. ~~Automatic link expiration~~~
      6. ~~Manual link removal~~
      7. ~~UI vs API~~
      8. Highly available
   2. Constrains:
      1. Basic knowledge:
         * 1.3 Billion Facebook active users
         * 650 Million Twitter
         * New Tweets per day 500 Million
      2. 这道题的数据
         1. All shortened URLs per Month: 1.5BN
         2. Sites below the top3: 300M per month
         3. We: 100M per month
         4. 1BN request per month
         5. request by second   400+per second(40 shorten 360 redirects)
         6. Total url 5 years * 12 * 100M: 6Billion url in 5 years
         7. 每个url长度 500bytes: __1 char = 1 byte__ 这个太重要了(ASCII是128=2**7个, 1byte就够了, 但是UTF-8是1~4bytes一个字符)
         8. __url是case sensitive的__
         9. 6 bytes per hash
         10. 注意, 10^3 K->kb, 10^6 M->MB, 10^9 B->GB, 10^12 ->TB
         11. New data written per second 40*(500+6)bytes = 20kb
         12. Data read per second: 360 * 506 bytes = 180k
      3. 重要的几个点
         1. Storage
         2. Data written & Data Read

2. Abstract Design - Finally simple the problem to per second
   1. Application service layer(serves the requests)
      * Shortening Service
      * Redirection Service
   2. Data storage layer(keep track of the hash =>url mapping)
      * Act like a big hash table: stores new mappings and retrieves a value given a key
   3. ```hashed_url = convert_to_base_62(md5(original_url + random_salt))[:6]```
      * Base 62 是一种short ulr的encoding, encode之后只有62种字符0-9 a-z A-Z
3. Understanding Bottlenecks
   * Traffic - not going to be very hard
   * Lots of data - more interesting
4. Scaling Abstract Design
   1. Application Service Layer
      * Start with one machine
      * Measure how far it take us(load tests)
      * Add a load balancer + a cluster of machines over time
        1. to deal with spiky traffice
        2. Also avoid single failure and increase the availability
   2. Data Storage Layer
      1. What's data?
         * Billions of objects
         * Each object is fairly small(<1k)
         * There are no relationship between the objects
         * Reads are 9x more frequent thant writes(360 reads, 40 writes per second)
         * 3TBs of urls, 36GB of hashes
      2. NoSQL vs Relation SQL
         * MySQL:
           * Widely used
           * Mature technology
           * Clear Scaling Paradimgs(sharding, master/slave replication, master/master replication)
           * Used by Facebook, Twitter, Google etc
           * Index lookups are very fast
         * Mappings
           * hash: varchar(6)
           * original_url: varchar(512)
      3. Create a unique index on the hash(36GB+). We want to hold it in memory to speed up lookups.
         1. Vertical Scaling of the MySQL machine (memory is cheap) (vertical for a while)
         2. Partition the data: 5 partitions, 600GB of data, 8GB of indexes (Eventually partiion)
            * We can add more shards in the future. Easier for backup and replicate
            * Default idea of this is: get the first char from the ```hash % num_of_partition```
      4. Master/Slave replication(reading from the slave replicas, writes to the master)(如果有一天read/write不balance了的话) Master/Master

------

####总结:
1. 从base开始, 最后变得复杂, 可以一开始vertical, 后面horizontal
2. 核心是从连个方向走
   * Traffic
     1. More server(应该是这里体现consistent hashing, map reduce可能也是这里)
     2. Load balancer
   * Data
     1. NoSQL vs Relation SQL
     2. 如果小的话就store in memory, 大的话就得考虑sharding(easier for replicate and backup)
     3. 如果读写不均匀的话就分开读写, master/slave replication(reading from slaves and write to master)

####数字
* 一个char是1 byte, 一个int/float/long是4 bytes, 一个double是 8 bytes
* 1 Million = 10^6, 1 Million char = 1MB, 1 Million int = 4MB, 1 Million double = 8MB
* 1 Billion = 10^9, 1 Billion char = 1GB, 1 Billion int = 4GB, 1 Million double = 8GB
* 综上所述，假设8G电脑很普通，一般来说如果不提memory size的话无论什么type都能放下，如果说了memory size就要对比下了
* We choose quicksort over mergesort as mergesort requires O(n) space. Quicksort uses O(logn) space.
* MD5 digest size 128 bits = 16 bytes
* SHA-1 digest size 160 bits = 20 bytes
* Max Email address = 254 char = 254 bytes

| Things| 1 | 1 Thousand(2^10) | 1 Million(2^20) | 1 Billion(2^30) |
| :---: | ---: | ---: | ---: | ---: |
| byte | byte | KB | MB | GB |
| char | 1 byte | 1 KB | 1 MB | 1 GB |
| int/float/long | 4 byte | 4 KB | 4 MB | 4 GB |
| double | 8 byte | 8 KB | 8 MB | 8 GB |
| MD5 | 128 bits = 16 bytes| 16 KB | 16 MB | 16 GB |
| SHA-1 | 160 bits = 20 bytes | 20 KB | 20 MB | 20 GB |
| Email | 254 chars = 254 bytes | 254 KB | 254 MB | 254 GB |
| IP Address(IPv4) | 2**8 * 4 = 4 bytes | 4 KB | 4 MB | 4 GB |
| IP Address(IPv6) | 128 bits = 16 bytes | 16 KB | 16 MB | 16 GB |


#####Note
1. 所有IP是能放进内存的，因为一共2^32个ip地址


------

####From [Harvard Class](https://www.youtube.com/watch?v=-W9F__D3oY4)
1. 形式: Multi-tier architecture
![Multi-tier architecture](./img/arch-anganguera.png)
![Another Pic](./img/perfpatrol.png)

2. 重要的几个东东西
   1. DNS - 可以通过DNS来进行geo based load balancing, ```nslookup google```
   2. Firewall - 只允许来自80 443 22 VPN端口的访问. 过了下面那层LB，把443转换成80就行了
     * [Principle of Least Privilege](http://en.wikipedia.org/wiki/Principle_of_least_privilege)
   3. Load Balancer
     * 分为软的和硬的  
       Software - Elastic Load Balancing, HAProxy(TCP/HTTP), Linux Virtual Server  
       Hardware - Barracuda, Cisco, Citrix, F5
     * 方法  
       Round robin 平均分配  
       Weighted round robin  
       Least connections  
       Least response time  
       Layer 7 load balancers can further distribute requests based on application specific data such as HTTP headers, cookies, or data within the application message itself, such as the value of a specific parameter.
     * Heart Beat health check
       * Active/Active - 意味着run full capacity, 如果一个跪了，整体的load balancing速度会降低
       * [Active/passive](http://www.loadbalancerblog.com/blog/2013/01/understanding-active-passive-activeactive-load-balancing)
     * ip-hash 根据ip造server
   4. Web Server
     * 可以partition，按照某种方法处理request(例如名字)
   5. 在Web Server和Storage之间还可能要有一层Load Balancer
   6. Switch - 每个server在联入网的时候都是有两个switch，需要调节好防止packet在中间形成loop
   7. Storage
     * NoSQL vs Relational SQL
     * Raid0, Raid1, Raid5, Raid6, Raid10
     * Master/Slave Mode (重点是replica)  
       一个Master多个Slave, 内容一样，如果Master跪了可以promote一个Slave  
       分开读写，Master写，Slave读，实时同步(好像有点点SPF)
     * Master/Master Mode  
       两个Master多个Slave, 就不会跪了

------

###NoSQL vs Relational SQL
* NoSQL
  * MongoDB(Document)
  * Google Big Table (Column)
  * Cassandra (Column)
  * HBase (Column)
  * Amazon DynamoDB(Key-Value Eventually Consistent)
  * Redis(Key-Value RAM)
  * MemcacheDB(Key-Value RAM)
* Eventually Consistent
* Pros:
  * Scalable
  * Flexible
  * It’s Administrator-Friendly
  * It’s Cost-Effective and Open-Source
  * The Cloud’s the Limit
* Cons:
  * A General Lack of Maturity
  * Performance and Scaling > Consistency - Performance and Scaling is good, lack of Consistency

###[Sharding](http://docs.mongodb.org/manual/core/sharding-introduction/)
* Storing data across multiple machines
* Purpose - horizontal scaling
* Advantages
  * Sharding reduces the number of operations each shard handles
  * Sharding reduces the amount of data that each server needs to store.
* 三个重要的structure
  * __Shards__ store the data
  * __Query Routers__ interface with client applications and direct operations to the appropriate shard or shards
  * __Config servers__ store the cluster’s metadata.
* Data Partitioning
  * Range Based Sharding
  * Hash Based Sharding
* Splitting
* Balancing

###[MapReduce](http://michaelnielsen.org/blog/write-your-first-mapreduce-program-in-20-minutes/)
拿这个link的word count作为栗子
* Map is a step to convert each chapter to a dict  
  * 实际栗子里是把combine这步放到这里，把多个chapter组成一个intermediate list
  * 所以，输入是chapter，输出是list of words with count 1, a lot duplidates
* Reduce is a step to combine each list and reduce the duplicate data
  输入是个list，通过使用itertool.groupby()和dict来实现去重，把intermediate信息输入进去，最后得到一个新的reduced list
* Steps
  1. Partitioning data
  2. Apply function to the pieces in parallel without communication to each other between the analyzers
  3. Apply another function to combine the results

###[Consistent Hashing](http://blog.csdn.net/sparkliang/article/details/5279393)
* Naive way to do: hash(k) % n
* four important keys
  * Balancing
  * Monotonicity
  * Spread
  * Load
* 解决的问题：N个server， 需要增加或者减少一台，但是又不想re-hash
* Steps:
  1. 环形hash空间
  2. 把数据对象Objecthash到环形空间
  3. 把Server hash到环形空间
  4. Map Object to Server：顺时针顺着object的key走遇到的第一个Server负责该object
  5. 分析
     * 移除Server
       Server B被移除后，只需要从B出发逆时针找第一个Server，在此之间的所有object都要re-map到Server B的下一个Server
     * 添加Server
       同样是从新的server逆时针出发到上一个server之间object归他管了
* 通过virtual node来提高balance
* 正常hash就直接hash ip就行了 hash('192.168.1.1')， 如果是hash virtual node可以 hash('192.168.1.1#1')

