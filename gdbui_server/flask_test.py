import unittest
import json
from flask import Flask
from flask_testing import TestCase # type: ignore
from gdbui_server.main import app  # Assuming your app is named main4.py

class TestGDBRoutes(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        # Compile a simple C++ program for testing
        compile_payload = {
            "code": "#include <iostream>\nint main() { std::cout << 'Hello, World!'; return 0; }",
            "name": "test_program"
        }
        self.client.post('/compile', data=json.dumps(compile_payload), content_type='application/json')

    def test_compile_code(self):
        payload = {
            "code": "#include <iostream>\nint main() { std::cout << 'Hello, Universe!'; return 0; }",
            "name": "test_program2"
        }
        response = self.client.post('/compile', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json['success'])

    def test_gdb_command(self):
        gdb_payload = {
            "command": "info locals",
            "name": "test_program"
        }
        response = self.client.post('/gdb_command', data=json.dumps(gdb_payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json['success'])

    def test_set_breakpoint(self):
        breakpoint_payload = {
            "location": "main",
            "name": "test_program"
        }
        response = self.client.post('/set_breakpoint', data=json.dumps(breakpoint_payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json['success'])

    def test_info_breakpoints(self):
        breakpoint_payload = {
            "location": "main",
            "name": "test_program"
        }
        self.client.post('/set_breakpoint', data=json.dumps(breakpoint_payload), content_type='application/json')

        info_payload = {
            "name": "test_program"
        }
        response = self.client.post('/info_breakpoints', data=json.dumps(info_payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json['success'])

    def test_stack_trace(self):
        stack_trace_payload = {
            "name": "test_program"
        }
        response = self.client.post('/stack_trace', data=json.dumps(stack_trace_payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json['success'])

    def test_threads(self):
        threads_payload = {
            "name": "test_program"
        }
        response = self.client.post('/threads', data=json.dumps(threads_payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json['success'])

    def test_get_registers(self):
        get_registers_payload = {
            "name": "test_program"
        }
        response = self.client.post('/get_registers', data=json.dumps(get_registers_payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json['success'])

    def test_get_locals(self):
        get_locals_payload = {
            "name": "test_program"
        }
        response = self.client.post('/get_locals', data=json.dumps(get_locals_payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json['success'])

    def test_run_program(self):
        run_payload = {
            "name": "test_program"
        }
        response = self.client.post('/run', data=json.dumps(run_payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json['success'])

    def test_memory_map(self):
        memory_map_payload = {
           "name": "test_program"
        }
        response = self.client.post('/memory_map', data=json.dumps(memory_map_payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json['success'])

if __name__ == '__main__':
    unittest.main()
