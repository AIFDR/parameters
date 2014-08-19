# coding=utf-8
__author__ = 'ismailsunni'
__project_name = 'parameters'
__filename = 'qt4_parameter_factory'
__date__ = '8/19/14'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from qt_widgets.boolean_parameter_widget import BooleanParameterWidget
from qt_widgets.float_parameter_widget import FloatParameterWidget


class Qt4ParameterFactory(object):
    """A factory class that will generate a widget given a parameter."""

    def __init__(self):
        """Constructor."""
        pass


    @staticmethod
    def get_widget(parameter):
        """Create parameter widget from current
        :param parameter: Parameter object.
        :type parameter: BooleanParameter, FloatParameter

        :returns: Widget of given parameter.
        :rtype: BooleanParameterWidget, FloatParameterWidget
        """
        parameter = parameter
        class_name = parameter.__class__.__name__

        if class_name == 'BooleanParameter':
            return BooleanParameterWidget(parameter)
        elif class_name == 'FloatParameter':
            return FloatParameterWidget(parameter)
        else:
            raise TypeError
