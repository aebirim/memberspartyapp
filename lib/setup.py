from generategraph import GenerateGraph
import json
import requests
import pprint
from urllib.parse import urljoin

class SetupGraph:
  """Setup a graph on a page that has the following properties:
  Attributes:
      Houses: A string representing the particular house of parliament, Houses=Commons passed as default
  """
  headers = {"content-type": "application/json"}
  baseUrl = "http://data.parliament.uk/membersdataplatform/services/mnis/members/query/"
  search_constraints = "House=Commons"

  def __init__(self, search_constraints=search_constraints):
      self.baseUrl = SetupGraph.baseUrl
      self.search_constraints = search_constraints
      self.outputs = "Constituencies"

  def _connect(self):
      url = self._buildUrl()
      try:
        r = requests.get(url, headers=SetupGraph.headers)
      except ValueError as err:
        print('Get request broken: {}'.format(err))
        r.encoding = "utf-8"

      output = r.text
      return output

  def newGraph(self):
      output = self._connect()
      members = json.loads(output[1:])
      GenerateGraph(members).test()

  def _buildUrl(self):
      # params = self.search_constraints
      # params += '/'
      # params += self.outputs
      new_params = [self.search_constraints, self.outputs]
      params = '/'.join(new_params)
      new_url = urljoin(self.baseUrl, params)
      return new_url

