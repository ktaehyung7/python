# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 17:12:49 2020

@author: Pulmuone
"""

import time
from locust import HttpUser, task, between

class Quickstartuser(HttpUser):
    wait_time = between(1,2)
    
    @task
    def index_page(self):
        self.client.get("/")
#        self.client.get("/hello")
#        self.client.get("/world")
        
    @task(3)
#    def view_item(self):
#        for item_id in range(10):
#            self.client.get(f"/item?id={item_id}", name="/item")
#            time.sleep(1)
            
    def on_start(self):
#        self.client.post("/login", json={"username":"foo", "password":"bar"})
#        self.client.post("/nidlogin.login", json={"userid":"bluebluelion", "password":"!05rltnftk22"})
        self.client.get("/")