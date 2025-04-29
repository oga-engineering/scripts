# Runs the commands to create a simulatable file in Verilator

echo "Create and enter sim directory"
mkdir sim
cd sim

verilator --binary -j 0 -Wall ../rtl/$argv

cd ../
