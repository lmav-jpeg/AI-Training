"""
This code presents a Hardware Integrity Expert System.
First, test the system using the `expected_identity.sql` file
and observe the output.
Then, run the `changes.sql` file to introduce changes to
the expected hardware information and run the Python program again.
 Compare the two outputs and observe how the Expert System detects
 the inconsistencies between the expected and observed hardware configurations.
"""

from wmi import WMI
import mysql.connector


def hardware_identity():
    '''
    Fact acquisition
    :return: dictionary with information about the hardware
    '''
    computer = WMI()

    identity = {}

    # BIOS
    bios = computer.Win32_BIOS()
    if bios:
        identity["bios"] = {
            "manufacturer": bios[0].Manufacturer,
            "serial_number": bios[0].SerialNumber,
            "version": bios[0].Version
        }

    # Computer
    system = computer.Win32_ComputerSystem()
    if system:
        identity["computer"] = {
            "manufacturer": system[0].Manufacturer,
            "model": system[0].Model,
            "system_family": system[0].SystemFamily
        }

    # Motherboard
    board = computer.Win32_BaseBoard()
    if board:
        identity["motherboard"] = {
            "manufacturer": board[0].Manufacturer,
            "product": board[0].Product,
            "serial_number": board[0].SerialNumber
        }

    # CPU
    processors = computer.Win32_Processor()

    identity["processors"] = []

    for processor in processors:
        identity["processors"].append({
            "manufacturer": processor.Manufacturer,
            "name": processor.Name,
            "processor_id": processor.ProcessorId
        })

    # RAM
    memory = computer.Win32_PhysicalMemory()

    identity["memory"] = []

    for module in memory:
        identity["memory"].append({
            "manufacturer": module.Manufacturer,
            "part_number": module.PartNumber,
            "serial_number": module.SerialNumber,
            "capacity": module.Capacity
        })

    # Disks
    disks = computer.Win32_DiskDrive()

    identity["disks"] = []

    for disk in disks:
        identity["disks"].append({
            "model": disk.Model,
            "manufacturer": disk.Manufacturer,
            "serial_number": disk.SerialNumber,
            "interface": disk.InterfaceType
        })

    return identity



def get_expected_hardware():
    '''
    Knowledge base
    :return: dictionary with expected information about the hardware
    '''

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="qwerty",
        database="KnowledgeBase"
    )

    cursor = connection.cursor(dictionary=True)

    expected = {}

    cursor.execute("SELECT * FROM bios")
    expected["bios"] = cursor.fetchone()

    cursor.execute("SELECT * FROM computer")
    expected["computer"] = cursor.fetchone()

    cursor.execute("SELECT * FROM motherboard")
    expected["motherboard"] = cursor.fetchone()

    cursor.execute("SELECT * FROM processor")
    expected["processor"] = cursor.fetchone()

    cursor.execute("SELECT * FROM memory")
    expected["memory"] = cursor.fetchall()

    cursor.execute("SELECT * FROM disks")
    expected["disks"] = cursor.fetchall()

    cursor.close()
    connection.close()
    return expected

#### INFERENCE ENGINE

def verify_computer(expected, observed):

    results = []

    if expected["manufacturer"] == observed["manufacturer"]:
        results.append("Computer manufacturer matches.")
    else:
        results.append("Computer manufacturer does not match.")

    if expected["model"] == observed["model"]:
        results.append("Computer model matches.")
    else:
        results.append("Computer model does not match.")

    if expected["systemFamily"] == observed["system_family"]:
        results.append("Computer system family matches.")
    else:
        results.append("Computer system family does not match.")

    return results

def verify_motherboard(expected, observed):

    results = []

    if expected["manufacturer"] == observed["manufacturer"]:
        results.append("Motherboard manufacturer matches.")
    else:
        results.append("Motherboard manufacturer does not match.")

    if expected["product"] == observed["product"]:
        results.append("Motherboard product matches.")
    else:
        results.append("Motherboard product does not match.")

    if expected["serialNumber"] == observed["serial_number"]:
        results.append("Motherboard serial number matches.")
    else:
        results.append("Motherboard serial number does not match.")

    return results

def verify_cpu(expected, observed):

    results = []

    if expected["manufacturer"] == observed["manufacturer"]:
        results.append("CPU manufacturer matches.")
    else:
        results.append("CPU manufacturer does not match.")

    if expected["processorID"] == observed["processor_id"]:
        results.append("CPU ID matches.")
    else:
        results.append("CPU ID does not match.")

    if expected["name"] == observed["name"]:
        results.append("CPU name matches.")
    else:
        results.append("CPU name does not match.")

    return results

def verify_disks(expected, observed):

    results = []

    if expected["model"] == observed["model"]:
        results.append("Disks model matches.")
    else:
        results.append("Disks model does not match.")

    if expected["serialNumber"] == observed["serial_number"]:
        results.append("Disks serial number matches.")
    else:
        results.append("Disks serial number does not match.")
    return results

def verify_memory(expected, observed):

    results = []

    if expected["manufacturer"] == observed["manufacturer"]:
        results.append("Memory manufacturer matches.")
    else:
        results.append("Memory manufacturer does not match.")

    if expected["serialNumber"] == observed["serial_number"]:
        results.append("Memory serial number matches.")
    else:
        results.append("Memory serial number does not match.")

    if expected["capacity"] == int(observed["capacity"]):
        results.append("Memory capacity matches.")
    else:
        results.append("Memory capacity does not match.")

    if expected["partNumber"] == observed["part_number"]:
        results.append("Memory part number matches.")
    else:
        results.append("Memory part number does not match.")

    return results

def verify_bios(expected, observed):

    results = []

    if expected["manufacturer"] == observed["manufacturer"]:
        results.append("BIOS manufacturer matches.")
    else:
        results.append("BIOS manufacturer does not match.")

    if expected["serialNumber"] == observed["serial_number"]:
        results.append("BIOS serial number matches.")
    else:
        results.append("BIOS serial number does not match.")

    if expected["version"] == observed["version"]:
        results.append("BIOS version matches.")
    else:
        results.append("BIOS version does not match.")

    return results


### INFORMATION RETRIEVAL
# FACT ACQUISITION
identity = hardware_identity()
#for key, value in identity.items():
#    print(f"{key}: {value}")

#### KNOWLEDGE BASE
expected = get_expected_hardware()
#for key, value in expected.items():
#    print(f"{key}: {value}")

#### WORKING MEMORY
problems = {}
results = verify_bios(
    expected["bios"],
    identity["bios"]
)
for result in results:
    if "does not match" in result:
        problems[result] = True

results = verify_computer(
    expected["computer"],
    identity["computer"]
)

for result in results:
    if "does not match" in result:
        problems[result] = True

results = verify_motherboard(
    expected["motherboard"],
    identity["motherboard"]
)

for result in results:
    if "does not match" in result:
        problems[result] = True

results = verify_cpu(
    expected["processor"],
    identity["processors"][0]
)

for result in results:
    if "does not match" in result:
        problems[result] = True

results = verify_memory(
    expected["memory"][0],
    identity["memory"][0]
)

for result in results:
    if "does not match" in result:
        problems[result] = True

results = verify_disks(
    expected["disks"][0],
    identity["disks"][0]
)

for result in results:
    if "does not match" in result:
        problems[result] = True

### CONCLUSION AND EXPLANATION
if problems:
    print("The computer is not consistent")
    print("Reasons below")
    for key in problems.keys():
        print(f"{key}")
else:
    print("The computer is consistent")