# ymdhms_to_jd.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute sec.
#  Text explaining script usage
# Parameters:
#  year
#  month
#  day
#  hour
#  minute
#  sec
#  ...
# Output:
#  jd_frac
#
# Written by Olivia Powell
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math as m # math ops
import numpy as np # matrix function

# "constants"
r_e_km = 6378.137 # redius of earth
e_e = 0.081819221456 # eccentricity of earth

# helper functions

## function description
## calculated denominator
def calc_denom(ecc, lat_rad):
  return m.sqrt(1.0-(ecc**2)*(m.sin(lat_rad)**2))

# initialize script arguments
year = float('nan')
month = float('nan')
day = float('nan')
hour = float('nan')
minute = float('nan')
sec = float('nan')

# parse script arguments
if len(sys.argv)==7:
  year = float(sys.argv[1])
  month = float(sys.argv[2])
  day = float(sys.argv[3])
  hour = float(sys.argv[4])
  minute = float(sys.argv[5])
  sec = float(sys.argv[6])
  ...
else:
  print(\
   'Usage: '\
   'python3 ymdhms_to_jd.py year month day hour minute sec'\
  )
  exit()

# write script below this line
def solve_jd_frac(year, month, day, hour, minute, sec):
  jd = day-32075+\
    int(1461*(year+4800+int((month-14)/12))/4)+\
    int(367*(month-2-int((month-14)/12)*12)/12) \
    -int(3*int((year+4900+int((month-14)/12))/100)/4)
  jd_midnight = jd-0.5
  d_frac = (sec+60*(minute+60*hour))/86400
  jd_frac = jd_midnight+d_frac
  return jd_frac

jd_frac = solve_jd_frac(year, month, day, hour, minute, sec)

#print
print(jd_frac)