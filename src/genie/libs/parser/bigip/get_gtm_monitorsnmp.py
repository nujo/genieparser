# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/monitor/snmp' resources
# =============================================


class GtmMonitorSnmpSchema(MetaParser):

    schema = {}


class GtmMonitorSnmp(GtmMonitorSnmpSchema):
    """ To F5 resource for /mgmt/tm/gtm/monitor/snmp
    """

    cli_command = "/mgmt/tm/gtm/monitor/snmp"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
