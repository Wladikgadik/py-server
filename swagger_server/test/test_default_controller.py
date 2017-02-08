# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.experiment import Experiment
from swagger_server.models.simulation import Simulation
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDefaultController(BaseTestCase):
    """ DefaultController integration test stubs """

    def test_exp_id_get(self):
        """
        Test case for exp_id_get

        
        """
        response = self.client.open('/v1/exp/{id}'.format(id='id_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_exp_id_results_get(self):
        """
        Test case for exp_id_results_get

        
        """
        response = self.client.open('/v1/exp/{id}/results'.format(id='id_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_exp_id_setvariables_post(self):
        """
        Test case for exp_id_setvariables_post

        
        """
        params = 'params_example'
        response = self.client.open('/v1/exp/{id}/setvariables'.format(id='id_example'),
                                    method='POST',
                                    data=json.dumps(params),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_exp_id_start_get(self):
        """
        Test case for exp_id_start_get

        
        """
        response = self.client.open('/v1/exp/{id}/start'.format(id='id_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_exp_id_stop_get(self):
        """
        Test case for exp_id_stop_get

        
        """
        response = self.client.open('/v1/exp/{id}/stop'.format(id='id_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_exp_init_get(self):
        """
        Test case for exp_init_get

        
        """
        query_string = [('gitrepo', 'gitrepo_example')]
        response = self.client.open('/v1/exp/init',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_sim_id_get(self):
        """
        Test case for sim_id_get

        
        """
        response = self.client.open('/v1/sim/{id}'.format(id='id_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_sim_id_results_get(self):
        """
        Test case for sim_id_results_get

        
        """
        response = self.client.open('/v1/sim/{id}/results'.format(id='id_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_sim_id_vizconnect_get(self):
        """
        Test case for sim_id_vizconnect_get

        
        """
        response = self.client.open('/v1/sim/{id}/vizconnect'.format(id='id_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
