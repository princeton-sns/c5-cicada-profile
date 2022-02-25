"""
CloudLab profile for CopyCat-Cicada experiments
"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# CONSTANTS
IMAGE = "urn:publicid:IDN+wisc.cloudlab.us+image+cops-PG0:copycat-cicada"
DEFAULT_HW_TYPE = "c220g5"

# Create a portal context.
pc = portal.Context()

pc.defineParameter("phystype", "Physical node type",
                   portal.ParameterType.STRING, DEFAULT_HW_TYPE,
                   longDescription="Specify a physical node type (pc3000, d710, etc.).")

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

# Retrieve the values the user specifies during instantiation.
params = pc.bindParameters()

# Check parameter validity.
if params.phystype == "":
    pc.reportError(portal.ParameterError("You must specify a node type.", ["phystype"]))

pc.verifyParameters()

# Add a raw PC to the request.
node = request.RawPC("node")
node.disk_image = IMAGE
node.hardware_type = params.phystype

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
