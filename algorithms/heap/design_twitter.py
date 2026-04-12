import heapq
from collections import defaultdict, deque
from itertools import count, islice

class Twitter:

    def __init__(self):
        self.timer = count(step=-1)
        self.tweets = defaultdict(deque)
        self.follows = defaultdict(set) 

    def postTweet(self, userId: int, tweetId: int) -> None:
        time = next(self.timer)
        self.tweets[userId].appendleft((time, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        related_users = self.follows[userId] | {userId}
        related_tweets = []
        for id in related_users:
            related_tweets.append(self.tweets[id])
        heap = heapq.merge(*related_tweets)
        return [t for _, t in islice(heap, 10)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
