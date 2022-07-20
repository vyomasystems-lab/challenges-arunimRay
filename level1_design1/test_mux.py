# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
     
    inp = [
    dut.inp0.value,
    dut.inp1.value, 
    dut.inp2.value, 
    dut.inp3.value,
    dut.inp4.value,
    dut.inp5.value,
    dut.inp6.value, 
    dut.inp7.value,
    dut.inp8.value,
    dut.inp9.value, 
    dut.inp10.value, 
    dut.inp11.value, 
    dut.inp12.value, 
    dut.inp13.value, 
    dut.inp14.value, 
    dut.inp15.value, 
    dut.inp16.value, 
    dut.inp17.value, 
    dut.inp18.value, 
    dut.inp19.value,  
    dut.inp20.value,
    dut.inp21.value, 
    dut.inp22.value, 
    dut.inp23.value,
    dut.inp24.value, 
    dut.inp25.value, 
    dut.inp26.value, 
    dut.inp27.value, 
    dut.inp28.value, 
    dut.inp29.value, 
    dut.inp30.value
    ]
     
    randomlist = random.randint(0,3,31)
    inp = randomList
    


    cocotb.log.info('##### CTB: Develop your test here ########')





    


@cocotb.test()
async def adder_basic_test(dut):
    """Test for 5 + 10"""

    A = 5
    B = 10

    # input driving
    dut.a.value = A
    dut.b.value = B

    await Timer(2, units='ns')
    
    assert dut.sum.value == A+B, "Adder result is incorrect: {A} + {B} != {SUM}, expected value={EXP}".format(
            A=int(dut.a.value), B=int(dut.b.value), SUM=int(dut.sum.value), EXP=A+B)


@cocotb.test()
async def adder_randomised_test(dut):
    """Test for adding 2 random numbers multiple times"""

    for i in range(5):

        sel = random.randint(0, 30)
        B = random.randint(0, 15)

        dut.a.value = A
        dut.b.value = B

        await Timer(2, units='ns')
        
        dut._log.info(f'A={A:05} B={B:05} model={A+B:05} DUT={int(dut.sum.value):05}')
        assert dut.sum.value == A+B, "Randomised test failed with: {A} + {B} = {SUM}".format(
            A=dut.a.value, B=dut.b.value, SUM=dut.sum.value)