import unittest
from commit_astrologer.core import analyze_commit_message, generate_astrological_reading

class TestCoreFunctions(unittest.TestCase):

    def test_analyze_commit_message_fix(self):
        predictions = analyze_commit_message("fix: Corrected a typo")
        self.assertTrue(any("bug" in p.lower() for p in predictions))

    def test_analyze_commit_message_feat(self):
        predictions = analyze_commit_message("feat: Added user authentication")
        self.assertTrue(any("new feature" in p.lower() for p in predictions))

    def test_analyze_commit_message_refactor(self):
        predictions = analyze_commit_message("refactor: Improved database queries")
        self.assertTrue(any("refactor" in p.lower() or "merge conflict" in p.lower() for p in predictions))

    def test_analyze_commit_message_no_match(self):
        predictions = analyze_commit_message("chore: Updated dependencies")
        self.assertTrue(len(predictions) == 1) # Should get a default reading

    def test_generate_astrological_reading(self):
        predictions = ["Prediction 1", "Prediction 2"]
        reading = generate_astrological_reading([predictions])
        self.assertTrue("The Commit Message Astrologer Says..." in reading)
        self.assertTrue("* Prediction" in reading)

    def test_analyze_commit_message_invalid_system(self):
        with self.assertRaises(ValueError):
            analyze_commit_message("test: something", system="invalid_system")

if __name__ == '__main__':
    unittest.main()