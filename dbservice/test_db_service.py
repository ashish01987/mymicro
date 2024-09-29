import unittest
from db_service import app, db, Message

class DBServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Use an in-memory SQLite database for testing
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()
        db.session.add(Message(text="Hello World"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_message(self):
        response = self.app.get('/api/message')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello World', response.data)

if __name__ == '__main__':
    unittest.main()

