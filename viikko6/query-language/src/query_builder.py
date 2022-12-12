from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

class QueryBuilder():
    def __init__(self, pino = All()):
        self.pino = pino

    def build(self):
        return self.pino

    def playsIn(self, joukkue):
        return QueryBuilder(And(self.pino, PlaysIn(joukkue)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.pino, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.pino, HasFewerThan(value, attr)))

    def oneOf(sefl, q1, q2):
        return QueryBuilder(Or(q1, q2))