#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#
from typing import Any, Dict, List


# @lc code=start
from dataclasses import dataclass


@dataclass
class FollowNode:
    user_id: str
    following_nodes: List[Any]


class Twitter:
    post_data = []
    follow_map: Dict[str, FollowNode] = {}

    counter: int = 0

    def __init__(self):
        self.post_data = []
        self.follow_map = {}
        self.counter = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post_data.append(
            {"user_id": userId, "tweet_id": tweetId, "counter": self.counter}
        )
        self.counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self._update_follow_node(userId)

        user_node: FollowNode = self.follow_map[userId]
        following_ids = list(map(lambda x: x.user_id, user_node.following_nodes))

        u_ids = following_ids + [userId]

        return list(
            map(
                lambda x: x["tweet_id"],
                sorted(
                    filter(lambda x: x["user_id"] in u_ids, self.post_data),
                    key=lambda x: -x["counter"],
                ),
            )
        )[:10]

    def _update_follow_node(self, user_id: str):
        if user_id not in self.follow_map:
            self.follow_map[user_id] = FollowNode(user_id, [])

    def follow(self, followerId: int, followeeId: int) -> None:
        self._update_follow_node(followeeId)
        self._update_follow_node(followerId)

        followee_node: FollowNode = self.follow_map[followeeId]
        follower_node: FollowNode = self.follow_map[followerId]

        if followee_node not in follower_node.following_nodes:
            follower_node.following_nodes.append(followee_node)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self._update_follow_node(followeeId)
        self._update_follow_node(followerId)

        followee_node: FollowNode = self.follow_map[followeeId]
        follower_node: FollowNode = self.follow_map[followerId]

        if followee_node in follower_node.following_nodes:
            follower_node.following_nodes.remove(followee_node)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 5)
    twitter.postTweet(1, 3)
    twitter.postTweet(1, 101)
    twitter.postTweet(1, 13)
    twitter.postTweet(1, 10)
    twitter.postTweet(1, 2)
    twitter.postTweet(1, 94)
    twitter.postTweet(1, 505)
    twitter.postTweet(1, 333)
    twitter.postTweet(1, 22)
    twitter.postTweet(1, 11)
    twitter.getNewsFeed(1)

    print(twitter.getNewsFeed(1))
