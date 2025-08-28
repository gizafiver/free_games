
import json
import importlib
import os
import sys

class Trojan:
    def __init__(self, config_path="config/abc.json"):
        self.config = self.load_config(config_path)
        self.modules = self.load_modules()
        
    def load_config(self, config_path):
        with open(config_path, 'r') as config_file:
            return json.load(config_file)
            
    def load_modules(self):
        modules = {}
        for module_config in self.config:
            module_name = module_config['module']
            try:
                # Import the module
                module = importlib.import_module(f'modules.{module_name}')
                modules[module_name] = module
                print(f"[+] Successfully loaded module: {module_name}")
            except ImportError as e:
                print(f"[-] Failed to load module {module_name}: {e}")
        return modules
        
    def run(self):
        print("[*] Starting Trojan execution")
        results = {}
        for module_name, module in self.modules.items():
            try:
                results[module_name] = module.run()
                print(f"[+] Module {module_name} executed successfully")
            except Exception as e:
                print(f"[-] Module {module_name} failed: {e}")
        return results

if __name__ == "__main__":
    trojan = Trojan()
    results = trojan.run()
    print("[*] Execution results:", results)