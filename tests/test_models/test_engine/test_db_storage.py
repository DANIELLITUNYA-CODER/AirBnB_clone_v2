#!/usr/bin/python3
''' Module for testing database storage '''

import unittest
import os
import MySQLdb
from datetime import datetime
from models.user import User
from models import storage

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'Database storage test not supported')
class TestDBStorage(unittest.TestCase):
    ''' Testing database storage engine '''

    def setUp(self):
        ''' Set up test environment '''
        self.db_config = {
            'user': os.getenv('HBNB_MYSQL_USER'),
            'host': os.getenv('HBNB_MYSQL_HOST'),
            'passwd': os.getenv('HBNB_MYSQL_PWD'),
            'port': 3306,
            'db': os.getenv('HBNB_MYSQL_DB')
        }
        # Create test database connection
        self.db = MySQLdb.connect(**self.db_config)
        self.cursor = self.db.cursor()

    def tearDown(self):
        ''' Clean up after each test '''
        self.cursor.close()
        self.db.close()

    def test_new_and_save(self):
        ''' Test creating and saving a new user '''
        new_user = User(first_name='John', last_name='Doe', email='john@example.com', password='12345')
        old_count = self._get_user_count()
        new_user.save()
        new_count = self._get_user_count()
        self.assertEqual(new_count, old_count + 1)

    def test_new(self):
        ''' Test creating a new user '''
        new_user = User(first_name='Jane', last_name='Smith', email='jane@example.com', password='password')
        self.assertNotIn(new_user.id, storage.all(User))
        new_user.save()
        self.assertIn(new_user.id, storage.all(User))
        self._check_user_in_database(new_user)

    def test_delete(self):
        ''' Test deleting a user '''
        new_user = User(first_name='Michael', last_name='Brown', email='michael@example.com', password='password')
        new_user.save()
        self.assertIn(new_user.id, storage.all(User))
        new_user.delete()
        self.assertNotIn(new_user.id, storage.all(User))

    def test_reload(self):
        ''' Test reloading the database session '''
        self.cursor.execute("INSERT INTO users(id, created_at, updated_at, email, password, first_name, last_name) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                            ('test_id', datetime.now(), datetime.now(), 'test@example.com', 'test_password', 'Test', 'User'))
        self.db.commit()
        self.assertNotIn('User.test_id', storage.all(User))
        storage.reload()
        self.assertIn('User.test_id', storage.all(User))

    def test_save(self):
        ''' Test saving a user to the database '''
        new_user = User(first_name='Emma', last_name='Davis', email='emma@example.com', password='password')
        old_count = self._get_user_count()
        new_user.save()
        new_count = self._get_user_count()
        self.assertEqual(new_count, old_count + 1)
        self.assertIn(new_user.id, storage.all(User))
        self._check_user_in_database(new_user)

    def _get_user_count(self):
        ''' Helper method to get the count of users in the database '''
        self.cursor.execute("SELECT COUNT(*) FROM users")
        return self.cursor.fetchone()[0]

    def _check_user_in_database(self, user):
        ''' Helper method to check if user exists in the database '''
        self.cursor.execute("SELECT * FROM users WHERE id=%s", (user.id,))
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[3], user.email)
        self.assertEqual(result[4], user.password)
        self.assertEqual(result[5], user.first_name)
        self.assertEqual(result[6], user.last_name)

if __name__ == "__main__":
    unittest.main()
