class Node:
    def __init__(self, url='', prev=None, next=None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:
    def __init__(self, homepage: str):
        self.curNode = Node(url=homepage)

    def visit(self, url: str) -> None:
        newNode = Node(url=url, prev=self.curNode)
        self.curNode.next = newNode
        self.curNode = newNode

    def back(self, steps: int) -> str:
        while self.curNode.prev and steps > 0:
            self.curNode = self.curNode.prev
            steps -= 1
        return self.curNode.url

    def forward(self, steps: int) -> str:
        while self.curNode.next and steps > 0:
            self.curNode = self.curNode.next
            steps -= 1
        return self.curNode.url
