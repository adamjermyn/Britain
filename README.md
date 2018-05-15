This module allows the usage of British English spellings within Python.
So, for instance, after installing the word ```colour``` may be used in place of ```color``` in Matplotlib scripts.
Note that this module likely entails a significant performance hit so usage except as a joke is not recommended.
Furthermore note that because this works by internally replacing British spellings with American ones before passing commands to the interpreter there may be unintended side effects.
Most notably:
```
print('colour')
```
will result in ```color``` being printed.
Such is the price of corrected spellings.

# Usage:

```
from britain import english
```

# Requirements

Britain requires Python 3.
