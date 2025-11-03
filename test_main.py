# 这是评分文件，不要修改
import sys
import importlib.util
import io
import contextlib

def load_module():
    """动态加载学生模块"""
    try:
        spec = importlib.util.spec_from_file_location("student_module", "main.py")
        student_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(student_module)
        return student_module
    except Exception as e:
        print(f"❌ 导入学生模块失败: {e}")
        return None

def run_main_program():
    """运行学生的主程序并捕获输出"""
    module = load_module()
    if not module:
        return None, "模块加载失败"
    
    # 捕获标准输出
    stdout_capture = io.StringIO()
    with contextlib.redirect_stdout(stdout_capture):
        if hasattr(module, '__name__') and module.__name__ == '__main__':
            # 执行主程序
            module.__name__ = '__not_main__'  # 避免重复执行
        elif hasattr(module, 'main'):
            module.main()
    
    return stdout_capture.getvalue(), None

def test_has_duplicates():
    """测试 has_duplicates 函数"""
    module = load_module()
    if not module or not hasattr(module, 'has_duplicates'):
        print("❌ 未找到 has_duplicates 函数")
        return False
    
    has_duplicates = module.has_duplicates
    
    test_cases = [
        # 无重复测试
        ([], False),            # 空列表
        (, False),           # 单个元素
        ([1, 2, 3], False),     # 无重复整数
        (["a", "b"], False),    # 无重复字符串
        ([1, "1"], False),      # 不同类型无重复
        
        # 有重复测试
        ([1, 1], True),         # 重复整数
        (["a", "a"], True),     # 重复字符串
        ([1.0, 1.0], True),     # 重复浮点数
        ([True, True], True),   # 重复布尔值
        ([None, None], True),   # 重复None
        ([1, 2, 3, 1], True),   # 部分重复
        (["a", "b", "a"], True),# 字符串重复
        
        # 特殊类型测试
        ([, ], False),    # 不同列表对象
        ([{"a":1}, {"a":1}], False),  # 不同字典对象
         # 不同字典对象
        ([1, 1.0], False),      # 不同类型（整数和浮点数）
    ]
    
    passed = 0    ]
    
    passed = 0
    total = len(test_cases)
    
    for test_input, expected in test_cases:
        try:
            result = has_duplicates(test_input)
            if result == expected:
                print(f"✅ 测试通过: {test_input} -> {expected}")
                passed += 1
            else:
                print(f"❌ 测试失败: {test_input}")
                print(f"   预期: {expected} | 实际: {result}")
        except Exception as e:
            print(f"❌ 测试异常: {test_input}")
            print(f"   异常: {            print(f"   异常: {e}")
    
    print(f"\n函数测试结果: {passed}/{total} 通过")
    return passed == total

def test_main_program_output():
    """测试主程序输出"""
    output, error = run_main_program()
    if error:
        print(f"❌ 主程序运行失败: {error}")
        return False
    
    # 预期输出模式
    expected_patterns = [
        r"测试 $$1, 2, 3$$：没有重复元素",
        r"测试 $$1, 2, 2$$：有重复元素",
        r"测试 $$'a', 'b', 'a'$$：有重复元素",
        r"测试 $$$$：没有重复元素"
    ]
    
    passed = True
    for pattern in expected_patterns:
        if not re.search(pattern, output):
            print(f"❌ 主程序输出缺失: {pattern}")
            passed = False
    
    if passed:
        print("✅ 主程序输出测试通过")
    else:
        print(f"实际输出:\n{output}")
    
    return passed

if __name__ == "__main__":
    import re
    
    print("== 函数功能测试 ==")
    func_pass = test_has_duplicates()
    
    print("\n== 主程序输出测试 ==")
    main_pass = test_main_program_output()
_pass = test_main_program_output()
    
    if func_pass and main_pass:
        print("\n🎉 所有测试通过!")
        sys.exit(0)
    else:
        print("\n💥 存在未通过的测试")
        sys.exit(1)
