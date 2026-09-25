# Version 1.0
#hostname = input("Enter hostname: ")
#used_GB = float(input("GB used: "))
#total_GB = float(input("Total GB: "))
#
#print("=" * 30, f"\nRECORD CHECK: {hostname:>13}", "\n", "=" * 30, f"\nUsed: {used_GB:>21.2f}\nTotal: {total_GB:>20.2f}", sep = "")
#
#
#free = total_GB - used_GB
#percentage = (used_GB / total_GB) * 100
#print(f"Free: {free:+21.2f}\nPercentage: {percentage:>15.2f}%", "\n", "=" * 30, sep = "")


# Version 2.0
#hostname = input("Enter hostname: ")
#used_GB = float(input("GB used: "))
#total_GB = float(input("Total GB: "))
#
#print("=" * 30, f"\nRECORD CHECK: {hostname:>13}", "\n", "=" * 30, f"\nUsed: {used_GB:>21.2f}\nTotal: {total_GB:>20.2f}", sep = "")
#
#free = total_GB - used_GB
#percentage = (used_GB / total_GB) * 100
## Free-space % is the metric IT monitoring alerts are usually based on
## (e.g. warn under 20% free), so it shows at a glance whether the host needs attention.
#free_percentage = 100 - percentage
#print(f"Free: {free:+21.2f}\nPercentage: {percentage:>15.2f}%\nFree %: {free_percentage:>19.2f}%", "\n", "=" * 30, sep = "")


# Version 3.0
hostname = input("Enter hostname: ")
used_GB = float(input("GB used: "))
total_GB = float(input("Total GB: "))

free = total_GB - used_GB
percentage = (used_GB / total_GB) * 100
# Free-space % is the metric IT monitoring alerts are usually based on
# (e.g. warn under 20% free), so it shows at a glance whether the host needs attention.
free_percentage = 100 - percentage

print("=" * 30, f"\nRECORD CHECK: {hostname:>13}", "\n", "=" * 30, f"\nTotal: {total_GB:>20.2f}\nUsed: {used_GB:>21.2f}\nPercentage: {percentage:>15.2f}%\nFree: {free:+21.2f}\nFree %: {free_percentage:>19.2f}%", "\n", "=" * 30, sep = "")