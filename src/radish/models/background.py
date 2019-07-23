"""
radish
~~~~~~

the root from red to green.  BDD tooling for Python.

:copyright: (c) 2019 by Timo Furrer <tuxtimo@gmail.com>
:license: MIT, see LICENSE for more details.
"""

from radish.models.scenario import Scenario
from radish.models.state import State


class Background(Scenario):
    """Represents a single instance of a Gherkin Background"""

    def __init__(self, short_description: str, path: str, line: int, steps) -> None:
        super().__init__(0, short_description, None, path, line, steps)

        #: Holds the Scenario for which this Background is supposed to run.
        self.scenario = None

    def __repr__(self) -> str:
        return "<Background: '{short_description} with {steps} Steps @ {path}:{line}>".format(
            short_description=self.short_description,
            steps=len(self.steps),
            path=self.path,
            line=self.line,
        )

    def set_scenario(self, scenario):
        """Set the Scenario instance for this Background

        Eventually each Background is run as part of a Scenario.
        The given Scenario will be used to access the execution hierarchy
        and other context sensitive functionalities.
        """
        self.scenario = scenario

    @property
    def state(self):
        """Get the State of this Scenario"""
        for step_state in (s.state for s in self.steps):
            if step_state is not State.PASSED:
                return step_state

        return State.PASSED
