from typing import List

# 841. 钥匙和房间

# 有 N 个房间，开始时你位于 0 号房间。每个房间有不同的号码：0，1，2，...，N-1，并且房间里可能有一些钥匙能使你进入下一个房间。
# 在形式上，对于每个房间 i 都有一个钥匙列表 rooms[i]，每个钥匙 rooms[i][j] 由 [0,1，...，N-1] 中的一个整数表示，其中 N = rooms.length。 钥匙 rooms[i][j] = v 可以打开编号为 v 的房间。
# 最初，除 0 号房间外的其余所有房间都被锁住。
# 你可以自由地在房间之间来回走动。
# 如果能进入每个房间返回 true，否则返回 false。
class Solution:
    # 深度优先搜索
    # 可以使用深度优先搜索的方式遍历整张图，统计可以到达的节点个数，并利用数组 \textit{vis}vis 标记当前节点是否访问过，以防止重复访问。
    # 时间复杂度：O(n+m)O(n+m)，其中 nn 是房间的数量，mm 是所有房间中的钥匙数量的总数。
    # 空间复杂度：O(n)O(n)，其中 nn 是房间的数量。主要为栈空间的开销。
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        roomsNum = len(rooms)
        if roomsNum == 0:
            return True
        roomStatus = [0 for n in range(roomsNum)]
        roomStatus[0] = 1
        self.openRoom(self, roomStatus, rooms, 0)
        for room in roomStatus:
            if room == 0:
                return False
        return True
    
    def openRoom(self,roomStatus:List[int],rooms: List[List[int]], roomNum:int):
        for key in rooms[roomNum]:
            if roomStatus[key] == 1:
                continue
            roomStatus[key] = 1
            self.openRoom(self,roomStatus, rooms, key)

rooms = [[1,3],[3,0,1],[2],[0]]
self = Solution
print(self.canVisitAllRooms(self, rooms))