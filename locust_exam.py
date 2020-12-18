# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 13:44:21 2020

@author: Pulmuone
"""

from locust import HttpUser, task, between
from locust.exception import RescheduleTask

class MyUser(HttpUser):
    wait_time = between(5,10)
    
    @task(1)
    def index(self):
        self.client.get("/")
        
    @task(10)
    def about(self):
        with self.client.get("/does_not_exist/", catch_response=True) as response:
            if response.status_code != 404 :
                raise RescheduleTask()
