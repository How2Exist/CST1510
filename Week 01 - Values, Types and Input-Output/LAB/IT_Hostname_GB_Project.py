"""
RECORD CHECK  -  my version
===========================

Name  : Stefan Valev
Lane  :  IT      
Date  : 25/09/2026

Run it:   python IT_Hostname_GB_Project.py
"""


#Final version of the project at Excellent level:
hostname = input("Enter hostname: ")
used_GB = float(input("GB used: "))
total_GB = float(input("Total GB: "))

free = total_GB - used_GB
percentage = (used_GB / total_GB) * 100
# Free-space % is the metric IT monitoring alerts are usually based on
# (e.g. warn under 20% free), so it shows at a glance whether the host needs attention.
free_percentage = 100 - percentage
# Note to reader: I have intentionally made the output
# extremely inconvenient to read by writing everything 
# on one line. 
# Please don't kill me. - Stefan
print("=" * 30, f"\nRECORD CHECK: {hostname:>13}", "\n", "=" * 30, f"\nTotal: {total_GB:>20.2f}\nUsed: {used_GB:>21.2f}\nPercentage: {percentage:>15.2f}%\nFree: {free:+21.2f}\nFree %: {free_percentage:>19.2f}%", "\n", "=" * 30, sep = "")
