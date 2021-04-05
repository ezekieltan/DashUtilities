import datetime
import pandas as pd
class DashUtilities:
    __instance__ = None
    def __init__(self):
        if DashUtilities.__instance__ is None:
            DashUtilities.__instance__ = self
        else:
            pass
    @staticmethod
    def getInstance():
        if not DashUtilities.__instance__:
            DashUtilities()
        return DashUtilities.__instance__
    
    
    @staticmethod
    def verticalMarksStyle():
        return {'writing-mode': 'vertical-lr', 'text-orientation': 'sideways'}
    
    
    @staticmethod
    def generateMarks(input, globalStyle = {}, style={}):
        ret = {}
        if isinstance(input, list):
            for x in input:
                ret[x] = {'label': str(x),'style': globalStyle}
        elif isinstance(input, dict):
            for key, value in input.items():
                ret[key] = {'label': str(value),'style': globalStyle}
        for k,v in style.items():
            if k in ret:
                ret[k]['style'] = v
        return ret
    
    @staticmethod
    def generateList(input = None, head = None, tail = None, empty=None, extraIfEmpty = False, disabled = None):
        ret=[]
        inputIsEmpty = DashUtilities.isEmpty(input)
        if(inputIsEmpty):
            if(extraIfEmpty):
                ret = ret + DashUtilities.processIterable(head)
            ret = ret + DashUtilities.processIterable(empty)
            if(extraIfEmpty):
                ret = ret + DashUtilities.processIterable(tail)
        else:
            ret = ret + DashUtilities.processIterable(head)
            ret = ret + DashUtilities.processIterable(input)
            ret = ret + DashUtilities.processIterable(tail)
        finalRet = []
        if(not DashUtilities.isEmpty(disabled)):
            if(isinstance(disabled, dict)):
                disabled = list(disabled.keys())
            if(isinstance(disabled, list)):
                for r in ret:
                    if r['value'] in disabled:
                        finalRet.append(r | {'disabled':True})
                    else:
                        finalRet.append(r)
            else:
                finalRet = ret
        else:
            finalRet = ret
        return finalRet
    @staticmethod
    def isEmpty(input):
        try:
            return input is None or (input is not None and len(input)<=0)
        except TypeError as e:
            return False
    @staticmethod
    def processIterable(input = None):
        ret = []
        if(isinstance(input, list)):
            for v in input:
                ret.append({'label': v, 'value': v})
        elif(isinstance(input, dict)):
            for key, value in input.items():
                ret.append({'label': value, 'value': key})
        elif(isinstance(input, pd.core.series.Series)):
            return DashUtilities.processIterable(input.to_dict())
        return ret
    
    ### Generator methods removed. Use plotly express instead.
    @staticmethod
    def emptyFigure():
        return {'data': [], 'layout': {}}
    @staticmethod
    def placeholderFigure():
        return {'data': [{'x': [2, 3, 4, 5, 6], 'y': [3, 6, 6, 7, 9], 'type': 'line', 'name': ''}], 'layout': {'title': ''}}