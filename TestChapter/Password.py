# 案例：对密码强度的验证
import pytest

def validate_password(password):
    """验证密码"""
    # 第1个检查：长度
    if len(password) < 8:
        return False, "密码至少8位"
    if len(password) > 16:
        return False, "密码最多16位"

    has_digit = False
    has_letter = False
    has_symbol = False

    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.isalpha():
            has_letter = True
        else:
            has_symbol = True

    type_count = sum([has_digit, has_letter, has_symbol])
    if type_count < 2:
        return False, "密码必须包含至少两种类型"

    if type_count == 2:
        strength = "中等"
    elif type_count == 3:
        strength = "强"
    else:
        strength = "弱"

    return True, f"验证通过，密码强度：{strength}"


"""
 # 第2个检查：是否包含数字
 has_digit = False
 for char in password:
     if char.isdigit():
         has_digit = True
         break
 # 第3个检查：是否包含字母
 has_letter = False
 for char in password:
     if char.isalpha():
         has_letter = True
         break
 if not has_digit:
     return False,"密码必须包含数字"
 if not has_letter:
     return False,"密码必须包含字母"
 return True, "验证通过"
"""

# 测试
# print(validate_password("abc"))
# print(validate_password("abcdefghijkl"))
# print(validate_password("12334455678"))
# print(validate_password("abcd1234"))
# print(validate_password("a" * 20))





