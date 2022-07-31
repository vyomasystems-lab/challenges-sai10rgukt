# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/mux.v

TOPLEVEL := mux          # design
MODULE   := test_mux     # test
VHDL_SOURCES=
include $(shell cocotb-config --makefiles)/Makefile.sim
include $(shell cocotb-config --makefiles)/Makefile.inc

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
