def add_setting(dictionary_setting,tuple_setting):
    key,value=tuple_setting
    key=key.lower()
    value=value.lower()
    if key in dictionary_setting:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        dictionary_setting[key]=value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(dictionary_setting,tuple_setting):
    key,value=tuple_setting
    key=key.lower()
    value=value.lower()
    if key in dictionary_setting:
        dictionary_setting[key]=value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dictionary_setting,key):
    key=key.lower()
    if key in dictionary_setting:
        del dictionary_setting[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(dictionary_setting):
    if not dictionary_setting:
        return "No settings available."
    result=""
    for key in dictionary_setting:
        result+=f"{key.capitalize()}: {dictionary_setting[key]}\n"
    return f"Current User Settings:\n{result}"
    
test_settings={'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}
