import requests


class Data(object):

    base_url = 'http://www.bea.gov/api/data?'

    def __init__(self, api_key, result_format='json'):
        self.api_key = api_key
        self.result_format = result_format

    @property
    def data_set_list(self):
        tmp_query = {'UserID': self.api_key,
                     'Method': 'GetDataSetList',
                     'ResultFormat': self.result_format}
        tmp_response = requests.get(url=self.base_url, params=tmp_query)
        return tmp_response
