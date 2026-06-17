import heapq

class Twitter:

    def __init__(self):
        self.tweets = [] # [(-time, Id, userId), (-time, Id, userId), ...]
        heapq.heapify(self.tweets)
        self.time = 1

        self.follows = {} # followerId: (followeeId, followeeId, ...)

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweets, (-self.time, tweetId, userId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        tweets_copy = list(self.tweets)
        print(tweets_copy)
        while tweets_copy and len(res) < 10:
            tweet = heapq.heappop(tweets_copy)
            print(tweet)
            if (tweet[2] == userId) or (userId in self.follows and tweet[2] in self.follows[userId]):
                res.append(tweet[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId in self.follows:
            self.follows[followerId].add(followeeId)
        else:
            self.follows[followerId] = {followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId in self.follows:
            if followeeId in self.follows[followerId]:
                self.follows[followerId].remove(followeeId)

