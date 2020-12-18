# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 15:35:36 2020

@author: Pulmuone
"""

from locust import HttpUser,  task, between
import random

class MyLocust(HttpUser):
    wait_time = between(3,5)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.serial = ['', '', '']
        
    def on_start(self):
        print('Now Shooting API')
        
    @task(1)
    def index(self):
        self.usertoken = '<user token>'
        self.headers = {'Authorization': self.usertoken}
        self.url = '<api request endpoint>' + random.choice(self.serial)
        self.client.get(url=self.url, headers=self.headers)
        