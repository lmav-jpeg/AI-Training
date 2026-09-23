"""
This code presents a Hardware Integrity Expert System.
First, test the system using the `expected_identity.sql` file
and observe the output.
Then, run the `changes.sql` file to introduce changes to
the expected hardware information and run the Python program again.
 Compare the two outputs and observe how the Expert System detects
 the inconsistencies between the expected and observed hardware configurations.

@author: Laurie MAVOUNGOU JK AI CEO lmavoungou@outlook.be
"""

from wmi import WMI
import mysql.connector

### Information Retrieval Points
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="qwerty",
    database="KnowledgeBase"
)

computer = WMI()

def hardware_identity():
    '''
    Fact acquisition
    :return: dictionary with information about the hardware
    '''
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
    # print(board)
    if board:
        identity["motherboard"] = {
            "manufacturer": board[0].Manufacturer,
            "product": board[0].Product,
            "serial_number": board[0].SerialNumber
        }

    # CPU
    processors = computer.Win32_Processor()
    #print(processors)
    identity["processors"] = []

    for processor in processors:
        identity["processors"].append({
            "manufacturer": processor.Manufacturer,
            "name": processor.Name,
            "processor_id": processor.ProcessorId
        })

    # RAM
    memory = computer.Win32_PhysicalMemory()
    #print(memory)
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
    #print(disks)
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

    cursor = connection.cursor(dictionary=True)
    commands = [
        "SELECT * FROM bios",
        "SELECT * FROM computer",
        "SELECT * FROM motherboard",
        "SELECT * FROM processor",
        "SELECT * FROM memory",
        "SELECT * FROM disks"
    ]

    tables = [
        "bios",
        "computer",
        "motherboard",
        "processor",
        "memory",
        "disks"
    ]

    expected = {}

    for table, command in zip(tables, commands):
        cursor.execute(command)

        if table in ["memory", "disks"]:
            expected[table] = cursor.fetchall()
        else:
            expected[table] = cursor.fetchone()

    cursor.close()
    connection.close()
    return expected

#### INFERENCE ENGINE

def verify_computer(expected, observed):
    fields = [
        ("manufacturer", "manufacturer", "Computer manufacturer"),
        ("model", "model", "Computer model"),
        ("systemFamily", "system_family", "Computer system family")
    ]

    results = []

    for expected_field, observed_field, description in fields:
        if expected[expected_field] == observed[observed_field]:
            results.append(f"{description} matches.")
        else:
            results.append(f"{description} does not match.")

    return results

def verify_motherboard(expected, observed):
    fields = [
        ("manufacturer", "manufacturer", "Motherboard manufacturer"),
        ("product", "product", "Motherboard product"),
        ("serialNumber", "serial_number", "Motherboard serial number")
    ]

    results = []

    for expected_field, observed_field, description in fields:
        if expected[expected_field] == observed[observed_field]:
            results.append(f"{description} matches.")
        else:
            results.append(f"{description} does not match.")

    return results

def verify_cpu(expected, observed):
    fields = [
        ("manufacturer", "manufacturer", "CPU manufacturer"),
        ("processorID", "processor_id", "CPU ID"),
        ("name", "name", "CPU name")
    ]

    results = []

    for expected_field, observed_field, description in fields:
        if expected[expected_field] == observed[observed_field]:
            results.append(f"{description} matches.")
        else:
            results.append(f"{description} does not match.")

    return results

def verify_disks(expected, observed):
    fields = [
        ("model", "model"),
        ("serialNumber", "serial_number")
    ]

    results = []

    for expected_field, observed_field in fields:
        if expected[expected_field] == observed[observed_field]:
            results.append(f"Disk {expected_field} matches.")
        else:
            results.append(f"Disk {expected_field} does not match.")
    return results

def verify_memory(expected, observed):
    fields = [
        ("manufacturer", "manufacturer"),
        ("serialNumber", "serial_number"),
        ("capacity", "capacity"),
        ("partNumber", "part_number")
    ]

    results = []

    for expected_field, observed_field in fields:
        expected_value = expected[expected_field]
        observed_value = observed[observed_field]

        if expected_field == "capacity":
            observed_value = int(observed_value)

        if expected_value == observed_value:
            results.append(f"Memory {expected_field} matches.")
        else:
            results.append(f"Memory {expected_field} does not match.")

    return results

def verify_bios(expected, observed):
    fields = [
        ("manufacturer", "manufacturer"),
        ("serialNumber", "serial_number"),
        ("version", "version")
    ]

    results = []

    for expected_field, observed_field in fields:
        if expected[expected_field] == observed[observed_field]:
            results.append(f"BIOS {expected_field} matches.")
        else:
            results.append(f"BIOS {expected_field} does not match.")

    return results

    return results

def working_memory(expected, observed):

    problems = {}
    results = verify_bios(
        expected["bios"],
        observed["bios"]
    )
    for result in results:
        if "does not match" in result:
            problems[result] = True

    results = verify_computer(
        expected["computer"],
        observed["computer"]
    )

    for result in results:
        if "does not match" in result:
            problems[result] = True

    results = verify_motherboard(
        expected["motherboard"],
        observed["motherboard"]
    )

    for result in results:
        if "does not match" in result:
            problems[result] = True

    for index, obs in enumerate(observed["processors"]):
        results = verify_cpu(
            expected["processor"],
            obs
        )

        for result in results:
            if "does not match" in result:
                problems[f"CPU {index + 1}: {result}"] = True

    expected_memory_count = expected["memory"][0]["numberMemory"]

    if len(observed["memory"]) != expected_memory_count:
        problems["Number of memory modules does not match."] = True

    for exp, obs in zip (expected["memory"], observed["memory"]):
        results = verify_memory(
            exp,
            obs
        )

        for result in results:
            if "does not match" in result:
                problems[result] = True

    if len(expected["disks"]) != len(observed["disks"]):
        problems["Number of disks modules does not match."] = True

    for exp, obs in zip (expected["disks"], observed["disks"]):
        results = verify_disks(
            exp,
            obs
        )

        for result in results:
            if "does not match" in result:
                problems[result] = True

    return problems

if __name__ == '__main__':
    ### INFORMATION RETRIEVAL
    # FACT ACQUISITION
    identity = hardware_identity()
    # KNOWLEDGE BASE
    expected = get_expected_hardware()

    ### WORKING MEMORY
    problems = working_memory(expected, identity)

    ### CONCLUSION AND EXPLANATION
    if problems:
        print("The computer is not consistent")
        print("Reasons below")
        for key in problems.keys():
            print(f"{key}")
    else:
        print("The computer is consistent")