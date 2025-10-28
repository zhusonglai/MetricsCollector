# test_metricscollector.py
"""
Tests for MetricsCollector module.
"""

import unittest
from metricscollector import MetricsCollector

class TestMetricsCollector(unittest.TestCase):
    """Test cases for MetricsCollector class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MetricsCollector()
        self.assertIsInstance(instance, MetricsCollector)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MetricsCollector()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
