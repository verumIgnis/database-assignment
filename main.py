from datetime import datetime, timedelta

parsedDate=datetime.strptime("2022-09-21", "%Y-%m-%d")
updatedDate = parsedDate + timedelta(days=3)
print(updatedDate)