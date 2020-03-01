from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy", "you", "anuj"]
graph["alice"] = ["peggy"]
graph["anuj"] = []
graph["peggy"] = ["bob", "you"]
graph["thom"] = []
graph["claire"] = ["thom", "jonny"]
graph["jonny"] = []


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
    return False


search("you")
