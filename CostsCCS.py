import pandas as pd
import numpy as np
from tableauscraper import TableauScraper as TS

url = "https://public.tableau.com/shared/99WD3TBJK"

ts = TS(delayMs=10000)
ts.loads(url)
workbook = ts.getWorkbook()


storypoint = workbook.goToStoryPoint(storyPointId=3)
worksheet = storypoint.getWorksheet("Sources map")
InstNoFilt = worksheet.getSelectableItems()

worksheetFilt = worksheet.setFilter('New pipeline?', 'Not possible', filterDelta=True)
workbookFilt = ts.getWorkbook()
storypointFilt = workbookFilt.goToStoryPoint(storyPointId=3)
worksheetFilt = storypointFilt.getWorksheet("Sources map")
InstPipelineFilt = worksheet.getSelectableItems()


data = {"ID": range(0, 2147),
        "Scenario": ["Short term" for x in range(0, 2147)],
        "New Pipeline": ["Not possible" for x in range(0, 2147)],
        "Costs": ["High estimates" for x in range(0, 2147)]}

for i in range(18):
    data[InstNoFilt[i]['column']] = InstNoFilt[i]['values']
df = pd.DataFrame(data)
df.to_csv('test.csv', index=False)



"""
df = pd.DataFrame({"ID": range(0, 2147),
                   InstNoFilt[0]['column']: InstNoFilt[0]['values'],
                   InstNoFilt[1]['column']: InstNoFilt[1]['values'],
                   InstNoFilt[2]['column']: InstNoFilt[2]['values'],
                   InstNoFilt[3]['column']: InstNoFilt[3]['values'],
                   InstNoFilt[4]['column']: InstNoFilt[4]['values'],
                   InstNoFilt[5]['column']: InstNoFilt[5]['values'],
                   InstNoFilt[6]['column']: InstNoFilt[6]['values'],
                   InstNoFilt[7]['column']: InstNoFilt[7]['values'],
                   InstNoFilt[8]['column']: InstNoFilt[8]['values'],
                   InstNoFilt[9]['column']: InstNoFilt[9]['values'],
                   InstNoFilt[10]['column']: InstNoFilt[10]['values'],
                   InstNoFilt[11]['column']: InstNoFilt[11]['values'],
                   InstNoFilt[12]['column']: InstNoFilt[12]['values'],
                   InstNoFilt[13]['column']: InstNoFilt[13]['values'],
                   InstNoFilt[14]['column']: InstNoFilt[14]['values'],
                   InstNoFilt[15]['column']: InstNoFilt[15]['values'],
                   InstNoFilt[16]['column']: InstNoFilt[16]['values'],
                   InstNoFilt[17]['column']: InstNoFilt[17]['values']})
df.to_csv('data.csv', index=False)
"""
