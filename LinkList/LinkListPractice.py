#!/usr/bin/python
class Node:

    __nextNode = None
    __previousNode = None

    def __init__(self):
        pass

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setNextNode(self, node):
        self.__nextNode = node

    def getNextNode(self):
        return self.__nextNode

    def getPreviousNode(self):
        return self.__previousNode


class LinkList:

    __head = None

    def __init__(self):
        pass

    def add(self, node):

        if self.__head is None:
            self.__head = node
            return

        currentNode = self.__head

        while currentNode.getNextNode() is not None:
            currentNode = currentNode.getNextNode()

        currentNode.setNextNode(node)

    def remove(self, node):

        currentNode = self.__head
        previousNode = None

        while currentNode is not node:
            previousNode = currentNode
            currentNode = currentNode.getNextNode()

        if previousNode is None:
            self.__head = currentNode.getNextNode()
        else:
            previousNode.setNextNode(currentNode.getNextNode())

    def reverseLink(self):

        currentNode = self.__head
        previousNode = None

        while currentNode is not None:
            nextNode = currentNode.getNextNode()
            currentNode.setNextNode(previousNode)
            previousNode = currentNode
            currentNode = nextNode

        self.__head = previousNode


    def displayList(self):

        currentNode = self.__head

        while currentNode is not None:
            print(currentNode.getName())
            currentNode = currentNode.getNextNode()

    def getHead(self):
        return self.__head

n1 = Node("First")
n2 = Node("Second")
n3 = Node("Third")
n4 = Node("Fourth")

linklist = LinkList()

linklist.add(n1)
linklist.add(n2)
linklist.add(n3)
linklist.add(n4)

linklist.reverseLink()
linklist.displayList()
































