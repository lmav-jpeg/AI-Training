# 🖥️ Student Work — Hardware Integrity Expert System

## 🎯 Objective

You are given a partially completed **Hardware Integrity Expert System**.

The system collects hardware information from a computer using **WMI**, retrieves expected hardware information from a **MySQL Knowledge Base**, and uses rules to determine whether the observed computer configuration is consistent with the expected configuration.

Your task is to **test, understand, improve, and extend the Expert System**. 🧠

---

## 1. 🔍 Test the Existing System

Start by running the system with the provided `expected_identity.sql` dataset after populating it.

Observe:

* 🖥️ The hardware information collected by WMI.
* 🗄️ The information retrieved from the Knowledge Base.
* 🔎 The verification results.
* 🧠 The final conclusion of the Expert System.

The expected result is that the observed hardware is consistent with the information stored in the Knowledge Base.

---

## 2. 🧪 Test the Expert System with Changes

Modify and run the `correction.sql` file to introduce changes to the expected hardware information.

Run the Python program again.

Compare the output **before and after** applying the changes.

Ask yourself:

* ❓ Did the Expert System detect the changes?
* 🔎 Which hardware component was identified as inconsistent?
* 💬 Is the explanation accurate?
* ⚠️ Are all inconsistencies detected?

---

## 3. 🕵️ Find What Does Not Work Well

Inspect the existing code and identify weaknesses in the system.

For example, investigate whether the system correctly handles:

* 🧠 Multiple memory modules.
* 💾 Multiple disks.
* ⚙️ Multiple processors.
* ❌ Missing hardware information.
* 🔄 Different values stored in the Knowledge Base.
* ➕ Unexpected hardware components.
* 💬 Incorrect or misleading explanations.

Do not assume that the existing implementation is complete.

Your goal is to **find problems through testing and reasoning**.

---

## 4. 🔧 Fix the Existing Problems

Modify the code to correct the problems you discover.

Your modifications should preserve the general Expert System architecture:

```text
🖥️ Hardware
     ↓
📥 Fact Acquisition
     ↓
🧠 Working Memory
     ↓
📚 Knowledge Base
     ↓
⚙️ Inference Engine
     ↓
💬 Explanation
     ↓
✅ Conclusion
```

Document the problems you found and explain how you fixed them.

---

## 5. 🧠 Improve the Inference Engine

The current system performs basic comparisons between expected and observed hardware information.

Extend the reasoning capabilities of the Expert System.

For example, create rules that can identify specific anomalies:

```text
IF disk information does not match
THEN identify a storage device anomaly
```

or:

```text
IF memory information does not match
THEN identify a memory module anomaly
```

The goal is not simply to report that something is different.

The Expert System should provide a **meaningful interpretation of the difference**. 💡

---

## 6. 💬 Improve the Explanation

Improve the output produced by the Expert System.

Instead of only reporting:

```text
The computer is not consistent.
```

the system should ideally provide useful evidence about **why**.

For example:

```text
⚠️ Hardware Integrity: ANOMALY DETECTED

Component: Disk

🧠 Inference:
    Storage device information does not match
    the expected configuration.
```

Design your own explanation format.

**Do not include real hardware identifiers in example outputs.**

---

## 7. ➕ Add a Missing Component

Extend the Expert System by adding at least **one additional hardware component**.

Possible choices include:

* 🎮 GPU
* 🌐 Network adapter
* 🔋 Battery
* 🔌 USB controller
* 🧩 Another WMI hardware class

For your new component:

1. 🔎 Identify the appropriate WMI class.
2. 📥 Collect its hardware information.
3. 🗄️ Determine what information the Knowledge Base would need to store.
4. 🧠 Create verification rules.
5. 🔗 Integrate the component into the inference process.
6. 🧪 Test both matching and mismatching cases.

You may represent Knowledge Base values using **placeholders or fictional values** in your code.

For example:

```text
<EXPECTED_SERIAL_NUMBER>
<EXPECTED_PROCESSOR_ID>
<EXPECTED_DISK_MODEL>
```

---

## 8. 🧪 Test Your Improvements

Create test cases that demonstrate that your modifications work.

At minimum, demonstrate:

### ✅ Test 1 — Consistent Hardware

```text
Expected hardware = Observed hardware
```

Result:

```text
✅ Hardware is consistent.
```

---

### ⚠️ Test 2 — One Anomaly

Change one component in the Knowledge Base.

Result:

```text
⚠️ Anomaly detected.
```

The system should identify the affected component.

**Do not present real hardware identifiers.**

---

### 🚨 Test 3 — Multiple Anomalies

Introduce changes to multiple components.

Result:

```text
🚨 Multiple anomalies detected.
```

The system should report the relevant evidence.

Use placeholders or fictional values in submitted examples.

---

## 9. 🔐 Hardware Data and Database Privacy

This assignment involves collecting hardware information that may contain **unique identifiers belonging to a physical computer**.

### ⚠️ Do not submit or publish your database.

Your submission must **not contain**:

* 🗄️ MySQL database dumps
* 📄 SQL files containing your hardware information
* 🔐 Real BIOS serial numbers
* 🔐 Real motherboard serial numbers
* 🔐 Real disk serial numbers
* 🔐 Real processor IDs
* 🔐 Real device identifiers
* 🔐 Other unique hardware identifiers from your computer

You may use your own computer and database **locally while developing and testing the system**.

However, your submitted project must contain only the **code and documentation necessary to demonstrate your implementation**.

If your code requires expected hardware values, use **placeholders or fictional values**, for example:

```python
expected_serial = "<EXPECTED_SERIAL_NUMBER>"
expected_processor_id = "<EXPECTED_PROCESSOR_ID>"
expected_disk_model = "<EXPECTED_DISK_MODEL>"
```

The purpose is to demonstrate how the Expert System **would interact with a Knowledge Base**, without submitting the actual Knowledge Base or personal hardware information.

---

## 10. 📦 Deliverables

### 💻 Code

Submit your modified Python Expert System.

Your code should demonstrate:

* 📥 Fact acquisition
* 🧠 Working memory
* 📚 Knowledge Base interaction
* ⚙️ Inference rules
* 💬 Explanation
* 🧪 Testing

Use placeholders or fictional values wherever expected hardware information must appear in the submitted code.

### 🗄️ Database

**Do not submit your database.**

Do not submit:

* MySQL dumps
* SQL database files
* Database exports
* Tables containing your hardware information
* Real hardware identifiers

The database is used only as part of your **local development and testing environment**.

### 📝 Documentation

Include a short report containing:

1. 🔎 **Problems discovered**
2. 🔧 **Changes made**
3. 🧠 **New rules added**
4. ➕ **New hardware component added**
5. 🧪 **Testing performed**
6. 📊 **Example outputs without real hardware values**
7. 💡 **What you learned about Expert Systems**

---

# 🚀 Final Challenge

The provided system is **not intended to be perfect**.

Your objective is not simply to make the program run.

Your objective is to make the Expert System:

* 🧠 **More intelligent**
* 🔎 **Better at detecting anomalies**
* 💬 **Better at explaining its reasoning**
* 🛠️ **More robust**
* ➕ **More capable of reasoning about hardware integrity**

Think like the designer of an Expert System:

> 🤔 **What facts does the system need?**
> 📚 **What knowledge should it store?**
> ⚙️ **What rules should it use?**
> 🧠 **What conclusions can it infer?**
> 💬 **How can it explain those conclusions?**
