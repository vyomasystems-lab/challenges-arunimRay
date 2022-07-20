# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    
    cocotb.log.info('##### CTB: Develop your test here ########')
     
    for i in range(5):
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

        inp = random.randint(0,3) 
        sel = dut.sel.value
        sel = random.randint(0,31)
        await Timer(2, units='ns')
        
        
        assert dut.out.value == inp[sel], "Randomised test failed with: select line {sel}, when input = {inp} the output is {out}".format(
            inp = inp[sel], sel=dut.sel.value, out=dut.out.value)
    


    





    

"""
    @cocotb.test()
    async def adder_basic_test(dut):
        
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
        make

        for i in range(5):

            sel = random.randint(0, 30)
            B = random.randint(0, 15)

            dut.a.value = A
            dut.b.value = B

            await Timer(2, units='ns')
            
            dut._log.info(f'A={A:05} B={B:05} model={A+B:05} DUT={int(dut.sum.value):05}')
            assert dut.sum.value == A+B, "Randomised test failed with: {A} + {B} = {SUM}".format(
                A=dut.a.value, B=dut.b.value, SUM=dut.sum.value)
"""