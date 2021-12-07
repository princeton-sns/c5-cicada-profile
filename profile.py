"""
CloudLab profile for CopyCat-Cicada experiments
"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# CONSTANTS
IMAGE = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU20-64-STD"
HW_TYPE = "c220g5"

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

# Add a raw PC to the request.
node = request.RawPC("node")
node.disk_image = IMAGE
node.hardware_type = HW_TYPE

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
