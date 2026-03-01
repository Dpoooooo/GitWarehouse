# 案例：对密码强度的自动化测试

import pytest

from Password import validate_password

def test_validate_phone_too_short():
    result, msg = validate_password("abc1234")
    assert result == False
    assert "至少8位" in msg

def test_validate_password_too_long():
    result, msg = validate_password("a" * 20)
    assert result == False
    assert "最多16位" in msg

def test_validate_password_no_digit():
    result, msg = validate_password("abcdefghijkl")
    assert result == False
    assert "至少两种类型" in msg

def test_validate_password_no_letter():
    result, msg = validate_password("1234567890123")
    assert result == False
    assert "至少两种类型" in msg

def test_validate_password_valid():
    result, msg = validate_password("abc123456")
    assert result == True
    assert "中等" in msg

def test_validate_password_with_symbol():
    result, msg = validate_password("!@#$%^&*()")
    assert result == False
    assert "至少两种类型" in msg

def test_validate_password_valid_with_symbol():
    """测试：包含数字、字母、符号的密码应该通过"""
    result, msg = validate_password("Abcd!1234")
    assert result == True
    assert "强" in msg



