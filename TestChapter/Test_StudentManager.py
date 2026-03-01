# Test_StudentManager.py
# 学生成绩管理系统自动化测试

import pytest
from StudentManager import StudentManager

# ==================== 测试 add_student ====================

def test_add_student_success():
    """测试：正常添加学生"""
    manager = StudentManager()
    result = manager.add_student("001", "张三", [85, 90, 78])
    assert result == True
    # 验证学生确实被添加了
    student = manager.get_student("001")
    assert student is not None
    assert student["name"] == "张三"

def test_add_student_duplicate():
    """测试：添加重复学号"""
    manager = StudentManager()
    manager.add_student("001", "张三", [85, 90, 78])
    # 再次添加同一学号，应该抛出异常
    with pytest.raises(ValueError) as exc_info:
        manager.add_student("001", "李四", [92, 88, 95])
    assert "已存在" in str(exc_info.value)

def test_add_student_empty_scores():
    """测试：成绩为空"""
    manager = StudentManager()
    with pytest.raises(ValueError) as exc_info:
        manager.add_student("001", "张三", [])
    assert "不能为空" in str(exc_info.value)

def test_add_student_invalid_score_type():
    """测试：成绩包含非数字"""
    manager = StudentManager()
    with pytest.raises(ValueError) as exc_info:
        manager.add_student("001", "张三", [85, "abc", 78])
    assert "必须是数字" in str(exc_info.value)

def test_add_student_score_out_of_range():
    manager = StudentManager()
    with pytest.raises(ValueError) as exc_info:
        manager.add_student("001", "张三", [85, -10, 78])
        assert "0-100" in str(exc_info.value)
    with pytest.raises(ValueError) as exc_info:
        manager.add_student("002", "李四", [85, 110, 78])
        assert "0-100" in str(exc_info.value)

# ==================== 测试 get_student ====================

def test_get_student_exists():
    """测试：查询存在的学生"""
    manager = StudentManager()
    manager.add_student("001", "张三", [85, 90, 78])
    student = manager.get_student("001")
    assert student is not None
    assert student["name"] == "张三"
    assert student["scores"] == [85, 90, 78]

def test_get_student_not_exists():
    """测试：查询不存在的学生"""
    manager = StudentManager()
    student = manager.get_student("999")
    assert student is None

# ==================== 测试 delete_student ====================

def test_delete_student_success():
    """测试：删除存在的学生"""
    manager = StudentManager()
    manager.add_student("001", "张三", [85, 90, 78])
    result = manager.delete_student("001")
    assert result == True
    # 验证学生确实被删除了
    student = manager.get_student("001")
    assert student is None

def test_delete_student_not_exists():
    """测试：删除不存在的学生"""
    manager = StudentManager()
    with pytest.raises(ValueError) as exc_info:
        manager.delete_student("999")
    assert "不存在" in str(exc_info.value)

# ==================== 测试 get_average ====================

def test_get_average_normal():
    """测试：计算平均分"""
    manager = StudentManager()
    manager.add_student("001", "张三", [85, 90, 75])
    avg = manager.get_average("001")
    # (85+90+75)/3 = 83.33
    assert avg == 83.33

def test_get_average_student_not_exists():
    """测试：计算不存在学生的平均分"""
    manager = StudentManager()
    with pytest.raises(ValueError) as exc_info:
        manager.get_average("999")
    assert "不存在" in str(exc_info.value)

# ==================== 测试 get_grade ====================

def test_get_grade_excellent():
    """测试：优秀等级（>=90）"""
    manager = StudentManager()
    manager.add_student("001", "张三", [95, 92, 90])
    grade = manager.get_grade("001")
    assert grade == "优秀"

def test_get_grade_good():
    """测试：良好等级（80-89）"""
    manager = StudentManager()
    manager.add_student("002", "李四", [85, 88, 82])
    grade = manager.get_grade("002")
    assert grade == "良好"

def test_get_grade_pass():
    """测试：及格等级（60-79）"""
    manager = StudentManager()
    manager.add_student("003", "王五", [70, 65, 68])
    grade = manager.get_grade("003")
    assert grade == "及格"

def test_get_grade_fail():
    """测试：不及格等级（<60）"""
    manager = StudentManager()
    manager.add_student("004", "赵六", [50, 45, 55])
    grade = manager.get_grade("004")
    assert grade == "不及格"

def test_get_grade_boundary_90():
    """测试：边界值90分"""
    manager = StudentManager()
    manager.add_student("005", "边界1", [90, 90, 90])
    grade = manager.get_grade("005")
    assert grade == "优秀"

def test_get_grade_boundary_89():
    """测试：边界值89分"""
    manager = StudentManager()
    manager.add_student("006", "边界2", [89, 89, 90])
    # (89+89+90)/3 = 89.33
    grade = manager.get_grade("006")
    assert grade == "良好"

# ==================== 测试 get_student_count ====================

def test_get_student_count_zero():
    """测试：初始学生数为0"""
    manager = StudentManager()
    count = manager.get_students_count()
    assert count == 0

def test_get_student_count_after_add():
    """测试：添加学生后数量变化"""
    manager = StudentManager()
    manager.add_student("001", "张三", [85, 90, 78])
    manager.add_student("002", "李四", [92, 88, 95])
    count = manager.get_students_count()
    assert count == 2

def test_get_student_count_after_delete():
    """测试：删除学生后数量变化"""
    manager = StudentManager()
    manager.add_student("001", "张三", [85, 90, 78])
    manager.add_student("002", "李四", [92, 88, 95])
    manager.delete_student("001")
    count = manager.get_students_count()
    assert count == 1
