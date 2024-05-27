# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import sys
import copy

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def goalTest(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
        Given a state, returns available actions.
        Returns a list of actions
        """        
        util.raiseNotDefined()

    def getResult(self, state, action):
        """
        Given a state and an action, returns resulting state.
        """
        util.raiseNotDefined()

    def getCost(self, state, action):
        """
        Given a state and an action, returns step cost, which is the incremental cost 
        of moving to that successor.
        """
        util.raiseNotDefined()

        def getSuccessor(self, actions):
            """
              state: Search state
            For a given state, this should return a list of triples, (successor,
            action, stepCost), where 'successor' is a successor to the current
            state, 'action' is the action required to get there, and 'stepCost' is
            the incremental cost of expanding to that successor.
            """
            util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

class Node:
    """
    Search node object for your convenience.

    This object uses the state of the node to compare equality and for its hash function,
    so you can use it in things like sets and priority queues if you want those structures
    to use the state for comparison.

    Example usage:
    >>> S = Node("Start", None, None, 0)
    >>> A1 = Node("A", S, "Up", 4)
    >>> B1 = Node("B", S, "Down", 3)
    >>> B2 = Node("B", A1, "Left", 6)
    >>> B1 == B2
    True
    >>> A1 == B2
    False
    >>> node_list1 = [B1, B2]
    >>> B1 in node_list1
    True
    >>> A1 in node_list1
    False
    """
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __hash__(self):
        return hash(self.state)

    def __eq__(self, other):
        return self.state == other.state

    def __ne__(self, other):
        return self.state != other.state


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def breadthFirstSearch(problem):
    # Group Homework 1 by Pauravi, Nityanand
    # define node, with state as initial starting state and path cost :0
    node = {'state': problem.getStartState(), 'action': problem.getActions(problem.getStartState()), 'cost': 0}
    # check if goalState is current-state then return bode.
    if problem.goalTest(node['state']):
        return []
    # declare the starting cost as 0
    cost = 0
    # Accessing the QUEUE to implement the FIFO with node , Inserting into Queue
    frontier = util.Queue()
    frontier.push(node)
    # Creating a set variable to hold the explored states to eliminating the same record trace again
    explored = set()

    # Loop until there are elements in the Frontier QUEUE
    while frontier:
        # Popping out the element that newest node
        node = frontier.pop()
        # Marking the state if explored
        explored.add(node['state'])

        # nextNode will be based on actions taken by current node
        nextNode = problem.getActions(node['state'])

        # Iterating through each possible nextNode we have for the current state
        for nextN in nextNode:
            # Creating the next-node state from the parent node
            child = {'state': problem.getResult(node['state'], nextN), 'action': nextN, 'parent': node,
                     'cost': cost}
            # Checking if the nextNode state is present in the explored set, if not then its explored
            if child['state'] not in explored:
                # if current node is goal node then return the path

                if problem.goalTest(child['state']):
                    # Creating ResultPath to store the steps.
                    resultPath = []
                    # Make the current node as the child
                    node = child
                    # Backtrack until we get parent node is root node.
                    while 'parent' in node:
                        # Append the result list with the action taken
                        resultPath.append(node['action'])
                        # Make the node point to the current nodes parent node
                        node = node['parent']
                    # Reversing because the first action to be taken will be in the end of the list
                    resultPath.reverse()
                    # Return resultPath that took us to goal node
                    return resultPath
                # if current is not nextNode continue to push node in frontier.
                frontier.push(child)

    util.raiseNotDefined()
    
def depthFirstSearch(problem): 

    "*** YOUR CODE HERE ***"   
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def iterativeDeepeningSearch(problem):
    """
    Perform DFS with increasingly larger depth. Begin with a depth of 1 and increment depth by 1 at every step.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.goalTest(problem.getStartState()))
    print("Actions from start state:", problem.getActions(problem.getStartState()))

    Then try to print the resulting state for one of those actions
    by calling problem.getResult(problem.getStartState(), one_of_the_actions)
    or the resulting cost for one of these actions
    by calling problem.getCost(problem.getStartState(), one_of_the_actions)

    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
    
def UniformCostSearch(problem):
    """Search the node that has the lowest path cost first."""
    "*** YOUR CODE HERE ***"  
    util.raiseNotDefined()
    

def aStarSearch(problem, heuristic=nullHeuristic):
    # Group Homework 1 by Pauravi, Nityanand
    startNode = problem.getStartState()
    # Check if the current state is the goal state. If it is, return.
    if problem.goalTest(startNode):
        return []
    # Use Priority Queue to create Current Path
    currentpath = util.PriorityQueue()
    # Defining a list to store all the visited nodes/places
    explored = []
    # Defining a result list, which store the result path
    result = []
    # Using Priority queue to store all the possible actions at every stage
    priorityQueue = util.PriorityQueue()
    # adding into the queue
    priorityQueue.push(startNode, 0)
    # Positon of current node determined by the queue
    currentNode = priorityQueue.pop()
    # Loop until the current node is the goal node
    while not problem.goalTest(currentNode):
        # Check if the current node visited ?
        if currentNode not in explored:
            # Since its visited now, append current node into explored
            explored.append(currentNode)
            # At this node, get all the possible actions, eg - North, South, East, West
            action = problem.getActions(currentNode)

            # For each action possible, calculate the Pathcost
            for A in action:
                # Since this node is a possible path to the goal, add it to result list
                nextnode = result + [A]
                # Calculate the Pathcost so that the nodes visited will have the priorities assigned based on Heuristic
                Pathcost = problem.getCostOfActions(nextnode) + heuristic(problem.getResult(currentNode, A), problem)
                # Explore only if the node is not visited before
                if A not in explored:
                    # Append the possible actions at each stage queue along with the corresponding Path cost
                    priorityQueue.push(problem.getResult(currentNode, A), Pathcost)
                    currentpath.push(nextnode, Pathcost)
        # Remove form queue as the current node is already visited.
        currentNode = priorityQueue.pop()
        # Store only the element with lower Pathcost rest pop element out
        result = currentpath.pop()
    return result

    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
astar = aStarSearch
ids = iterativeDeepeningSearch
