class TestGeneratorAgent:
    def generate_tests(self, requirements):
        print("[TestGenerator] Generating test cases...")
        tests = []
        for req in requirements:
            tests.append(f"test_{req['module']}")
        return tests
