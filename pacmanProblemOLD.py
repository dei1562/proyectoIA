from simpleai.search import SearchProblem

GOAL = 'HELLO WORLD'

class PacmanProblem(SearchProblem):

    pacman = 0
    cereza = 0

    def actions(self, state):
        if len(state) < len(GOAL):
            return list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        else:
            return []

    def result(self, state, action):
        return state + action

    def is_goal(self, state):
        return state == GOAL

    def heuristic(self, state):
        # how far are we from the goal?
        wrong = sum([1 if state[i] != GOAL[i] else 0
        for i in range(len(state))])
        missing = len(GOAL) - len(state)
        return wrong + missing