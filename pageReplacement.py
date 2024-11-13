# FIFO
# LRU
# Optimal

class PageReplacement:
    def __init__(self, no: int, pages: list) -> None:
        self.max_frames = no
        self.pageNumbers = pages
    
    def FIFO(self):
        frame = []
        misscount = 0
        print(self.pageNumbers)
        for i in self.pageNumbers:
            if i not in frame:
                misscount += 1
                if len(frame) == self.max_frames:
                    frame.pop(0)
                frame.append(i)
                print(f"{i}    MISS    {frame}")
            else:
                print(f"{i}    HIT    {frame}")
        return misscount, len(self.pageNumbers) - misscount

    def Optimal(self):
        frame = []
        misscount = 0
        for i in range(len(self.pageNumbers)):
            if self.pageNumbers[i] not in frame:
                misscount += 1
                if len(frame) == self.max_frames:
                    maxdist = -1
                    maxidx = -1
                    for ind, page in enumerate(frame):
                        if page in self.pageNumbers[i + 1:]:
                            dist = self.pageNumbers[i+1:].index(page)
                        else:
                            dist = float('inf')
                        if dist > maxdist:
                            maxdist = dist
                            maxidx = ind
                    frame[maxidx] = self.pageNumbers[i]
                else:
                    frame.append(self.pageNumbers[i])
                print(f"{self.pageNumbers[i]}    MISS    {frame}")
            else:
                print(f"{self.pageNumbers[i]}    HIT    {frame}")
        return misscount, len(self.pageNumbers) - misscount
    
    def LRU(self):
        frame = []
        frame_age = []
        misscount = 0
        for i in range(len(self.pageNumbers)):
            for j in range(len(frame_age)):
                frame_age[j] += 1
            if self.pageNumbers[i] not in frame:
                misscount += 1
                if self.max_frames == len(frame):
                    max_ind = frame_age.index(max(frame_age))
                    frame[max_ind] = self.pageNumbers[i]
                    frame_age[max_ind] = 0
                else:
                    frame.append(self.pageNumbers[i])
                    frame_age.append(0)
                print(f"{self.pageNumbers[i]}    MISS    {frame}")
            else:
                # print(self.pageNumbers[i])
                index = frame.index(self.pageNumbers[i])
                frame_age[index] = 0
                print(f"{self.pageNumbers[i]}    HIT    {frame}")
                
        return misscount, len(self.pageNumbers) - misscount
    
frames = [17,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
algo = PageReplacement(3,frames)
frame_miss_count = 0
frame_hit_count = 0

print("FIFO.....")
frame_miss_count, frame_hit_count = algo.FIFO()
print("Hit count: " + str(frame_hit_count) + " Miss count: " + str(frame_miss_count))
print()

print("LRU.......")
frame_miss_count, frame_hit_count = algo.LRU()
print("Hit count: " + str(frame_hit_count) + " Miss count: " + str(frame_miss_count))
print()

print("Optimal......")
frame_miss_count, frame_hit_count = algo.Optimal()
print("Hit count: " + str(frame_hit_count) + " Miss count: " + str(frame_miss_count))
print()
