import pandas as pd
from tableauscraper import TableauScraper as TS

url = "https://public.tableau.com/shared/99WD3TBJK"

ts = TS(delayMs=500)
ts.loads(url)
workbook = ts.getWorkbook()

storypoint = workbook.goToStoryPoint(storyPointId=3)
worksheet = storypoint.getWorksheet("Sources map")
InstNoFilt = worksheet.getSelectableItems()


data = {"ID": range(0, 2147),
        "Scenario": ["Short term" for x in range(0, 2147)],
        "New Pipeline": ["Not possible" for x in range(0, 2147)],
        "Costs": ["High estimates" for x in range(0, 2147)]}

for i in range(18):
    data[InstNoFilt[i]['column']] = InstNoFilt[i]['values']
df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)
