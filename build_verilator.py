# This is a script that will build the verilator file to run.
import subprocess
import os

#file_list=["../rtl/ip_codma_pkg.sv" , "../rtl/ip_codma_crc.sv" , "../rtl/ip_codma_interfaces_verilator.sv" , "../rtl/ip_codma_main_machine.sv" , "../rtl/ip_codma_rd_machine.sv" , "../rtl/ip_codma_wr_machine.sv", "../rtl/ip_codma_top.sv" ]
with open('../rtl/file_list.txt','r') as f:
    file_list = [f"../rtl/{line.strip()}" for line in f if line.strip()]

print(file_list)
verilator_cmd=[ "verilator", "--binary", "-j", "0", "-Wall", "-Wno-DECLFILENAME", "-Wno-fatal"] + file_list

subprocess.run(verilator_cmd,check=True)