# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')
    for i in range(100): # 100 experiments
        
        exact = random.randint(0, 255) # generate randomized input
        dut.d.value = exact # drive pins
        
        await FallingEdge(dut.clk) # wait for falling edge
        
        computed = dut.q.value.integer # Read pins as unsigned integer.
        # computed = dut.q.value.signed_integer # Read pins as signed integer.
        
        assert exact == computed, f"Failed on the {i}th cycle. Got {computed}, expected {exact}" # If any assertion fails, the test fails, and the string would be printed in console
        print(f"Driven value: {exact} \t received value: {computed}")
