import pytest

# 案例1：手机号验证
def validate_phone(phone):
    if len(phone) != 11:
        return False, "手机号必须是11位"
    if phone[0] != '1':
        return False, "手机号必须 1 开头"
    if phone[1] not in '3456789':
        return False, "手机号格式不正确"
    if not phone.isdigit():
        return False, "手机号只能包含数字"
    return True, "验证通过"

def test_phone_valid():
    result, msg = validate_phone("13553456789")
    assert result == True

def test_phone_invalid_length():
    result, msg = validate_phone("133456789")
    assert result == False
    assert "11位" in msg

