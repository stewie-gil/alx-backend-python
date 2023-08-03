#!/usr/bin/env python3
""" This module contains the safe_first_element function"""


from typing import Iterable, Any, Optional


def safe_first_element(lst: Iterable[Any]) -> Optional[Any]:
    """ safe_first function"""
    if lst:
        return next(iter(lst))
    else:
        return None
