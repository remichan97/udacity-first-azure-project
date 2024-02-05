"""
The Azure Storage handling class.
"""
from azure.storage.blob import BlobServiceClient

class Storage:
	# Using newer version of azure-storage-blob, adapted from examples at 
	# https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/storage/azure-storage-blob/samples/blob_samples_hello_world.py
	def __init__(self, connectionstring : str, blobcontainer : str) :
		client = BlobServiceClient.from_connection_string(connectionstring)
		self.container = client.get_container_client(blobcontainer)

	def upload_to_storage(self, filename, file):
		self.container.upload_blob(filename, file)

	def delete_file(self, filename):
		self.container.delete_blob(filename)
		