from filter import Filter
import operator

class Logic(object):
    """
    The main Logical object
    """

    def __init__(self, target1: Filter, target2: Filter = None):
        """
        :param target1: It stands for the first parameter. It can be single Logic procedure
        :param target2: Not necessarily must be given. It stands for logical procedures which has two parameters
        """
        self.target1: Filter = target1
        self.target2: Filter = target2

    def is_pass(self, entity) -> bool:
        raise NotImplementedError()


class AndLogic(Logic):
    def __init__(self, condition1, condition2):
        """
        Both they are Filter objects
        :param condition1: first param
        :param condition2:  second param
        """
        super().__init__(condition1, condition2)
        self._cond1 = condition1
        self._cond2 = condition2

    def is_pass(self, entity) -> bool:
        return self._cond1 and self._cond2


class OrLogic(Logic):
    def __init__(self, condition1, condition2):
        """
        Both they are Filter objects
        :param condition1: first param
        :param condition2:  second param
        """
        super().__init__(condition1, condition2)
        self._cond1 = condition1
        self._cond2 = condition2

    def is_pass(self, entity) -> bool:
        return self._cond1 or self._cond2

class XORLogic(Logic):
    """
    XOR
    """
    def __init__(self, condition1, condition2):
        """
        Both they are Filter objects
        :param condition1: first param
        :param condition2:  second param
        """
        super().__init__(condition1, condition2)
        self._cond1 = condition1
        self._cond2 = condition2

    def is_pass(self, entity) -> bool:
        return operator.xor(self._cond1, self._cond2)


class TrueLogic(Logic):
    def __init__(self, condition):
        """
        Excatly does nothing, we just need it because we use Logic mainly.
        So if no Logic used, in my program I use TrueLogic
        :param condition: Filter
        """
        super().__init__(condition)
        self._cond1 = condition
        # self._cond2 = condition

    def is_pass(self, entity) -> bool:
        return self._cond1
