import json

class JSONConfig:
	'''Simple constructor to use .json files as configs'''

	def __init__(self, config_path: str) -> None:
		'''config_path: .json config path '''
		self.path = config_path
	
	def _get_scheme(self) -> dict:
		'''get data as dict of .json config'''
		with open(self.path, encoding='utf-8') as file:
			return json.load(file)

	def _save_scheme(self, data: dict) -> None:
		'''save data into .json config'''
		with open(self.path, 'w', encoding='utf-8') as file:
			return json.dump(data, file, indent=4, ensure_ascii=False)

	def _get_pretty_path(self, path: str) -> str:
		'''parse path'''
		path = ".".join([f"'{key}'" for key in path.split('.')])
		path =  f"[{path.replace('.', '][')}]"

		return path
	
	def set_value(self, path: str, value) -> None:
		'''update value of .json config'''
		data = self._get_scheme()
		exec(f"data{self._get_pretty_path(path)} = {value}")
		self._save_scheme(data)
	
	def get_value(self, path: str) -> None:
		'''get value of .json config'''
		return eval(f"{self._get_scheme()}{self._get_pretty_path(path)}")