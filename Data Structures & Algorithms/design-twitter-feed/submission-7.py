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
        # # if instead we had to return the k most recent post, this would run in: F*K*log(K) which is suboptimal
        # # we can instead break this down into two, 1 by creating a max heap and adding the initial (last) message
        # # for each user that userId follows, we create a min heap on those last messages and then we pop the min one
        # # of all those messages. we keep track of the index of the most recent pop value and decrease it and then we 
        # # we push that value to into the heap again. we continue this process until we get the K most recent values.
        # # this would result in a total complexity of F + K + K*logK
        # max_heap = []
        # for follow_id in self.users_followers[userId]:
        #     for tp, tweet in self.users_tweets[follow_id][-10:]:
        #         heapq.heappush(max_heap, [tp, tweet])
        #         if len(max_heap) > 10:
        #             heapq.heappop(max_heap)

        # return [heapq.heappop(max_heap)[1] for _ in range(len(max_heap))][::-1]

        # K*log K solution:
        res = []
        max_heap = []
        for followee in self.users_followers[userId]: # O(F)
            if followee in self.users_tweets:
                idx = len(self.users_tweets[followee]) - 1
                tp, tweet = self.users_tweets[followee][idx]
                max_heap.append([-tp, tweet, followee, idx])

        heapq.heapify(max_heap) #. O(F)

        while max_heap and len(res) < 10:
            tp, tweet, followee, idx = heapq.heappop(max_heap)
            res.append(tweet)
            if idx -1 >= 0:
                tp, tweet = self.users_tweets[followee][idx-1]
                heapq.heappush(max_heap, [-tp, tweet, followee, idx-1])
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.users_followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId in self.users_followers[followerId]:
            self.users_followers[followerId].remove(followeeId)
        
