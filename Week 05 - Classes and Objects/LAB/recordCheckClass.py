"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  IT
Date  :

Run it:   python recordCheckClass.py
"""

"""Record check: Compare rows loaded against rows expected for each dataset."""
 
from pathlib import Path
 
''' Looking for the file'''
Data_file = Path(__file__).resolve().parent / "records.txt"
Border = "=" * 34
 
 
class Record:
    """A dataset with its name, rows loaded and rows expected"""
 
    def __init__(self, label, value, limit):
        self.label = label  # dataset name
        self.value = value  # rows loaded
        self.limit = limit  # rows expected
 
    def percent(self):
        """Return rows loaded as a percentage of rows expected"""
        return self.value / self.limit * 100
 
    def status(self):
        """Return OVER LIMIT, WARNING or OK """
        pct = self.percent()
        if pct >= 100:
            return "OVER LIMIT"
        if pct >= 90:
            return "WARNING"
        return "OK"
 
    def free(self):
        """Return how many rows are left"""
        return max(self.limit - self.value, 0)
 
    def report(self, status):
        """Return the bordered report text for this record"""
        lines = [
            Border,
            f"  RECORD CHECK  -  {self.label}",
            Border,
            f"  {'Loaded':<12}: {self.value:>10,}",
            f"  {'Total':<12}: {self.limit:>10,}",
            f"  {'Remaining':<12}: {self.free():>10,}",
            f"  {'Percent':<12}: {self.percent():>10.2f} %",
            f"  {'Status':<12}: {status:>10}",
            Border,
        ]
        return "\n".join(lines)
 
 
def load_records(path):
    """Read label, value and limit lines from a file and return a list of Records"""
    records = []
    with open(path, encoding="utf-8") as file:
        for number, line in enumerate(file, start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = [part.strip() for part in line.split(",")]
            try:
                label, value, limit = parts[0], int(parts[1]), int(parts[2])
                if len(parts) != 3 or limit <= 0 or value < 0:
                    raise ValueError
            except (ValueError, IndexError):
                print(f"Skipping line {number}: {line!r}")
                continue
            records.append(Record(label, value, limit))
    return records
 
 
def main():
    """Load every record, print its report, then print the OVER LIMIT total"""
    records = load_records(Data_file)
    over_limit_count = 0
 
    for record in records:
        status = record.status()
        print(record.report(status))
        print(" ")
        if status == "OVER LIMIT":
            over_limit_count += 1
 
    print(f"Records checked : {len(records)}")
    print(f"OVER LIMIT total: {over_limit_count}")
 
 
if __name__ == "__main__":
    main()
 
 
