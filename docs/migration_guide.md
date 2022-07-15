# Migration Guide

This guide outlines how to convert existing code based on legacy PyTrinamic (<0.2.0) to newer versions.  

Also check out the new [examples](https://github.com/trinamic/PyTrinamic/tree/master/examples).
For almost all examples that were published for legacy PyTrinamic, new examples are provided.

## Imports

All imports now use PyTrinamic in lowercase letters.

PyTrinamic < 0.2.0:

```py
import PyTrinamic
from PyTrinamic.version import __version__
```

Now:

```py
import pytrinamic
from pytrinamic.version import __version__
```


## Shorter Import Paths

We introduced shorter imports.

PyTrinamic < 0.2.0:

```py
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1160.TMCM_1160 import TMCM_1160
```

Now:

```py
from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM1160
```

## Module Naming

All modules now use snake_case naming convention.

PyTrinamic < 0.2.0:

```py
from PyTrinamic.TMCL import ...
```

Now
```py
from pytrinamic.tmcl import ...
```

## Class Naming

All classes now use the PascalCase naming convention.
We also removed any underscore in class names.

PyTrinamic < 0.2.0:

```py
module = TMCM_1160(..)
.. = TMCL.TMCL_Command
```

Now:

```py
module = TMCM1160(..)
.. = tmcl.TMCLCommand
```

## Function Naming

All functions now use the snake_case naming convention.

PyTrinamic < 0.2.0:

```py
module.getAxisParameter(TMCM_1160.APs.ActualPosition)
```

Now:

```py
module.get_axis_parameter(TMCM1160._MotorTypeA.AP.ActualPosition)
```
