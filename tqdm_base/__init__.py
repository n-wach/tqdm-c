from ._monitor import TMonitor, TqdmSynchronisationWarning
from ._tqdm_pandas import tqdm_pandas
from .cli import main  # TODO: remove in v5.0.0
from .gui import tqdm as tqdm_gui  # TODO: remove in v5.0.0
from .gui import trange as tgrange  # TODO: remove in v5.0.0
from .std import (
    TqdmDeprecationWarning, TqdmExperimentalWarning, TqdmKeyError, TqdmMonitorWarning,
    TqdmTypeError, TqdmWarning, tqdm, trange)
from .version import __version__

__all__ = ['tqdm', 'tqdm_gui', 'trange', 'tgrange', 'tqdm_pandas',
           'tqdm_notebook', 'tnrange', 'main', 'TMonitor',
           'TqdmTypeError', 'TqdmKeyError',
           'TqdmWarning', 'TqdmDeprecationWarning',
           'TqdmExperimentalWarning',
           'TqdmMonitorWarning', 'TqdmSynchronisationWarning',
           '__version__']


def tqdm_notebook(*args, **kwargs):  # pragma: no cover
    """See tqdm_base.notebook.tqdm_base for full documentation"""
    from warnings import warn

    from .notebook import tqdm as _tqdm_notebook
    warn("This function will be removed in tqdm_base==5.0.0\n"
         "Please use `tqdm_base.notebook.tqdm_base` instead of `tqdm_base.tqdm_notebook`",
         TqdmDeprecationWarning, stacklevel=2)
    return _tqdm_notebook(*args, **kwargs)


def tnrange(*args, **kwargs):  # pragma: no cover
    """
    A shortcut for `tqdm_base.notebook.tqdm_base(xrange(*args), **kwargs)`.
    On Python3+, `range` is used instead of `xrange`.
    """
    from warnings import warn

    from .notebook import trange as _tnrange
    warn("Please use `tqdm_base.notebook.trange` instead of `tqdm_base.tnrange`",
         TqdmDeprecationWarning, stacklevel=2)
    return _tnrange(*args, **kwargs)
