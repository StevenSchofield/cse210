from game.scripting.action import Action
from game.casting.actor import Actor

class MoveActorsAction(Action):
    """The action of moving all actors in a given cast
    """
    def execute(self, cast, script):
        """Executing the action of moving all actors in a given cast
        """
        actors = cast.get_all_actors()
        for i in range(len(actors)):
            actor:Actor = actors[i]
            actor.move_next()
