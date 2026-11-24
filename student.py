import sys 

def total_marks(m1, m2, m3):
    return m1 + m2 + m3
def main():
    m1 = int(sys.argv[1])
    m2 = int(sys.argv[2])
    m3 = int(sys.argv[3])
    Total = total_marks(m1, m2, m3)
    Average = Total / 3
    percentage = (Total / 300) * 100
    print("Total Marks:", Total)
    print("Average Marks:", Average)
    print("Percentage:", percentage)
if __name__ == "__main__":
    main()