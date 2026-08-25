from typing import List
import heapq


class Twitter:

    def __init__(self):
        # userId -> set of users they follow
        self.following = {}

        # userId -> list of (timestamp, tweetId)
        self.tweets = {}

        # Increasing timestamp
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []

        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        # User always sees their own tweets
        users = self.following.get(userId, set())
        users = list(users) + [userId]

        # Max heap using negative timestamp
        heap = []

        for user in users:
            if user in self.tweets and self.tweets[user]:
                timestamp, tweetId = self.tweets[user][-1]

                # Store:
                # -timestamp
                # user
                # index of tweet
                heapq.heappush(heap, (-timestamp, user, len(self.tweets[user]) - 1))

        result = []

        while heap and len(result) < 10:
            neg_time, user, index = heapq.heappop(heap)

            timestamp, tweetId = self.tweets[user][index]
            result.append(tweetId)

            # Move to the previous tweet from the same user
            if index > 0:
                prev_time, prev_tweet = self.tweets[user][index - 1]

                heapq.heappush(
                    heap,
                    (-prev_time, user, index - 1)
                )

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)