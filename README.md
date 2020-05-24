# Output PTV Vissim Parking Lot Occupancy

## Description

This repo contains a [PTV Vissim](https://www.ptvgroup.com/en/solutions/products/ptv-vissim/) integrated Python script that outputs a CSV file containing the parking lot occupancy per simulation second. A separate CSV file is output for each parking lot in the network.

Note: To use this script, you must have Python installed as well as the [pandas](https://pandas.pydata.org/) package.

<scripts>
		<script fromTime="0" funcName="initialize" name="" no="1" period="1" runType="AFTSIMSTART" scope="SIMULATIONRUN" scriptFile="#examples#Examples Training\Parking\Parallel Parking\output-parking-lot-occupancy.py" toTime="INF"/>
		<script fromTime="0" funcName="main" name="" no="2" period="10" runType="ATTMSTEPSTART" scope="SIMULATIONRUN" scriptFile="#examples#Examples Training\Parking\Parallel Parking\output-parking-lot-occupancy.py" toTime="INF"/>
</scripts>

---

### Supported PTV Vissim versions

- PTV Vissim 2020.00-xx
- PTV Vissim 11.00-xx

---

## Instructions
