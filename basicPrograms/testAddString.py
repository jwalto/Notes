def AddString(one, two):
    if one is not None and two is not None:
        return  one + two
    elif one is None and isinstance(two, str):
        return ""
    elif two is None and isinstance(one, str):
        return ""
    else:
        return None

def test_AddString():
    assert AddString(None, None) == None
    assert AddString("","") == ""
    assert len(AddString("","")) == len("") + len("")
    assert AddString(None,"") == ""
    assert AddString("",None) == ""
    try:
        AddString(1, 'one')
        assert False
    except TypeError:
        assert True
    assert AddString('hello','world') == 'helloworld'


test_AddString()