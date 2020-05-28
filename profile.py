"""
CloudLab profile for Silo (as part of Thermopylae)
"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# CONSTANTS
IMAGE = "urn:publicid:IDN+apt.emulab.net+image+emulab-ops:UBUNTU14-64-STD"

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

# Add a raw PC to the request.
node = request.RawPC("node")
node.disk_image = IMAGE

# Install and execute a script that is contained in the repository.
node.addService(pg.Execute(shell="sh", command="/local/repository/setup.sh"))

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
