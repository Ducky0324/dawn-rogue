class Action:
    def __init__(self, actor):
        self.actor = actor

    def perform(self):
        pass


class ActionResult:
    def __init__(self, result: bool, action_list: list = [], alt=None):
        self.result = result
        self.actionList = action_list
        self.alt = alt

    def do(self):
        if len(self.actionList) > 0:
            for i in range(len(self.actionList)):
                self.actionList[i]


class Attack(Action):
    def __init__(self, attacker, target):
        super().__init__(attacker)
        self.target = target

    def perform(self):
        return ActionResult(True)


class Walk(Action):
    def __init__(self, actor, stage, direction):
        super().__init__(actor)
        self.stage = stage
        self.direction = direction

    def perform(self):
        nextTile = self.stage.getTile(self.actor.pos + self.direction)
        nextActor = self.stage.getActorAt(self.actor.pos + self.direction)
        if nextActor is not None:
            return ActionResult(result=False, alt=Attack(self.actor, nextActor))
        if nextTile.walkable:
            return ActionResult(
                result=True,
                action_list=[
                    self.stage.moveActor(self.actor, self.direction),
                    self.actor.move(self.direction),
                ],
            )
        return ActionResult(result=False)
