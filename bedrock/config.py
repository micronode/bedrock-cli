from .utils import *


class ConfigSpec:

    def __init__(self, blueprint_id, instance_name, dry_run=False):

        # Enable dry run (skip backend configuration)
        self.dry_run = dry_run

        # Blueprint identifier
        self.blueprint_id = blueprint_id

        # Command-line variables
        self.cvars = {}

    def run(self):
        if self.dry_run:
            print("Dry run enabled. No changes will be made.")

        if not self.dry_run:
            workspace = current_workspace(self.blueprint_id)
            write_config(self.blueprint_id, workspace, self.cvars)