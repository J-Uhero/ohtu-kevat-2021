from typing import List
from matchers import And, Not, Or, PlaysIn, HasAtLeast, HasFewerThan

class QueryBuilder:
    def __init__(self, quary=And()):
        self._queries = quary

    def build(self):
        return self._queries
    
    def playsIn(self, team):
        return QueryBuilder(And(PlaysIn(team), self._queries))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(HasAtLeast(value, attr), self._queries))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(HasFewerThan(value, attr), self._queries))
