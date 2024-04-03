# Re-establishing the given values
source_instructions = 18920 # Source instructions
initial_defect_density = 25  # Defects per KLOC
object_instructions_per_source = 4.5  # Object instructions per source instruction
execution_rate_MIPS = 176  # Execution rate in MIPS
fault_exposure_ratio = 6e-7  # Fault-exposure ratio

# Convert execution rate to instructions per second
execution_rate_instructions_per_second = execution_rate_MIPS * 1e6

# Calculate the total number of object instructions per second
total_object_instructions_per_second = source_instructions * object_instructions_per_source

# Calculate β1 using the fault-exposure ratio and the total object instructions per second
beta1 = fault_exposure_ratio / (total_object_instructions_per_second / execution_rate_instructions_per_second)
beta1
print(beta1)