import unittest
import json
from to_do_list import load_tasks, save_tasks, add_task, remove_task, mark_task_completed, list_tasks

class TestTaskManager(unittest.TestCase):
    
    def test_load_tasks(self):
        tasks = load_tasks("tasks.json")
        print("Loaded tasks:", tasks)
        self.assertIsInstance(tasks, list)  
        self.assertGreater(len(tasks), 0)

    def test_save_tasks(self):
        tasks = [{"id": 1, "description": "Test task", "completed": False}]
        save_tasks(tasks, "tasks.json")
        
        tasks_from_file = load_tasks("tasks.json")
        self.assertEqual(tasks, tasks_from_file)

    def test_add_task(self):
        add_task("tasks.json", "new task")
        tasks = load_tasks("tasks.json")
        print("Tasks after adding:", tasks)
        self.assertEqual(len(tasks), 2)  
        self.assertEqual(tasks[-1]['description'], "new task")  

    def test_remove_task(self):
        remove_task("tasks.json", 1)
        tasks = load_tasks("tasks.json")
        print("Tasks after removing:", tasks)
        self.assertEqual(len(tasks), 0)  

    def test_mark_task_completed(self):
        add_task("tasks.json", "new task")
        mark_task_completed("tasks.json", 2)
        tasks = load_tasks("tasks.json")
        print("Tasks after marking as completed:", tasks)
        self.assertTrue(tasks[1]['completed'])

if __name__ == "__main__":
    unittest.main()
