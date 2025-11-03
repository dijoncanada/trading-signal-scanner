import subprocess
import sys

# Make sure we use the right python and capture live logs
cmd = [sys.executable, "scanner.py"]

print("🔍 Running AI Leaders Scanner...")
try:
    output = subprocess.check_output(cmd).decode()
    print("\n----- SCANNER RESULTS -----\n")
    print(output)

    # Save results to a text file for easy review later
    with open("daily_scanner_output.txt", "w") as f:
        f.write(output)

    print("\n✅ Done! Results saved in daily_scanner_output.txt")

except subprocess.CalledProcessError as e:
    print("\n❌ Scanner failed:")
    print(e.output.decode())
