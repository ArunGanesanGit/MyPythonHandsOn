import unittest
import cap

class TestCap(unittest.TestCase):

	def test_one_word(self):
		result = cap.cap_text('python')
		self.assertEqual(result, 'Python')

	def test_multi_word(self):
		result = cap.cap_text('all my words')
		self.assertEqual(result, 'All My Words')

if __name__ == '__main__':
	unittest.main()