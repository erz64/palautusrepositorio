from matchers import *
class QueryBuilder:
    def __init__(self, matcher = All()):
        self._matcher = matcher

    def build(self):
        return self._matcher

    def playsIn(self, team):
        return QueryBuilder(And(self._matcher, PlaysIn(team)))
    
    def hasAtLeast(self, value, attribute):
        return QueryBuilder(And(self._matcher, HasAtLeast(value, attribute)))

    def hasFewerThan(self, value, attribute):
        return QueryBuilder(And(self._matcher, HasFewerThan(value, attribute)))
    
    def oneOf(self, matcher1, matcher2):
        return QueryBuilder(Or(matcher1, matcher2))
