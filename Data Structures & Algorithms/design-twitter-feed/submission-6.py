from collections import defaultdict
class Twitter:

    def __init__(self):
        self.users_ids = set()
        self.users_tweets = defaultdict(list) # id -> their tweets
        self.users_followers = defaultdict(set) # id -> id
        self.tp = 0
        
    def new_user(self, user_id) -> bool:
        return not user_id in self.users_ids

    def postTweet(self, userId: int, tweetId: int) -> None:
        if self.new_user(userId):
            self.users_ids.add(userId)
            self.users_followers[userId].add(userId)

        self.users_tweets[userId].append([self.tp, tweetId])
        self.tp += 1
        

    def getNewsFeed(self, userId: int) -> Lisst[int]:
        max_heap = []
        for follow_id in self.users_followers[userId]:
            for tp, tweet in self.users_tweets[follow_id][-10:]:
                heapq.heappush(max_heap, [tp, tweet])
                if len(max_heap) > 10:
                    heapq.heappop(max_heap)

        return [heapq.heappop(max_heap)[1] for _ in range(len(max_heap))][::-1]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.users_followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId in self.users_followers[followerId]:
            self.users_followers[followerId].remove(followeeId)
        
