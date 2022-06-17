from sqlite3 import connect
from cloudant.client import Cloudant
client = Cloudant.iam("eb042170-8fc1-4ad4-a792-320d11925ca9-bluemix", "UFY5C1LMlfJmRmNJaq52u9WgX8wFLzPJvBzhHHpx13Oq", connect = True)
my_database = client.create_database('my_database')