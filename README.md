# Output PTV Vissim Parking Lot Occupancy

## Description

This repo contains a [PTV Vissim](https://www.ptvgroup.com/en/solutions/products/ptv-vissim/) integrated Python script that outputs a CSV file containing the parking lot occupancy per unit of time as defined by the user. A separate CSV file is output for each parking lot in the network.

Note: To use this script, you must have Python installed as well as the [pandas](https://pandas.pydata.org/) package.

---

### Supported PTV Vissim versions

- PTV Vissim 2020.00-xx
- PTV Vissim 11.00-xx

---

## Instructions

1. With a network open in PTV Vissim, open the Scripts list.

2. Create an entry in the Scripts list with the following attributes:

   - fromTime="0"
   - funcName="initialize"
   - name=""
   - no="1"
   - period="1"
   - runType="AFTSIMSTART"
   - scope="SIMULATIONRUN"
   - scriptFile="output-parking-lot-occupancy.py"
   - toTime="INF"

3. Create another entry in the Scripts list with the following attributes:

   - fromTime="0"
   - funcName="main"
   - name=""
   - no="2"
   - period="10"
   - runType="ATTMSTEPSTART"
   - scope="SIMULATIONRUN"
   - scriptFile="output-parking-lot-occupancy.py"
   - toTime="INF"
