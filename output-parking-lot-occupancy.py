# ==========================================================================
# Python Script for PTV Vissim 11
# Copyright (C) PTV Group, Jared Best
# All rights reserved.
# ==========================================================================
import pandas as pd


def initialize():
    global number_of_executions
    number_of_executions = 0
    return


def main():
    global number_of_executions
    simulation_second = Vissim.Net.Simulation.AttValue('SimSec')
    all_parking_lot_attributes = Vissim.Net.ParkingLots.GetMultipleAttributes(
        ('No', 'Name', 'Capacity', 'CurrentOccup'))
    for Count in range(len(all_parking_lot_attributes)):
        dfOutput = pd.DataFrame({'Time': simulation_second,
                                 'No': all_parking_lot_attributes[Count][0],
                                 'Name': all_parking_lot_attributes[Count][1],
                                 'Capacity': all_parking_lot_attributes[Count][2],
                                 'CurrentOccup': all_parking_lot_attributes[Count][3]}, index=[0])

        dfOutput.index.name = 'Index'
        dfOutput.reset_index(drop=True)
        if number_of_executions == 0:
            dfOutput.to_csv(
                'ParkingLot' + str(all_parking_lot_attributes[Count][0]) + '.csv', sep=';', mode='a')
        else:
            dfOutput.to_csv(
                'ParkingLot' + str(all_parking_lot_attributes[Count][0]) + '.csv', sep=';', mode='a', header=None)
    number_of_executions += 1
    return
