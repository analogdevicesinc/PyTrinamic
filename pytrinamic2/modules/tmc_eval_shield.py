class TmcEvalShield:
    """
    Arguments:
        connection:
            Type: connection interface
            The connection interface used for this module.
        shield:
            Type: class
            The EvalShield class used for every axis on this module.
            For every axis connected, an instance of this class will be created,
            which can be used later.
    """
    def __init__(self, connection, shield, module_id=1):
        self.shields = []

        while not(connection.get_global_parameter(self.GP.AttachedAxes, 0, module_id)):
            pass

        attached_axes = connection.get_global_parameter(self.GP.AttachedAxes, 0, module_id)
        for i in range(attached_axes):
            self.shields.append(shield(connection, i, module_id))

    class GP:
        AttachedAxes = 6
