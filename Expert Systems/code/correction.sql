#Instruction: Make the changes to match your correct data
USE KnowledgeBase;

UPDATE disks
SET serialNumber = ''
WHERE diskID = 1;

USE KnowledgeBase;
UPDATE memory
SET partNumber = ''
WHERE memoryID = 1;