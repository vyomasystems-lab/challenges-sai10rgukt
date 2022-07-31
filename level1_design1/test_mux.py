# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure
@cocotb.test()
def test_mux(dut):
    """Test for mux2"""
    cocotb.log.info('##### CTB: Develop your test here ########')
   
    dut.sel.value=30
    dut.inp24.value=0
    dut.inp22.value=0
    dut.inp30.value=2
    
    yield Timer(1,"ns")
    if dut.out !=2:
        print("Failure!")
    

    