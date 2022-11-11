# JSONConfig

### JSONConfig was created to use .json files as configs

### You can create own functions to get values from the config and update values

## How can i use it?

*Use this command to install the module*
```console
$ > pip3 install json-config
```

## Simple tutorial

*We are going to create some `Config` to add and get admins*

#### Create `config.json` file in the root directory with content like this
```json
{
    "admins": []
}
```

#### Import the module into your main .py file
```python
import json_config
```

#### Then you need to create some class with extend by the module
```python 
class Config(json_config.JSONConfig):
    def get_admins(self):
        return self.get_value('admins') 

    def add_admin(self, admin):
        self.set_value('admins', admin)
```

#### That\`s it! Now let`s test it

```python
config = Config('.config.json')

config.get_admins() # []

config.add_admin(123)

config.get_admins() # [123]
```

#### Now you can create own functions but you don`t know a main feature

##### To get or update values you need to point the `path`, but if u have a complex structure you can use the "dot" operator like this:

```python

# the structure 
# 
# {
#     "main": {
#         "sub_main": {
#             "admins": []
#         }
#     }
# }

class Config(json_config.JSONConfig):
    def get_admins(self):
        return self.get_value('main.sub_main.admins') 

    def add_admin(self, admin):
        self.set_value('main.sub_main.admins', admin)
```

## Ther are also others functions here:

### `self._get_scheme`
get data as dict of .json config

### `self._save_scheme`
save data into .json config

### `self.set_value`
update value of .json config

### `self.get_value`
get value of .json config