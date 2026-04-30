from agents.parser_agent import ParserAgent
from agents.test_generator import TestGeneratorAgent

print("🚀 Agentic QA Pipeline Started")

parser = ParserAgent()
generator = TestGeneratorAgent()

# 模拟PRD（需求文档）
prd = "User can login and make payment"

# Step 1: 解析需求
requirements = parser.parse_prd(prd)

# Step 2: 生成测试用例
tests = generator.generate_tests(requirements)

print("✅ Generated Test Cases:")
for t in tests:
    print("-", t)

print("🎯 Pipeline Finished")
