# Author:Alex Li
import s3

obj = s3.RedisHelper()
data = obj.subscribe('fm111.7')
print(data.parse_response())
