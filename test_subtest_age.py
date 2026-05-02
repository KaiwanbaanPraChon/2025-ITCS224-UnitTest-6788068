import unittest
from age import categorize_by_age

class TestCategorizeByAgeSubtest(unittest.TestCase):
    
    def test_child_age(self):
        # Testing all valid ages for Child: 0 through 9
        for age in range(10): 
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Child")
                print(f"{age} is considered as a child.")

    def test_adult_age(self):
        # Testing all valid ages for Adult: 19 through 65
        for age in range(19, 66): 
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Adult")
                print(f"{age} is considered as an adult.")

    def test_golden_age(self):
        # Testing all valid ages for Golden age: 66 through 150
        for age in range(66, 151): 
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Golden age")
                print(f"{age} is considered as a golden age.")

if __name__ == "__main__":
    unittest.main(verbosity=2)