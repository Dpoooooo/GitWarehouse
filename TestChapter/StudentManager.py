# 案例：学生成绩管理系统


class StudentManager:
    """学生成绩管理系统"""
    def __init__(self):
        """初始化"""
        # 用字典存储学生信息
        # 格式：{学号：{"name": 姓名, "scores":[成绩列表]}}
        self.stu = {}

    def add_student(self, student_id, name , scores):
        """添加学生
            参数：
                student_id: 学号（字符串）
                name: 姓名（字符串）
                age: 年龄（int）
                scores: 成绩列表（列表，如[85，90，80])
            返回：
                成功返回True，失败抛出异常
        """
        # 检查学号是否已存在
        if student_id in self.stu:
            raise ValueError(f"学号{student_id}已存在")

        # 检查成绩是否为空
        if not scores:
            raise ValueError("成绩不能为空")

        # 检查成绩是否都是数字
        for score in scores:
            if not isinstance(score, (int, float)):
                raise ValueError("成绩必须是数字")
            if score < 0 or score > 100:
                raise ValueError("成绩必须在0—100之间")

        # 添加学生
        self.stu[student_id] = {
            "name": name,
            "scores": scores
        }
        return True

    def get_student(self, student_id):
        """查询学生信息
            参数：
                student_id:学号
            返回：
                学生信息字典，如果不存在返回None
        """
        return self.stu.get(student_id)

    def delete_student(self, student_id):
        """删除学生
            参数：
                student_id:学号
            返回：
                成功返回True，学生不存在抛出异常
        """
        if student_id not in self.stu:
            raise ValueError(f"学号{student_id}不存在")
        del self.stu[student_id]
        return True

    def get_average(self, student_id):
        if student_id not in self.stu:
            raise ValueError(f"学号{student_id}不存在")
        scores = self.stu[student_id]["scores"]
        average = sum(scores) / len(scores)
        return round(average, 2)

    def get_grade(self, student_id):
        average = self.get_average(student_id)
        if average >= 90:
            return "优秀"
        elif average >= 80:
            return "良好"
        elif average >= 60:
            return "及格"
        else:
            return "不及格"

    def get_all_students(self):
        return self.stu

    def get_students_count(self):
        return len(self.stu)



# 测试
if __name__ == "__main__":
    s = StudentManager()
    print("=" * 50)
    print("学生成绩管理系统")
    print("=" * 50)

    # 测试1：添加多个学生
    print("\n【测试1】添加学生")
    s.add_student("001","金",[88,77,96])
    s.add_student("002","张三",[67,55,66])
    s.add_student("003","李四",[98,76,50])
    s.add_student("004","王五",[61,43,54])
    print(f"成功添加4名学生，当前学生总是：{s.get_students_count()}")

    # 测试2：查询学生信息
    print("\n【测试2】查询学生信息")
    student = s.get_student("001")
    print(f"学号001的学习：{student}")

    # 测试3：计算平均分
    print("\n【测试3】计算平均分")
    avg1 = s.get_average("001")
    avg2 = s.get_average("002")
    avg3 = s.get_average("003")
    avg4 = s.get_average("004")
    print(f"金的平均分：{avg1}")
    print(f"张三的平均分：{avg2}")
    print(f"李四的平均分：{avg3}")
    print(f"王五的平均分：{avg4}")

    # 测试4：获取等级
    print("\n【测试4】获取等级")
    grade1 = s.get_grade("001")
    grade2 = s.get_grade("002")
    grade3 = s.get_grade("003")
    grade4 = s.get_grade("004")
    print(f"金的等级：{grade1}")
    print(f"张三的等级：{grade2}")
    print(f"李四的等级：{grade3}")
    print(f"王五的等级：{grade4}")

    # 测试5：获取所有学生
    print("\n【测试5】获取所有学生")
    all_students = s.get_all_students()
    for student_id , info in all_students.items():
        avg = s.get_average(student_id)
        grade = s.get_grade(student_id)
        print(f"学号：{student_id}, 姓名：{info['name']}, "
              f"成绩：{info['scores']}, 平均分：{avg}, 等级：{grade}")

    # 测试6：删除学生
    print("\n【测试6】删除学生")
    s.delete_student("004")
    print(f"删除王五后，当前学生总数：{s.get_students_count()}")

    # 测试7：异常测试
    print("\n【测试7】异常测试")
    try:
        s.add_student("003" , "重复学号" , [80,85,90])
    except ValueError as e:
        print(f"预期错误：{e}")
    try:
        s.get_average("999")
    except ValueError as e:
        print(f"预期错误：{e}")

    print("\n" + "=" * 50)
    print("所以测试完成！")
    print("=" * 50)






