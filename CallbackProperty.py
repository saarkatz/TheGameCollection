class _CallbackData:
    """Data class for callback variables"""
    def __init__(self, value, *callbacks):
        self.value = value
        self.cblist = list(callbacks)  # TODO: Maybe change to OrderedSet to guaranty no repeated and ordered execution.

    def add_callback(self, callback):
        """Add a callback function to the callback iterable.
        :param callback: The callback function to add to the list.
        :type callback: func(any)
        """
        self.cblist.append(callback)
        return True

    def remove_callback(self, callback):
        """Remove one callback matching the given callback. Returns true is successful.
        :param callback: The callback function to remove from the list.
        :type callback: func(any)
        """
        if callback in self.cblist:
            self.cblist.remove(callback)
            return True
        return False

    def clear_callbacks(self):
        """Remove all the assigned callbacks"""
        self.cblist.clear()
        return True


class CallbackProperty(property):
    """This property adds a callback mechanism for changes in the specified variable"""
    def __init__(self, name, *callbacks):
        """Initialize the property object.
        This should be called in the Class scope and executed once for each variable when the class in initialized.
        :param name: The name of the variable that would be encapsulated by the property.
        :type name: str
        :param callbacks: Callback arguments to initialize an instance with.
        :type callbacks: func(any)
        """
        name = '_' + name

        def getter(self):
            """The getter function of the property"""
            return getattr(self, name).value

        def setter(self, value):
            """The setter function of the property"""
            # Initial setting
            if name not in dir(self):
                setattr(self, name, _CallbackData(value, *callbacks))
            # Happy flow
            else:
                cbdata = getattr(self, name)
                for cb in cbdata.cblist:
                    cb(value)
                cbdata.value = value

        super().__init__(getter, setter)


class AdvancedCallbackProperty(property):
    """This property adds a callback mechanism for changes in the specified variable with advanced parameters in the
    callbacks"""
    def __init__(self, name, *callbacks):
        """Initialize the property object.
        This should be called in the Class scope and executed once for each variable when the class in initialized.
        :param name: The name of the variable that would be encapsulated by the property.
        :type name: str
        :param callbacks: Callback arguments to initialize an instance with.
        :type callbacks: func(any)
        """
        _name = '_' + name

        def getter(self):
            """The getter function of the property"""
            return getattr(self, _name).value

        def setter(self, value):
            """The setter function of the property"""
            try:
                cbdata = getattr(self, _name)
            except AttributeError:
                # TODO: Organize exceptions
                raise Exception('The property "{0}" was not initialized! Call the _init_{0} method before the first use'
                                ' of {0}, preferably at the beginning of __init__.'.format(name))
            for cb in cbdata.cblist:
                params = ('value', 'self', 'prev')
                parameters = cb.__code__.co_varnames
                values = []
                for var in parameters:
                    if params[0] == var:
                        values.append(value)
                    elif params[1] == var:
                        values.append(self)
                    elif params[2] == var:
                        values.append(cbdata.value)
                    else:
                        raise NameError('The parameter \'{0}\' is not a supported advanced parameter! ({1})'
                                        .format(var, ', '.join(params)))
                cb(*values)
            cbdata.value = value

        super().__init__(getter, setter)


# The variable var_name will become a property implementing callbacks in the setattr function.
# The real name of the variable will become _{var_name} and will be an encapsulating _CallbackData object. The get the
# value of the variable use {obj}._{var_name}.value though it is not advised to meddle with the internal of the
# callback mechanism as you might cause exceptions, not knowing what you're doing.
# When overriding a property by calling make_callback in a subclass, the callbacks initialized on the super class will
# be overridden by new callbacks in the call to make_callback.
def make_callback(var_name, *callbacks, advanced_params=False):
    """Class decorator to initialize a variable to support the callback mechanism.
    This function also creates two additional functions for the management of the callbacks of the variable. These are
    {var_name}_add_callback(callback) - Adds a callback to the variable
    {var_name}_remove_callback(callback) - Tries to remove a callback from the variable. Raises ValueError if the
    callback is not present.
    {var_name}_clear_callbacks - Clears all the callbacks assigned to the property.

    The property need to be initialized in the __init__ function by calling the special function
    _init_(var_name} - Initializes the property. This does not however calls the callbacks.

    You should assign the variable in the __init__ function. Any callbacks added before the assignment will be
    called.

    Be careful when overriding callback properties.

    :param var_name: The name of the variable.
    :type var_name: str
    :param callbacks: Callbacks to initialize the property with.
    :type callbacks: func(any)
    :param advanced_params: True to indicate that callbacks should use the advanced parameter passing should be used.
    :type advanced_params: bool
    :return: The class cls
    """
    # TODO: Clear the documentation.
    _var_name = '_' + var_name

    # This function initializes the property and should be called in the __init__ function of the class
    def _init_property(self):
        setattr(self, _var_name, _CallbackData(None, *callbacks))
    _init_property.__name__ = '_init_' + var_name
    _init_property.__doc__ = """This function initializes '{0}' and should be called in the __init__ function of the
     class.
    """.format(var_name)

    # TODO: These two functions might be recreating the variable name on every call here.
    # Functions for adding callback
    def add_callback(self, callback, *callbacks):
        getattr(self, _var_name).add_callback(callback)
        for cb in callbacks:
            getattr(self, _var_name).add_callback(cb)
    add_callback.__name__ = var_name + '_add_callback'
    add_callback.__doc__ = """Add callback to the property {0}.
        :param callback: The callback to add.
        :type callback: func(any)
        :param callbacks: Additional callbacks to add.
        :type callbacks: func(any)
        """.format(var_name)

    # Function for removing callback
    def remove_callback(self, callback, *callbacks):
        getattr(self, _var_name).remove_callback(callback)
        for cb in callbacks:
            getattr(self, _var_name).remove_callback(cb)
    remove_callback.__name__ = var_name + '_remove_callback'
    remove_callback.__doc__ = """Try to remove a callback from the property {0}. Raises ValueError if the callback
    is not present.
    :param callback: The callback to remove.
    :type callback: func(any)
    :param callbacks: Additional callbacks to remove.
    :type callbacks: func(any)
    """.format(var_name)

    def clear_callbacks(self):
        getattr(self, _var_name).clear_callbacks()
    remove_callback.__name__ = var_name + '_clear_callbacks'
    remove_callback.__doc__ = """Clear all the callbacks assigned to the property {0}.""".format(var_name)


    def class_decorator(cls):
        # Set the property
        if advanced_params:
            setattr(cls, var_name, AdvancedCallbackProperty(var_name, *callbacks))
        else:
            setattr(cls, var_name, CallbackProperty(var_name, *callbacks))
        # Set the init function
        setattr(cls, _init_property.__name__, _init_property)
        # Set the callback functions
        setattr(cls, add_callback.__name__, add_callback)
        setattr(cls, remove_callback.__name__, remove_callback)
        return cls
    return class_decorator
