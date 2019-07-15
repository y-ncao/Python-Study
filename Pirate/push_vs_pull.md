# Push VS Pull Design in News Feed

## Problem
Push和Pull是两种不同的system design approach,主要应用于feed design或者类似的应用场景例如Live comment.

## Main Differences

### Data Structure Differences
一般来讲, 实现Push和Pull时需要的data structure是不一样的. 以feed design为例, 最naive的feed design是至少需要一个timeline table的, 就是用户所有的post按照chronological order的一个 list.
在Pull model中, 只需实现一个
```python
def getUserFeed(user_id: int, start_at: Optional[int] = None, ..., last_feed_item_id: Optional[int] = None):
    following_list = getFollowingList(user_id)
    feed = []
    for following in following_list:
      recent_posts = getRecentPost(following.user_id)
      if start_at or last_feed_item_id:
        for post in recent_posts:
          if post.timestamp >= start_at and post.id < last_feed_item_id:
            feed.add(post)

    return feed
```
具体这个function中的getRecentPost其实只需要做一个`select * from timeline_table where user_id = user_id`. 于是我们只需要一个`timeline_table`就可以实现pull model了.

对比push model, 需要除了maintain一个`timeline_table`, 还需要maintain一个`news_feed_table` keyed by `feed_owner`, 也就是这个newsfeed reader.

### Process Differences
* Pull approach
    * Distribute actions by writer
    * Write one location(对应`timeline_table`), read gathers(对应每个人的`timeline_table`)
* Push approach
    * Distribute actions by reader
    * Write broadcasts(对应每个人的`news_feed_table`), read one location(对应某个人的`news_feed_table`)

ML ranking应该是发生在 read path.

### Reference
* 九章黄药师 - https://www.jiuzhang.com/qa/2074/
* Facebook architecture slides - http://itsumomono.blogspot.com/2015/07/news-feed-approaches-push-vs-pull.html
