"""
RECORD CHECK  -  my version
===========================

Name  : Stefan Valev
Lane  :  IT      
Date  : 25/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
#
#    Remember: input() always gives back text.

#label = ""      # : replace with an input() call
#first = 0.0     # : replace with an input() call, converted
#second = 0.0    # : replace with an input() call, converted


# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
#    - difference : how far the first is from the second
#    - percent    : the first as a percentage of the second
#
#    Do not type the answers. Calculate them.

#difference = 0.0   # 
#percent = 0.0      # 


# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign

#print()
#print("=" * 34)
#print(f"  RECORD CHECK  -  {label}")
#print("=" * 34)

# : your report lines go here

#print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you


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
# extremely difficult to read by writing everything 
# on one line. 
# Please don't kill me. - Stefan
print("=" * 30, f"\nRECORD CHECK: {hostname:>13}", "\n", "=" * 30, f"\nTotal: {total_GB:>20.2f}\nUsed: {used_GB:>21.2f}\nPercentage: {percentage:>15.2f}%\nFree: {free:+21.2f}\nFree %: {free_percentage:>19.2f}%", "\n", "=" * 30, sep = "")