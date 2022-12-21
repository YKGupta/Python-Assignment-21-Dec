# Slice list into 3 equal chunks and reverse each chunk
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
chunk1 = sample_list[:len(sample_list)//3]
chunk2 = sample_list[len(sample_list)//3:2*len(sample_list)//3]
chunk3 = sample_list[2*len(sample_list)//3:]
print("Chunk 1", chunk1)
chunk1 = chunk1[::-1]
print("After reversing it", chunk1)
print("Chunk 2", chunk2)
chunk2 = chunk2[::-1]
print("After reversing it", chunk2)
print("Chunk 3", chunk3)
chunk3 = chunk3[::-1]
print("After reversing it", chunk3)