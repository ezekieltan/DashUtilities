import pytest
from lib_DashUtilities import DashUtilities as du
import pandas as pd

listCombos = [
    (
        None, {'x':'y'}, True, {'head':'h'}, {'tail':'t'}, {'x':'y'}, 
        [{'label': 'h', 'value': 'head'}, {'label': 'y', 'value': 'x', 'disabled': True}, {'label': 't', 'value': 'tail'}]
    ),
    (
        None, {'x':'y'}, True, {'head':'h'}, {'tail':'t'}, ['x'], 
        [{'label': 'h', 'value': 'head'}, {'label': 'y', 'value': 'x', 'disabled': True}, {'label': 't', 'value': 'tail'}]
    ),
    (
        None, {'x':'y'}, True, {'head':'h'}, {'tail':'t'}, 123, 
        [{'label': 'h', 'value': 'head'}, {'label': 'y', 'value': 'x'}, {'label': 't', 'value': 'tail'}]
    ),
    (
        None, {'x':'y'}, True, {'head':'h'}, {'tail':'t'}, [], 
        [{'label': 'h', 'value': 'head'}, {'label': 'y', 'value': 'x'}, {'label': 't', 'value': 'tail'}]
    ),
    (
        None, {'x':'y'}, False, {'head':'h'}, {'tail':'t'}, {'x':'y'}, 
        [{'label': 'y', 'value': 'x', 'disabled': True}]
    ),
    (
        None, {'x':'y'}, False, {'head':'h'}, {'tail':'t'}, ['x'], 
        [{'label': 'y', 'value': 'x', 'disabled': True}]
    ),
    (
        None, {'x':'y'}, False, {'head':'h'}, {'tail':'t'}, 123, 
        [{'label': 'y', 'value': 'x'}]
    ),
    (
        None, {'x':'y'}, False, {'head':'h'}, {'tail':'t'}, [], 
        [{'label': 'y', 'value': 'x'}]
    ),
    (
        None, {}, True, {'head':'h'}, {'tail':'t'}, {'head':'head'}, 
        [{'label': 'h', 'value': 'head', 'disabled': True}, {'label': 't', 'value': 'tail'}]
    ),
    (
        None, {}, True, {'head':'h'}, {'tail':'t'}, ['head'], 
        [{'label': 'h', 'value': 'head', 'disabled': True}, {'label': 't', 'value': 'tail'}]
    ),
    (
        None, {}, True, {'head':'h'}, {'tail':'t'}, 123, 
        [{'label': 'h', 'value': 'head'}, {'label': 't', 'value': 'tail'}]
    ),
    (
        None, {}, True, {'head':'h'}, {'tail':'t'}, [], 
        [{'label': 'h', 'value': 'head'}, {'label': 't', 'value': 'tail'}]
    ),
    (
        None, {}, False, {'head':'h'}, {'tail':'t'}, {'head','head'}, 
        []
    ),
    (
        None, {}, False, {'head':'h'}, {'tail':'t'}, ['head'], 
        []
    ),
    (
        None, {}, False, {'head':'h'}, {'tail':'t'}, 123, 
        []
    ),
    (
        None, {}, False, {'head':'h'}, {'tail':'t'}, [], 
        []
    ),
    (
        {'x':'y'}, {}, False, {}, {}, {'x':'y'}, 
        [{'label': 'y', 'value': 'x', 'disabled': True}]
    ),
    (
        {'x':'y'}, {}, False, {}, {}, ['x'], 
        [{'label': 'y', 'value': 'x', 'disabled': True}]
    ),
    (
        {'x':'y'}, {}, False, {}, {}, 123, 
        [{'label': 'y', 'value': 'x'}]
    ),
    (
        {'x':'y'}, {}, False, {}, {}, [], 
        [{'label': 'y', 'value': 'x'}]
    ),
    (
        {'x':'y'}, {}, False,  {'head':'h'}, {'tail':'t'}, [], 
        [{'label': 'h', 'value': 'head'}, {'label': 'y', 'value': 'x'}, {'label': 't', 'value': 'tail'}]
    ),
]

@pytest.mark.parametrize('a,b,c,d,e,f,g',listCombos)
def test_generateList(a,b,c,d,e,f,g):
    assert du.generateList(input = a, empty = b , extraIfEmpty = c, head = d, tail = e, disabled = f)==g
    
iterableCombos = [
    ([],[]),
    ({},[]),
    (pd.Series(), []),
    (['a'],[{'label': 'a', 'value': 'a'}]),
    ({'k':'v'},[{'label': 'v', 'value': 'k'}]),
    (pd.Series({'k': 1}), [{'label': 1, 'value': 'k'}]),
]

@pytest.mark.parametrize('a,b',iterableCombos)
def test_processIterables(a,b):
    assert du.processIterable(a)==b
    
emptyCombos = [
    ([],True),
    ({},True),
    (pd.Series(), True),
    (['a'],False),
    ({'k':'v'},False),
    (pd.Series({'k': 1}), False),
    (123, False),
]

@pytest.mark.parametrize('a,b',emptyCombos)
def test_isEmpty(a,b):
    assert du.isEmpty(a)==b
    