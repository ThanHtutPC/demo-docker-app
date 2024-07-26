import pymongo
import gridfs

# MongoDB connection details
client = pymongo.MongoClient("mongodb://admin:password@localhost:27017/")
db = client["mydatabase"]
fs = gridfs.GridFS(db)

# Function to upload file to GridFS
def upload_file(file_path, file_name):
    with open(file_path, 'rb') as f:
        file_id = fs.put(f, filename=file_name)
    return file_id

# Upload profile_card.html
file_id = upload_file('profile_card.html', 'profile_card.html')
print(f'profile_card.html uploaded with file ID: {file_id}')

