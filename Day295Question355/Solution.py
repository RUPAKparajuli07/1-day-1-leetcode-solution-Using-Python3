from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        # Initialize variables
        self.timestamp = 0  # Global timestamp to maintain the order of tweets
        self.tweets = defaultdict(list)  # Maps userId to a list of (timestamp, tweetId)
        self.followees = defaultdict(set)  # Maps userId to a set of followees

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.timestamp += 1
        self.tweets[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        # Min-heap to store the 10 most recent tweets
        min_heap = []
        
        # Add user's own tweets
        for time, tweetId in self.tweets[userId]:
            heapq.heappush(min_heap, (time, tweetId))
            if len(min_heap) > 10:
                heapq.heappop(min_heap)

        # Add tweets from followees
        for followee in self.followees[userId]:
            for time, tweetId in self.tweets[followee]:
                heapq.heappush(min_heap, (time, tweetId))
                if len(min_heap) > 10:
                    heapq.heappop(min_heap)

        # Extract tweet IDs from the heap in reverse order (most recent first)
        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap)[1])
        return result[::-1]

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)

# Example usage:
# twitter = Twitter()
# twitter.postTweet(1, 5)
# print(twitter.getNewsFeed(1))  # Output: [5]
# twitter.follow(1, 2)
# twitter.postTweet(2, 6)
# print(twitter.getNewsFeed(1))  # Output: [6, 5]
# twitter.unfollow(1, 2)
# print(twitter.getNewsFeed(1))  # Output: [5]
