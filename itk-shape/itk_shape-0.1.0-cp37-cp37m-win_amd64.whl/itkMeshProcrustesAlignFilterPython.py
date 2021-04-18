# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _Mesh3DProcrustesAlignFilterPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkMeshProcrustesAlignFilterPython
else:
    import _itkMeshProcrustesAlignFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkMeshProcrustesAlignFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkMeshProcrustesAlignFilterPython.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import collections.abc
import itk.itkMeshBasePython
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkPointSetPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.itkCovariantVectorPython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.itkPointPython
import itk.itkVectorContainerPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkContinuousIndexPython
import itk.itkIndexPython
import itk.itkBoundingBoxPython
import itk.itkMapContainerPython
import itk.itkArrayPython

def itkMeshProcrustesAlignFilterMD3MD3_New():
    return itkMeshProcrustesAlignFilterMD3MD3.New()

class itkMeshProcrustesAlignFilterMD3MD3(itk.ITKCommonBasePython.itkProcessObject):
    r"""Proxy of C++ itkMeshProcrustesAlignFilterMD3MD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3___New_orig__)
    Clone = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_Clone)
    SetNumberOfInputs = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_SetNumberOfInputs)
    SetInput = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_SetInput)
    GetInput = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_GetInput)
    GetOutput = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_GetOutput)
    GetMean = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_GetMean)
    GetTransform = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_GetTransform)
    GetRotationDegrees = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_GetRotationDegrees)
    PrintTransform = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_PrintTransform)
    GetConvergence = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_GetConvergence)
    SetConvergence = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_SetConvergence)
    SetUseScalingOn = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_SetUseScalingOn)
    SetUseScalingOff = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_SetUseScalingOff)
    SetUseScaling = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_SetUseScaling)
    GetUseScaling = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_GetUseScaling)
    SetUseInitialAverageOn = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_SetUseInitialAverageOn)
    SetUseInitialAverageOff = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_SetUseInitialAverageOff)
    SetUseInitialAverage = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_SetUseInitialAverage)
    GetUseInitialAverage = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_GetUseInitialAverage)
    SetUseNormalizationOn = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_SetUseNormalizationOn)
    SetUseNormalizationOff = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_SetUseNormalizationOff)
    SetUseNormalization = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_SetUseNormalization)
    GetUseNormalization = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_GetUseNormalization)
    SetUseSingleIterationOn = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_SetUseSingleIterationOn)
    SetUseSingleIterationOff = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_SetUseSingleIterationOff)
    SetUseSingleIteration = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_SetUseSingleIteration)
    GetUseSingleIteration = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_GetUseSingleIteration)
    SetAlignRotationOn = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_SetAlignRotationOn)
    SetAlignRotationOff = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_SetAlignRotationOff)
    SetAlignRotation = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_SetAlignRotation)
    GetAlignRotation = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_GetAlignRotation)
    __swig_destroy__ = _itkMeshProcrustesAlignFilterPython.delete_itkMeshProcrustesAlignFilterMD3MD3
    cast = _swig_new_static_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_cast)

    def New(*args, **kargs):
        """New() -> itkMeshProcrustesAlignFilterMD3MD3

        Create a new object of the class itkMeshProcrustesAlignFilterMD3MD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeshProcrustesAlignFilterMD3MD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMeshProcrustesAlignFilterMD3MD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMeshProcrustesAlignFilterMD3MD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMeshProcrustesAlignFilterMD3MD3 in _itkMeshProcrustesAlignFilterPython:
_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_swigregister(itkMeshProcrustesAlignFilterMD3MD3)
itkMeshProcrustesAlignFilterMD3MD3___New_orig__ = _itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3___New_orig__
itkMeshProcrustesAlignFilterMD3MD3_cast = _itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMD3MD3_cast


def itkMeshProcrustesAlignFilterMF3MF3_New():
    return itkMeshProcrustesAlignFilterMF3MF3.New()

class itkMeshProcrustesAlignFilterMF3MF3(itk.ITKCommonBasePython.itkProcessObject):
    r"""Proxy of C++ itkMeshProcrustesAlignFilterMF3MF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3___New_orig__)
    Clone = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_Clone)
    SetNumberOfInputs = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_SetNumberOfInputs)
    SetInput = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_SetInput)
    GetInput = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_GetInput)
    GetOutput = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_GetOutput)
    GetMean = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_GetMean)
    GetTransform = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_GetTransform)
    GetRotationDegrees = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_GetRotationDegrees)
    PrintTransform = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_PrintTransform)
    GetConvergence = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_GetConvergence)
    SetConvergence = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_SetConvergence)
    SetUseScalingOn = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_SetUseScalingOn)
    SetUseScalingOff = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_SetUseScalingOff)
    SetUseScaling = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_SetUseScaling)
    GetUseScaling = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_GetUseScaling)
    SetUseInitialAverageOn = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_SetUseInitialAverageOn)
    SetUseInitialAverageOff = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_SetUseInitialAverageOff)
    SetUseInitialAverage = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_SetUseInitialAverage)
    GetUseInitialAverage = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_GetUseInitialAverage)
    SetUseNormalizationOn = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_SetUseNormalizationOn)
    SetUseNormalizationOff = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_SetUseNormalizationOff)
    SetUseNormalization = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_SetUseNormalization)
    GetUseNormalization = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_GetUseNormalization)
    SetUseSingleIterationOn = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_SetUseSingleIterationOn)
    SetUseSingleIterationOff = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_SetUseSingleIterationOff)
    SetUseSingleIteration = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_SetUseSingleIteration)
    GetUseSingleIteration = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_GetUseSingleIteration)
    SetAlignRotationOn = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_SetAlignRotationOn)
    SetAlignRotationOff = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_SetAlignRotationOff)
    SetAlignRotation = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_SetAlignRotation)
    GetAlignRotation = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_GetAlignRotation)
    __swig_destroy__ = _itkMeshProcrustesAlignFilterPython.delete_itkMeshProcrustesAlignFilterMF3MF3
    cast = _swig_new_static_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_cast)

    def New(*args, **kargs):
        """New() -> itkMeshProcrustesAlignFilterMF3MF3

        Create a new object of the class itkMeshProcrustesAlignFilterMF3MF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeshProcrustesAlignFilterMF3MF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMeshProcrustesAlignFilterMF3MF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMeshProcrustesAlignFilterMF3MF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMeshProcrustesAlignFilterMF3MF3 in _itkMeshProcrustesAlignFilterPython:
_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_swigregister(itkMeshProcrustesAlignFilterMF3MF3)
itkMeshProcrustesAlignFilterMF3MF3___New_orig__ = _itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3___New_orig__
itkMeshProcrustesAlignFilterMF3MF3_cast = _itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMF3MF3_cast


def itkMeshProcrustesAlignFilterMSS3MSS3_New():
    return itkMeshProcrustesAlignFilterMSS3MSS3.New()

class itkMeshProcrustesAlignFilterMSS3MSS3(itk.ITKCommonBasePython.itkProcessObject):
    r"""Proxy of C++ itkMeshProcrustesAlignFilterMSS3MSS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3___New_orig__)
    Clone = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_Clone)
    SetNumberOfInputs = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_SetNumberOfInputs)
    SetInput = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_SetInput)
    GetInput = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_GetInput)
    GetOutput = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_GetOutput)
    GetMean = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_GetMean)
    GetTransform = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_GetTransform)
    GetRotationDegrees = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_GetRotationDegrees)
    PrintTransform = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_PrintTransform)
    GetConvergence = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_GetConvergence)
    SetConvergence = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_SetConvergence)
    SetUseScalingOn = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_SetUseScalingOn)
    SetUseScalingOff = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_SetUseScalingOff)
    SetUseScaling = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_SetUseScaling)
    GetUseScaling = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_GetUseScaling)
    SetUseInitialAverageOn = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_SetUseInitialAverageOn)
    SetUseInitialAverageOff = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_SetUseInitialAverageOff)
    SetUseInitialAverage = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_SetUseInitialAverage)
    GetUseInitialAverage = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_GetUseInitialAverage)
    SetUseNormalizationOn = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_SetUseNormalizationOn)
    SetUseNormalizationOff = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_SetUseNormalizationOff)
    SetUseNormalization = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_SetUseNormalization)
    GetUseNormalization = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_GetUseNormalization)
    SetUseSingleIterationOn = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_SetUseSingleIterationOn)
    SetUseSingleIterationOff = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_SetUseSingleIterationOff)
    SetUseSingleIteration = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_SetUseSingleIteration)
    GetUseSingleIteration = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_GetUseSingleIteration)
    SetAlignRotationOn = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_SetAlignRotationOn)
    SetAlignRotationOff = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_SetAlignRotationOff)
    SetAlignRotation = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_SetAlignRotation)
    GetAlignRotation = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_GetAlignRotation)
    __swig_destroy__ = _itkMeshProcrustesAlignFilterPython.delete_itkMeshProcrustesAlignFilterMSS3MSS3
    cast = _swig_new_static_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_cast)

    def New(*args, **kargs):
        """New() -> itkMeshProcrustesAlignFilterMSS3MSS3

        Create a new object of the class itkMeshProcrustesAlignFilterMSS3MSS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeshProcrustesAlignFilterMSS3MSS3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMeshProcrustesAlignFilterMSS3MSS3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMeshProcrustesAlignFilterMSS3MSS3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMeshProcrustesAlignFilterMSS3MSS3 in _itkMeshProcrustesAlignFilterPython:
_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_swigregister(itkMeshProcrustesAlignFilterMSS3MSS3)
itkMeshProcrustesAlignFilterMSS3MSS3___New_orig__ = _itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3___New_orig__
itkMeshProcrustesAlignFilterMSS3MSS3_cast = _itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMSS3MSS3_cast


def itkMeshProcrustesAlignFilterMUC3MUC3_New():
    return itkMeshProcrustesAlignFilterMUC3MUC3.New()

class itkMeshProcrustesAlignFilterMUC3MUC3(itk.ITKCommonBasePython.itkProcessObject):
    r"""Proxy of C++ itkMeshProcrustesAlignFilterMUC3MUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_Clone)
    SetNumberOfInputs = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_SetNumberOfInputs)
    SetInput = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_SetInput)
    GetInput = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_GetInput)
    GetOutput = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_GetOutput)
    GetMean = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_GetMean)
    GetTransform = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_GetTransform)
    GetRotationDegrees = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_GetRotationDegrees)
    PrintTransform = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_PrintTransform)
    GetConvergence = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_GetConvergence)
    SetConvergence = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_SetConvergence)
    SetUseScalingOn = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_SetUseScalingOn)
    SetUseScalingOff = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_SetUseScalingOff)
    SetUseScaling = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_SetUseScaling)
    GetUseScaling = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_GetUseScaling)
    SetUseInitialAverageOn = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_SetUseInitialAverageOn)
    SetUseInitialAverageOff = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_SetUseInitialAverageOff)
    SetUseInitialAverage = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_SetUseInitialAverage)
    GetUseInitialAverage = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_GetUseInitialAverage)
    SetUseNormalizationOn = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_SetUseNormalizationOn)
    SetUseNormalizationOff = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_SetUseNormalizationOff)
    SetUseNormalization = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_SetUseNormalization)
    GetUseNormalization = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_GetUseNormalization)
    SetUseSingleIterationOn = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_SetUseSingleIterationOn)
    SetUseSingleIterationOff = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_SetUseSingleIterationOff)
    SetUseSingleIteration = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_SetUseSingleIteration)
    GetUseSingleIteration = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_GetUseSingleIteration)
    SetAlignRotationOn = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_SetAlignRotationOn)
    SetAlignRotationOff = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_SetAlignRotationOff)
    SetAlignRotation = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_SetAlignRotation)
    GetAlignRotation = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_GetAlignRotation)
    __swig_destroy__ = _itkMeshProcrustesAlignFilterPython.delete_itkMeshProcrustesAlignFilterMUC3MUC3
    cast = _swig_new_static_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_cast)

    def New(*args, **kargs):
        """New() -> itkMeshProcrustesAlignFilterMUC3MUC3

        Create a new object of the class itkMeshProcrustesAlignFilterMUC3MUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeshProcrustesAlignFilterMUC3MUC3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMeshProcrustesAlignFilterMUC3MUC3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMeshProcrustesAlignFilterMUC3MUC3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMeshProcrustesAlignFilterMUC3MUC3 in _itkMeshProcrustesAlignFilterPython:
_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_swigregister(itkMeshProcrustesAlignFilterMUC3MUC3)
itkMeshProcrustesAlignFilterMUC3MUC3___New_orig__ = _itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3___New_orig__
itkMeshProcrustesAlignFilterMUC3MUC3_cast = _itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUC3MUC3_cast


def itkMeshProcrustesAlignFilterMUS3MUS3_New():
    return itkMeshProcrustesAlignFilterMUS3MUS3.New()

class itkMeshProcrustesAlignFilterMUS3MUS3(itk.ITKCommonBasePython.itkProcessObject):
    r"""Proxy of C++ itkMeshProcrustesAlignFilterMUS3MUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_Clone)
    SetNumberOfInputs = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_SetNumberOfInputs)
    SetInput = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_SetInput)
    GetInput = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_GetInput)
    GetOutput = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_GetOutput)
    GetMean = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_GetMean)
    GetTransform = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_GetTransform)
    GetRotationDegrees = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_GetRotationDegrees)
    PrintTransform = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_PrintTransform)
    GetConvergence = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_GetConvergence)
    SetConvergence = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_SetConvergence)
    SetUseScalingOn = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_SetUseScalingOn)
    SetUseScalingOff = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_SetUseScalingOff)
    SetUseScaling = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_SetUseScaling)
    GetUseScaling = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_GetUseScaling)
    SetUseInitialAverageOn = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_SetUseInitialAverageOn)
    SetUseInitialAverageOff = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_SetUseInitialAverageOff)
    SetUseInitialAverage = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_SetUseInitialAverage)
    GetUseInitialAverage = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_GetUseInitialAverage)
    SetUseNormalizationOn = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_SetUseNormalizationOn)
    SetUseNormalizationOff = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_SetUseNormalizationOff)
    SetUseNormalization = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_SetUseNormalization)
    GetUseNormalization = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_GetUseNormalization)
    SetUseSingleIterationOn = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_SetUseSingleIterationOn)
    SetUseSingleIterationOff = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_SetUseSingleIterationOff)
    SetUseSingleIteration = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_SetUseSingleIteration)
    GetUseSingleIteration = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_GetUseSingleIteration)
    SetAlignRotationOn = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_SetAlignRotationOn)
    SetAlignRotationOff = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_SetAlignRotationOff)
    SetAlignRotation = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_SetAlignRotation)
    GetAlignRotation = _swig_new_instance_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_GetAlignRotation)
    __swig_destroy__ = _itkMeshProcrustesAlignFilterPython.delete_itkMeshProcrustesAlignFilterMUS3MUS3
    cast = _swig_new_static_method(_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_cast)

    def New(*args, **kargs):
        """New() -> itkMeshProcrustesAlignFilterMUS3MUS3

        Create a new object of the class itkMeshProcrustesAlignFilterMUS3MUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeshProcrustesAlignFilterMUS3MUS3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMeshProcrustesAlignFilterMUS3MUS3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMeshProcrustesAlignFilterMUS3MUS3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMeshProcrustesAlignFilterMUS3MUS3 in _itkMeshProcrustesAlignFilterPython:
_itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_swigregister(itkMeshProcrustesAlignFilterMUS3MUS3)
itkMeshProcrustesAlignFilterMUS3MUS3___New_orig__ = _itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3___New_orig__
itkMeshProcrustesAlignFilterMUS3MUS3_cast = _itkMeshProcrustesAlignFilterPython.itkMeshProcrustesAlignFilterMUS3MUS3_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def mesh_procrustes_align_filter(*args,  number_of_inputs: int=..., convergence: float=..., use_scaling: bool=..., use_initial_average: bool=..., use_normalization: bool=..., use_single_iteration: bool=..., align_rotation: bool=...,**kwargs):
    """Functional interface for MeshProcrustesAlignFilter"""
    import itk

    kwarg_typehints = { 'number_of_inputs':number_of_inputs,'convergence':convergence,'use_scaling':use_scaling,'use_initial_average':use_initial_average,'use_normalization':use_normalization,'use_single_iteration':use_single_iteration,'align_rotation':align_rotation }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] != ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.MeshProcrustesAlignFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def mesh_procrustes_align_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.Mesh3DProcrustesAlignFilter.MeshProcrustesAlignFilter
    mesh_procrustes_align_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    mesh_procrustes_align_filter.__doc__ = filter_object.__doc__




