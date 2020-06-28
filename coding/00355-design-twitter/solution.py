# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from collections import deque


class Twitter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cap = 10
        self.timer = 0
        # uid -> set([uid])
        self.follows = {}
        # uid -> deque([(tid, timer)])
        self.tweets = {}

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.timer += 1
        if userId not in self.tweets:
            self.tweets[userId] = deque([(tweetId, self.timer)])
        else:
            user_tweets = self.tweets[userId]
            user_tweets.append((tweetId, self.timer))
            if len(user_tweets) > self.cap:
                user_tweets.popleft()

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        user_follows = {userId}
        if userId in self.follows:
            user_follows |= self.follows[userId]
        tweets = []
        for uid in user_follows:
            if uid in self.tweets:
                tweets.extend(self.tweets[uid])
        tweets = sorted(tweets, key=lambda t: t[1], reverse=True)
        return map(lambda t: t[0], tweets[:self.cap])

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.follows:
            self.follows[followerId].add(followeeId)
        else:
            self.follows[followerId] = {followeeId}

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.follows:
            self.follows[followerId] -= {followeeId}


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
