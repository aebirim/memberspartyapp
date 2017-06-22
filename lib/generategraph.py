import pandas as pd
import matplotlib.pyplot as plt, mpld3
#plt.switch_backend("TkAgg")

class GenerateGraph:

  def __init__(self, members):
      self.members = members
      self.name = []
      self.party = []
      self.house = []
      self.gender = []
      self.dataMember = [self.name, self.party, self.house, self.gender]
      self.dataDict = {}

  def test(self):
      members = self.members['Members']['Member']
      members_data = members
      name, gender, party, house = self._buildData(members_data)
      dataDict = self._buildDict(name, gender, party, house)
      self._buildGraph(dataDict)

  def _buildData(self, data):
      for member in data:
          if self.name in self.dataMember:
             self.name.append(member['DisplayAs'])
          if self.gender in self.dataMember:
             self.gender.append(member['Gender'])
          if self.party in self.dataMember:
             self.party.append(member['Party']['#text'])
          if self.house in self.dataMember:
             self.house.append(member['House'])

      return self.name, self.gender, self.party, self.house

  def _buildDict(self, name, gender, party, house):
      self.dataDict['member'] = name
      self.dataDict['gender'] = gender
      self.dataDict['party'] = party
      self.dataDict['house'] = house
      return self.dataDict


  def _buildGraph(self, dict):
      politicians = pd.DataFrame(dict)
      p_house = politicians['house']
      house = p_house.unique()
      e = politicians.groupby(['party', 'gender']).size().unstack().plot(kind='barh', stacked=True,
                                                                         title='Gender count in House of %s' %
                                                                               house[0], figsize=(15,8))
      e.set_xlabel("count")
      e.set_ylabel("party")
      e.legend(["Female", "Male"], loc=9, ncol=4, fontsize = 'large')
      mpld3.show()




