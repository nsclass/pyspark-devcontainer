# Copyright (c) 2023 Nam Seob Seo
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import unittest
import os
from pathlib import Path
from pyspark.sql import SparkSession

from nseo.pyspark.pyspark_app import pyspark_app_process

class HelloWorldTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        THIS_DIR = Path(__file__).parent
        data_path = THIS_DIR.parent / 'data'
        cls.spark = SparkSession \
                    .builder \
                    .master("spark://spark:7077") \
                    .config("spark.driver.host", "pyspark-app") \
                    .appName('pyspark-app') \
                    .getOrCreate()

        return None

    def test_should_issue_hello_world_message(self):
        df = self.spark.read.csv("/mounted-data/src/unittest/data/crash_catalonia.csv")
        row_count = df.count();
        print(f"Row count: {row_count}")
        pyspark_app_process()
