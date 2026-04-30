class ParserAgent:
    def parse_prd(self, text):
        print("[ParserAgent] Parsing PRD...")
        return [
            {"module": "login", "test_point": "valid login"},
            {"module": "payment", "test_point": "successful payment"}
        ]
