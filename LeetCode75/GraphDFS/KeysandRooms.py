class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        all_rooms = set(list(range(1, len(rooms))))
        stack = rooms[0]

        while len(stack) > 0 and len(all_rooms) > 0:
            room = stack.pop()
            if room in all_rooms:
                all_rooms.remove(room)
                stack.extend(rooms[room])

        return len(all_rooms) == 0