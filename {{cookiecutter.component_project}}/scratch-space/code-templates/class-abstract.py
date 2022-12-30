# Remember to import abc!

class AbstractClassName(metaclass=abc.ABCMeta):
    """TODO: Document the class.
    Provides baseline functionality, interface requirements, and
    type-identity for objects that can REPRESENT_SOMETHING
    """

    ###################################
    # Class attributes/constants      #
    ###################################

   # _property_name = None

    ###################################
    # Property-getter methods         #
    ###################################

    # @property
    # def property_name(self) -> str:
    #     return self._property_name

    ###################################
    # Property-setter methods         #
    ###################################

    # @property_name.setter
    # def property_name(self, value:str) -> None:
    #     # TODO: Type- and/or value-check the value argument of the
    #     #       setter-method, unless it's deemed unnecessary.
    #     self._property_name = value

    ###################################
    # Property-deleter methods        #
    ###################################

    # @property_name.deleter
    # def _del_property_name(self) -> None:
    #     self._property_name = None

    ###################################
    # Instance property definitions   #
    ###################################

#     abstract_property = abc.abstractproperty()

    ###################################
    # Object initialization           #
    ###################################

    # TODO: Add and document arguments if/as needed
    def __init__(self):
        """
        Object initialization.
        self .............. (AbstractClassName instance, required) The
                             instance to execute against
        """
        # - Call parent initializers if needed
        # - Set default instance property-values using _del_... methods
        # - Set instance property-values from arguments using
        #   _set_... methods
        # - Perform any other initialization needed
        pass # Remove this line

    ###################################
    # Object deletion                 #
    ###################################

    ###################################
    # Abstract methods                #
    ###################################

#     @abc.abstractmethod
#     def instance_method(self, arg:str, *args, **kwargs):
#         """TODO: Document method
#         DOES_WHATEVER
#
#         self .............. (AbstractClassName instance, required) The
#                             instance to execute against
#         arg ............... (str, required) The string argument
#         *args ............. (object*, optional) The arglist
#         **kwargs .......... (dict, optional) keyword-args, accepts:
#          - kwd_arg ........ (type, optional, defaults to SOMETHING) The SOMETHING
#                             to apply
#        """
#         pass

    ###################################
    # Instance methods                #
    ###################################

#     def instance_method(self, arg:str, *args, **kwargs):
#         """TODO: Document method
#         DOES_WHATEVER
#
#         self .............. (AbstractClassName instance, required) The
#                             instance to execute against
#         arg ............... (str, required) The string argument
#         *args ............. (object*, optional) The arglist
#         **kwargs .......... (dict, optional) keyword-args, accepts:
#          - kwd_arg ........ (type, optional, defaults to SOMETHING) The SOMETHING
#                             to apply
#         """
#         pass

    ###################################
    # Overrides of built-in methods   #
    ###################################

    ###################################
    # Class methods                   #
    ###################################

    ###################################
    # Static methods                  #
    ###################################